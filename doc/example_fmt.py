# -*- coding: utf-8 -*-

class CsvFormatter:
    def __init__(self, format_map):
        """
        Validate and initialize the format_map
        """
        if not isinstance(format_map, dict):
            raise TypeError('The format_map parameter provided to instantiate the class must be a dictionary')
        self._verify_map(format_map)
        self.format_map = format_map

    def _verify_map(self, format_map):
        """
        Validates the format_map looking for unknown format specifiers.  The format
        specifiers are considered to be valid if the instance has a method with a
        name that matches the pattern _fmt_<format_specifier>.
        """
        invalid_formats = set([])
        for value in format_map.values():
            if not hasattr(self, '_fmt_{:s}'.format(value)):
                invalid_formats.add(value)

        if invalid_formats:
            format_names = ', '.join(sorted(invalid_formats))
            msg = 'Invalid format specifier(s) in map:  {:s}'.format(format_names)
            raise ValueError(msg)
        
    def _fmt_default(self, val):
        """
        This formatter returns the value unmodified.
        """
        return val

    def _fmt_us_currency(self, val):
        """
        This formatter returns the value formatted as US currency.
        """
        try:
            the_float = float(val)
            return '${:.2f}'.format(the_float)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the us_currency formatter'.format(str(val)))

    def _fmt_thousands_us_currency(self, val):
        """
        This formatter returns the value formatted as US currency with a comma as the thousands separator
        """
        try:
            the_float = float(val)
            return '${:,.2f}'.format(the_float)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the thousands_us_currency formatter'.format(str(val)))

    def _fmt_integer(self, val):
        """
        This formatter returns the value formatted as an integer.
        """
        try:
            the_integer = int(val)
            return '{:d}'.format(the_integer)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the integer formatter'.format(str(val)))

    def _fmt_thousands_integer(self, val):
        """
        This formatter returns the value formatted with commas separating the thousands.
        """
        try:
            the_integer = int(val)
            return '{:,d}'.format(the_integer)
        except (ValueError, TypeError) as e:
            raise ValueError('The value "{:s}" is not valid for the thousands_integer formatter'.format(str(val)))
        
    def format(self, record):
        """
        Applies the formatting rules to the specified record.
        """
        if not isinstance(record, dict):
            raise TypeError('The record parameter must be a dictionary')

        new_record = {}
        failed_formats = []
        for key in record.keys():
            try:
                new_record[key] = getattr(self, '_fmt_{:s}'.format(self.format_map.get(key, 'default')))(record[key])
            except ValueError as e:
                failed_formats.append(key)
                new_record[key] = record[key]
        return sorted(failed_formats), new_record
