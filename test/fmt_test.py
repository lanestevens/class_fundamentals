# -*- coding: utf-8 -*-
import os
import sys
import textwrap

try:
    from src.fmt import CsvFormatter
except Exception:
    CsvFormatter = None

def format_msg(msg):
    lines = '\n'.join(textwrap.wrap(msg))
    return '\n{:s}'.format(lines)

#The next few tests validate the setup.
def test_virtualenv():
    """
    It should operate in an active virtual environment.
    """
    msg = 'An active virtual environment was not detected.  Activate the virtual environment following the steps in the setup instructions'
    assert os.getenv('VIRTUAL_ENV'), format_msg(msg)

def test_python_3():
    """
    It should be version 3 of python.
    """
    msg = 'You must use version 3 of python.  Please follow the setup instructions to correct this'
    assert 3 == sys.version_info[0], format_msg(msg)
    
def test_cwd():
    """
    It should run tests from a child directory of the virtual environment.
    """
    cwd = os.getcwd()
    virtual_env = os.getenv('VIRTUAL_ENV')
    msg = 'It is expected that the tests be run from the project root, which is a child of the virtual env.  Please change directory to the project root'
    assert os.path.dirname(cwd) == virtual_env, format_msg(msg)

def test_project_sanity():
    """
    It should run tests from the project root
    """
    cwd = os.getcwd()
    file_path = os.path.realpath(__file__)
    file_directory = os.path.dirname(file_path)
    expected_directory = os.path.dirname(file_directory)
    msg = 'It is expected that the tests be run from the project root.  Please change directory to {:s}.'.format(expected_directory)
    assert os.path.dirname(file_directory) == cwd, format_msg(msg)
    
#These tests validate the module tasks.
def test_fmt_exists():
    """
    It should include a file named ./src/fmt.py
    """
    cwd = os.getcwd()
    msg = 'The file {:s}/src/fmt.py is expected. Create this file per the task instructions.'.format(cwd)
    assert os.path.isfile('./src/fmt.py'), format_msg(msg)

def test_class_exists():
    """
    It should create a class named CsvFormatter.
    """
    cwd = os.getcwd()
    msg = 'The file {:s}/src/fmt.py is expected to define the class CsvFormatter.  Create this class per the task instructions'.format(cwd)
    assert CsvFormatter, format_msg(msg)

def test_override_init_method():
    """
    It should override the __init__ method.
    """
    try:
        CsvFormatter(1)
    except TypeError as e:
        msg = 'It is expected that you will override the __init__ method with a method of 1 parameter.  Please see the task instructions'
        assert e.args[0] != 'object() takes no parameters', format_msg(msg)
        
def test_init_type_error():
    """
    It should override the __init__ method and validate the format_map.
    """
    for bad_type in (1, '', [], None):
        try:
            csv_formatter = CsvFormatter(bad_type)
            msg = 'The __init__ method must raise a TypeError if the parameter is not a dictionary instance'
            assert False, format_msg(msg)
        except TypeError as e:
            if e.args[0] == 'object() takes no parameters':
                msg = 'It is expected that you will override the __init__ method with a method of 1 parameter.  Please see the task instructions'
                assert False, format_msg(msg)
            msg = 'The exception message is expected to be:  "The format_map parameter provided to instantiate the class must be a dictionary"'
            assert e.args[0] == 'The format_map parameter provided to instantiate the class must be a dictionary', format_msg(msg)

def test_instantiate_success():
    """
    It should set format_map on self as part of the instantiate of the class instance.
    """
    format_map = {'column': 'default'}
    csv_formatter = CsvFormatter(format_map)
    msg = 'The instance is expected to have an attribute named "format_map." Verify that this attribute is being assigned.'
    assert hasattr(csv_formatter, 'format_map'), format_msg(msg)
    msg = 'The format_map attribute of the instance must match the value of the supplied parameter.  Verify that the correct value is being assigned.'
    assert format_map == csv_formatter.format_map, format_msg(msg)

def test_check_method_exists():
    """
    It should have a method named _verify_map.
    """
    csv_formatter = CsvFormatter({})
    msg = 'It must have a method named _verify_map.  Please refer to the tasks and requirements.'
    assert hasattr(csv_formatter, '_verify_map'), format_msg(msg)

