# -*- coding: utf-8 -*-
import argparse
import csv
import os
import sys
sys.path.append(os.path.join(os.getcwd(), 'src'))

# try:
#     from fmt import CsvFormatter
# except Exception:
#     CsvFormatter = None
from fmt import CsvFormatter

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-m', '--format-map')
if __name__ == '__main__':
    args = arg_parser.parse_args()
    the_map = {}
    if args.format_map:
        try:
            with open(args.format_map, 'r') as f:
                rows = csv.DictReader(f)
                for row in rows:
                    the_map[row['column']] = row['formatter']
        except:
            print('Error! Unable to open {:s}. Aborting'.format(args.format_map))
            sys.exit(1)

    csv_formatter = None
    if CsvFormatter:
        try:
            csv_formatter = CsvFormatter(the_map)
        except ValueError:
            print('Error! Unsupported format specifiers in {:s}. Aborting'.format(args.format_map), file=sys.stderr)
            sys.exit(1)
        
    rows = csv.DictReader(sys.stdin)
    formatted_rows = csv.DictWriter(sys.stdout, rows.fieldnames)
    formatted_rows.writeheader()
    unformatted_rows = csv.DictWriter(sys.stderr, rows.fieldnames)
    unformatted_rows.writeheader()
    for row in rows:
        if csv_formatter:
            result = csv_formatter.format(row)
            if result[0]:
                unformatted_rows.writerow(row)
            else:
                formatted_rows.writerow(result[1])
