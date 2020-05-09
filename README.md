# Klassen

A Python utility to generate statistics for assigned CPC/IPC classes.

## Description

This script provides functions to ...

1. read a matrix of CPC (IPC) classes from a CSV file,
2. generate frequency counts for all unique elements, and
3. generate a bar chart plot for the frequency counts vs unique classes.

## How to use

Run the script with your Python interpreter, and add the CSV data file's name
as command-line argument.

### Example

```
  python3 klassen_stats.py example.csv
```

There are some sample input files located in the `csv/` directory to get started.

## Requirements

The script requires Python3 with the [NumPy package](https://numpy.org/ "NumPy").
We need the `matplotlib.pyplot` module for the visualization, and the `csv`
module takes care of reading CSV files.

## License

The script is released under the GNU General Public License (GPL) Version 2.
See the file LICENSE for details.

Created by Akos Bazso, Version 2020.05