def test_unknown_values():
    """
    It should raise a ValueError if there is an unknown value.  All unknown values will be reported in the exception.
    """
    csv_formatter = CsvFormatter({})
    try:
        csv_formatter._verify_map({'column1': 'unknown1', 'column2': 'unknown2', 'column3': 'an_unknown'})
        msg = 'The _verify_map method must raise an exception if there are invalid format specifiers'
        assert False, format_msg(msg)
    except ValueError as e:
        expected_message = 'Invalid format specifier(s) in map:  an_unknown, unknown1, unknown2'
        msg = 'Incorrect message returned from the exception:  "{:s}."  The expected message is:  "{:s}."  Please see tasks and requirements'.format(e.args[0], expected_message)
        assert e.args[0] == expected_message, format_msg(msg)

def test_known_values():
    """
    It should not raise an exception if there are not any invalid format specifiers.
    """
    csv_formatter = CsvFormatter({})
    try:
        format_map = {'column1': 'default',
                      'column2': 'us_currency',
                      'column3': 'thousands_us_currency',
                      'column4': 'integer',
                      'column5': 'thousands_integer',
                      }
        result = csv_formatter._verify_map(format_map)
        msg = 'It is expected that the _verify_map method return None on success'
        assert result is None, format_msg(msg)
    except ValueError as e:
        msg = 'An unexpected ValueError was raised.  This likely indicates that one or more valid format specifiers was not accounted for.  See the tasks and requirements for the list of valid specifiers.'
        assert False, format_msg(msg)

def test_init_validates_map():
    """
    It should validate the map during initialization.
    """
    bad_map = {'column1': 'unknown1', 'column2': 'unknown2'}
    try:
        csv_formatter = CsvFormatter(bad_map)
        msg = 'An expected ValueError exception was not raised.  The __init__ method should validate the format_map with the _verify_map method'
        assert False, format_msg(msg)
    except ValueError as e:
        expected_message = 'Invalid format specifier(s) in map:  unknown1, unknown2'
        msg = 'The ValueError message does not match the expected message:  Your message {:s} != Expected message {:s}'.format(e.args[0], expected_message)
        assert e.args[0] == expected_message, format_msg(msg)

def test_has_fmt_default():
    """
    It should have a method named _fmt_default.
    """
    csv_formatter = CsvFormatter({})
    msg = 'The class must have a method named _fmt_default to implement the default format specifier'
    assert hasattr(csv_formatter, '_fmt_default'), format_msg(msg)
    
def test_fmt_default_success():
    """
    It should return the value it was provided.
    """
    csv_formatter = CsvFormatter({})
    msg = 'The _fmt_default method should return its input'
    test_cases = ('123',
                  'onetwothree',
                  )
    for test_case in test_cases:
        assert csv_formatter._fmt_default(test_case) == test_case, format_msg(msg)

def test_has_fmt_us_currency():
    """
    It should have a method named _fmt_us_currency
    """
    csv_formatter = CsvFormatter({})
    msg = 'The class must have a method named _fmt_us_currency'
    assert hasattr(csv_formatter, '_fmt_us_currency'), format_msg(msg)

def test_fmt_us_currency_value_error():
    """
    It should raise a ValueError if the value is not a representation of a float.
    """
    csv_formatter = CsvFormatter({})
    for test_case in ('bad', None):
        try:
            csv_formatter._fmt_us_currency(test_case)
            msg = 'The _fmt_us_currency must raise an exception when the value is not a representation of a floating point number'
            assert False, format_msg(msg)
        except ValueError as e:
            expected_message = 'The value "{:s}" is not valid for the us_currency formatter'.format(str(test_case))
            msg = 'The exception message did not match the expected message:  Your message: {:s} != Expected message {:s}'.format(e.args[0], expected_message)
            assert expected_message == e.args[0], format_msg(msg)

def test_fmt_us_currency_success():
    """
    It should return a value formatted as us currency - without commas
    """
    csv_formatter = CsvFormatter({})
    expected_result = '$12345.00'
    test_cases = ('12345', '12345.000')
    for test_case in test_cases:
        result = csv_formatter._fmt_us_currency(test_case)
        msg = 'The _fmt_us_currency method must return a formatted string, not None'
        assert result is not None, format_msg(msg)
        msg = 'The expected result was not produced:  Your result: {:s} != Expected result: {:s}'.format(result, expected_result)
        assert result == expected_result, format_msg(msg)

