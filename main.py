#!/usr/bin/env python3
"""Convert a CSV file to JSON.

Each CSV row becomes one JSON object keyed by the header row.
Output is a JSON array, written to a file with ``-o`` or printed
to standard output when no output file is given.
"""
import argparse
import csv
import json
import sys


def convert(input_path, delimiter=",", encoding="utf-8"):
    """Read a CSV file and return a list of row dicts."""
    with open(input_path, newline="", encoding=encoding) as handle:
        reader = csv.DictReader(handle, delimiter=delimiter)
        if reader.fieldnames is None:
            raise ValueError(f"no header row found in {input_path}")
        rows = [row for row in reader if any(
            (value or "").strip() for value in row.values() if value is not None)]
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert a CSV file to JSON.")
    parser.add_argument("input", help="input CSV file")
    parser.add_argument("-o", "--output",
                        help="output JSON file (default: print to stdout)")
    parser.add_argument("--delimiter", default=",",
                        help="CSV field delimiter (default: ',')")
    parser.add_argument("--indent", type=int, default=2,
                        help="JSON indent spaces (default: 2, use 0 for compact)")
    parser.add_argument("--encoding", default="utf-8",
                        help="input file encoding (default: utf-8)")
    args = parser.parse_args(argv)

    try:
        rows = convert(args.input, delimiter=args.delimiter,
                       encoding=args.encoding)
    except FileNotFoundError:
        print(f"error: file not found: {args.input}", file=sys.stderr)
        return 1
    except (ValueError, csv.Error, UnicodeDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    text = json.dumps(rows, indent=args.indent or None,
                      ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
        print(f"Converted {len(rows)} row(s): {args.input} -> {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
