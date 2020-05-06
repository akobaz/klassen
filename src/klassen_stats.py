#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@file    klassen_stats.py
@author  Bazso Akos
@version 1.0, 16 Feb 2020
         1.1, 25 Feb 2020
         1.2, 30 Apr 2020
         1.3, 06 May 2020
@brief   generate statistics for assigned CPC/IPC classes
@details generate statistics and frequency counts for matrix elements
         input from a CSV file; generate bar chart plot for frequencies
@usage   python3 klassen_stats.py [INPUT FILE]
         or ./klassen_stats.py [INPUT FILE]
@example python3 klassen_stats.py ../data/klassen-test.csv
"""

# import modules
import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

# -----------------------------------------------------------------------------

# global constants
CONST_VERSION_ = "1.3"
CONST_DATE_    = "06 May 2020"

# show verbose debug output ? True | False (default)
DEBUG_stats    = False

# initialize empty input array
arr = []

# -----------------------------------------------------------------------------

# read input from CSV file
def ReadCSVFile(filename):
    """read CSV formatted input from 'filename'"""
    with open(filename, 'r') as fp:
        # TODO FIXME enable selection of delimiter (default: ',')
        rows = csv.reader(fp, delimiter=',')
        # DEBUG
        if DEBUG_stats:
            print( rows )

        # fill array with matrix elements
        for row in rows:
            arr.append(row)
            # DEBUG
            if DEBUG_stats:
                print( row )

# -----------------------------------------------------------------------------

# generate counts and show results
def GetCounts():
    """calculate IPC/CPC class-symbols frequency counts"""

    # extract sub-matrix that contains only CPC/IPC symbols
    # https://docs.scipy.org/doc/numpy/user/basics.indexing.html
    a = np.array(arr)[1::,1::]
    # DEBUG
    if DEBUG_stats:
        print( arr )
        print( a )

    # --- Variante #1 --- NOTE unused
    # https://stackoverflow.com/questions/16330831/
    #import scipy.stats
    #print( scipy.stats.mode(a) )

    # --- Variante #2 ---
    # https://stackoverflow.com/questions/10741346/
    u, c = np.unique(a, return_counts=True)

    # transpose arrays but ignore first line for 'empty' cells
    result = np.asarray((u, c)).T[1:]
    # DEBUG
    if DEBUG_stats:
        # print resulting ndarray
        print( result, type(result), result.shape )
        # print only x-values
        print( result[:,0] )
        # print only y-values
        print( result[:,1] )

    return result

# -----------------------------------------------------------------------------

# generate bar chart plot
def MakePlot(data):
    """create a bar chart with class labels and usage frequency"""

    # select figure size (width, height) in inches
    plt.figure(figsize=(4,12))

    # format x-axis
    x = np.array(data[:,1], np.int32)
    plt.xlabel('Frequency')
    # DEBUG
    if DEBUG_stats:
        print( x )

    # format y-axis
    yticlabels = data[:,0]
    yticvalues = np.arange( len(yticlabels) )
    plt.yticks(yticvalues, yticlabels)
    # DEBUG
    if DEBUG_stats:
        print(yticlabels, yticvalues)

    # prepare plot
    # https://pythonspot.com/matplotlib-bar-chart/
    plt.barh(yticvalues, x, align='center', alpha=0.8)
    # sorted top to bottom
    plt.gca().invert_yaxis()
    plt.title('CPC/IPC class statistics')
    plt.tight_layout()

    # show plot
    plt.show()

    # TODO FIXME save plot to file
    #plt.savefig("klassen_stats.png")

# -----------------------------------------------------------------------------

# show script usage
def Usage(name):
    """print info about script and usage"""
    print(
        "{0} -- generate statistics for assigned CPC/IPC classes\n"
        "(C) Bazso Akos, Version {1} from {2}\n\n"
        "read a matrix from CSV file and generate frequency counts for elements\n\n"
        "Usage:   python3 {0} [INPUT FILE]\n"
        "Example: python3 {0} testfile.csv\n"
        "\n".format(name, CONST_VERSION_, CONST_DATE_)
    )

# -----------------------------------------------------------------------------

# main function
def main():
    """main function"""

    # check command-line arguments
    argc = len( sys.argv )
    if argc > 1:
        # read input file to variable 'arr'
        ReadCSVFile( sys.argv[1] )

        # generate frequency counts
        cnts = GetCounts()
        print( cnts )

        # show diagram with statistics
        MakePlot( cnts )

        # exit indicating success
        sys.exit(0)
    else:
        # show script usage
        Usage( sys.argv[0] )

        # exit with failure
        sys.exit(1)

# -----------------------------------------------------------------------------

# check if script runs stand-alone
if __name__ == "__main__":
    main()