def test_has_fmt_thousands_us_currency():
    """
    It should have a _fmt_thousands_us_currency method.
    """
    csv_formatter = CsvFormatter({})
    msg = 'The class must have a method named thousands_us_currency'
    assert hasattr(csv_formatter, '_fmt_thousands_us_currency'), format_msg(msg)

def test_fmt_thousands_us_currency_value_error():
    """
    It should raise a ValueError if the value is not a representation of a float.
    """
    csv_formatter = CsvFormatter({})
    for test_case in ('bad', None):
        try:
            csv_formatter._fmt_thousands_us_currency(test_case)
            msg = 'The _fmt_thousands_us_currency must raise an exception when the value is not a representation of a floating point number'
            assert False, format_msg(msg)
        except ValueError as e:
            expected_message = 'The value "{:s}" is not valid for the thousands_us_currency formatter'.format(str(test_case))
            msg = 'The exception message did not match the expected message:  Your message: {:s} != Expected message {:s}'.format(e.args[0], expected_message)
            assert expected_message == e.args[0], format_msg(msg)

def test_fmt_thousands_us_currency_success():
    """
    It should return a value formatted as us currency - with commas
    """
    csv_formatter = CsvFormatter({})
    expected_result = '$12,345.00'
    test_cases = ('12345', '12345.000')
    for test_case in test_cases:
        result = csv_formatter._fmt_thousands_us_currency(test_case)
        msg = 'The _fmt_thousands_us_currency method must return a formatted string, not None'
        assert result is not None, format_msg(msg)
        msg = 'The expected result was not produced:  Your result: {:s} != Expected result: {:s}'.format(result, expected_result)
        assert result == expected_result, format_msg(msg)

def test_has_fmt_thousands_integer():
    """
    It should have a method _fmt_thousands_integer
    """
    csv_formatter = CsvFormatter({})
    msg = 'The class must have a method named _fmt_thousands_integer'
    assert hasattr(csv_formatter, '_fmt_thousands_integer'), format_msg(msg)

def test_fmt_thousands_integer_value_error():
    """
    It should raise a ValueError if the value does not represent a valid integer.
    """
    csv_formatter = CsvFormatter({})
    for test_case in ('bad', None):
        try:
            csv_formatter._fmt_thousands_integer(test_case)
            msg = 'The _fmt_thousands_integer must raise an exception when the value is not a representation of an integer'
            assert False, format_msg(msg)
        except ValueError as e:
            expected_message = 'The value "{:s}" is not valid for the thousands_integer formatter'.format(str(test_case))
            msg = 'The exception message did not match the expected message:  Your message: {:s} != Expected message {:s}'.format(e.args[0], expected_message)
            assert expected_message == e.args[0], format_msg(msg)

def test_fmt_thousands_integer():
    """
    It should return a value formatted as an integer with commas grouping thousands.
    """
    csv_formatter = CsvFormatter({})
    expected_result = '12,345'
    result = csv_formatter._fmt_thousands_integer('12345')
    msg = 'The _fmt_thousands_integer method must return a formatted string, not None'
    assert result is not None, format_msg(msg)
    msg = 'The expected result was not produced:  Your result: {:s} != Expected result: {:s}'.format(result, expected_result)
    assert result == expected_result, format_msg(msg)

    
def test_has_fmt_integer():
    """
    It should have a method named _fmt_integer
    """
    csv_formatter = CsvFormatter({})
    msg = 'The class must have a method named _fmt_integer'
    assert hasattr(csv_formatter, '_fmt_integer'), format_msg(msg)

def test_fmt_integer_value_error():
    """
    It should raise a ValueError exception if the value is not an integer.
    """
    csv_formatter = CsvFormatter({})
    for test_case in ('bad', None):
        try:
            csv_formatter._fmt_integer(test_case)
            msg = 'The _fmt_integer must raise an exception when the value is not a representation of an integer'
            assert False, format_msg(msg)
        except ValueError as e:
            expected_message = 'The value "{:s}" is not valid for the integer formatter'.format(str(test_case))
            msg = 'The exception message did not match the expected message:  Your message: {:s} != Expected message {:s}'.format(e.args[0], expected_message)
            assert expected_message == e.args[0], format_msg(msg)

