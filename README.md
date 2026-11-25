# CSV to JSON

Convert a CSV file to JSON. Each row becomes one JSON object keyed
by the header row, and the result is a JSON array — written to a
file with `-o`, or printed to standard output when no output file
is given.

## Requirements

- Python 3 (standard library only, no extra packages)

## Usage

```bash
python3 main.py data.csv
python3 main.py data.csv -o data.json
python3 main.py data.csv -o data.json --delimiter ";" --indent 4
```

## Example

```bash
$ cat people.csv
name,age,city
Ayesha,28,Lahore
Bilal,31,Karachi

$ python3 main.py people.csv -o people.json
Converted 2 row(s): people.csv -> people.json

$ cat people.json
[
  {
    "name": "Ayesha",
    "age": "28",
    "city": "Lahore"
  },
  {
    "name": "Bilal",
    "age": "31",
    "city": "Karachi"
  }
]
```

## License

MIT — see [LICENSE](LICENSE).
