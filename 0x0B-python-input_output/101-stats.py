#!/usr/bin/python3
import sys

def print_metrics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        for line in sys.stdin:
            if line_count % 10 == 0 and line_count > 0:
                print_metrics(total_size, status_counts)
            line_count += 1
            parts = line.split()
            if len(parts) >= 9:
                try:
                    size = int(parts[-1])
                    status_code = int(parts[-2])
                    total_size += size
                    if status_code in status_counts:
                        status_counts[status_code] += 1
                except ValueError:
                    pass
    except KeyboardInterrupt:
        pass
    print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