def test_fmt_integer():
    """
    It should return a value formatted as an integer with commas grouping thousands.
    """
    csv_formatter = CsvFormatter({})
    expected_result = '12345'
    result = csv_formatter._fmt_integer('012345')
    msg = 'The _fmt_integer method must return a formatted string, not None'
    assert result is not None, format_msg(msg)
    msg = 'The expected result was not produced:  Your result: {:s} != Expected result: {:s}'.format(result, expected_result)
    assert result == expected_result, format_msg(msg)

def test_has_format_method():
    """
    It should have an __exec__ method
    """
    csv_formatter = CsvFormatter({})
    msg = 'The class must have a method named format'
    assert hasattr(csv_formatter, 'format'), format_msg(msg)

def test_format_type_error():
    """
    It should raise a TypeError if the parameter passed to the method is not a dictionary.
    """
    csv_formatter = CsvFormatter({})
    test_cases = (1, 'one', None, [],)
    for test_case in test_cases:
        try:
            csv_formatter.format(test_case)
            msg = 'The method must raise a TypeError if the supplied parameter is not a dictionary'
            assert False, format_msg(msg)
        except TypeError as e:
            expected_message = 'The record parameter must be a dictionary'
            msg = 'Your message:  {:s} != Expected message {:s}'.format(e.args[0], expected_message)
            assert e.args[0] == expected_message, format_msg(msg)
    
def test_format_with_all_exceptions():
    """
    It should return a tuple with a list of failed formats as the first element and the formatted record as the second
    if there are any exceptions raised during formatting.
    """
    format_map = {'column1': 'integer',
                  'column2': 'thousands_integer',
                  'column3': 'us_currency',
                  }

    csv_formatter = CsvFormatter(format_map)
    record = {'column1': 'so',
              'column2': 'many',
              'column3': 'errors',
              }
    result = csv_formatter.format(record)
    msg = 'The result must be a tuple with a list of failed columns and the modified record'
    assert isinstance(result, tuple), format_msg(msg)

    msg = 'The list of columns does not match the expected list'
    assert result[0] == ['column1', 'column2', 'column3'], format_msg(msg)

    msg = 'The record should not have been modified'
    assert result[1] == record, format_msg(msg)
    
def test_format_with_one_exception():
    """
    It should format the fields that it can.
    """
    format_map = {'column1': 'integer',
                  'column2': 'thousands_integer',
                  'column3': 'us_currency',
                  }

    csv_formatter = CsvFormatter(format_map)
    record = {'column1': '012345',
              'column2': 'many',
              'column3': '1.23',
              }
    expected_record = {'column1': '12345',
                       'column2': 'many',
                       'column3': '$1.23',
                       }
    result = csv_formatter.format(record)
    msg = 'The result must be a tuple with a list of failed columns and the modified record'
    assert isinstance(result, tuple), format_msg(msg)

    msg = 'The list of columns does not match the expected list'
    assert result[0] == ['column2'], format_msg(msg)

    msg = 'The formatted record does not match the expected formatting'
    assert result[1] == expected_record, format_msg(msg)
    
def test_format_full_success():
    """
    It should return an empty list of failures and a fully modified record when no exceptions.
    """
    format_map = {'column1': 'integer',
                  'column2': 'thousands_integer',
                  'column3': 'us_currency',
                  }

    csv_formatter = CsvFormatter(format_map)
    record = {'column1': '012345',
              'column2': '0654321',
              'column3': '1.23',
              }
    expected_record = {'column1': '12345',
                       'column2': '654,321',
                       'column3': '$1.23',
                       }
    result = csv_formatter.format(record)
    msg = 'The result must be a tuple with an empty list of failed columns and the modified record'
    assert isinstance(result, tuple), format_msg(msg)

    msg = 'The list of columns is not empty'
    assert result[0] == [], format_msg(msg)

    msg = 'The formatted record does not match the expected formatting'
    assert result[1] == expected_record, format_msg(msg)
