#!/usr/bin/python3
"""Module the computed metrics."""

import sys


def print_metrics(total_size, status_codes):
    """Print the computed metrics."""
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.keys())
    for code in sorted_status_codes:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


line_count = 0
total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

try:
    for line in sys.stdin:
        try:
            fields = line.split()
            if len(fields) >= 2:
                status_code = fields[-2]
                total_size += int(fields[-1])
                if status_code in status_codes:
                    status_codes[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)

        except (IndexError, ValueError):
            pass

except KeyboardInterrupt:
    pass

finally:
    print_metrics(total_size, status_codes)
