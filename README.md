Klassen
=======

A Python utility to generate statistics for assigned CPC/IPC classes.

Description
-----------

This script provides functions to read a matrix of CPC (IPC) classes from a CSV
file, to generate statistics and frequency counts for all unique elements, and
to generate a bar chart plot for the frequency counts vs unique classes.

How to use
----------

Run the script with your Python interpreter, and add the name of your CSV data
file as command-line argument.

## Example

```
  python3 klassen_stats.py example.csv
```

There is a sample input file located in the `data/` directory to get started.

Requirements
------------

The script requires Python3 with the [NumPy package](https://numpy.org/ "NumPy").

License
-------

The script is released under the GNU General Public License (GPL) Version 2.
See the file LICENSE for details.

Created by Akos Bazso, Version 2020.05
