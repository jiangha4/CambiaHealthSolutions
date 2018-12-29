# -----------------------------------------------------------------------------
# Cambia Health Solutions Assignment
# Author: David Jiang
# Email: davidjiang.haohan@gmail.com
# -----------------------------------------------------------------------------

import argparse
import csv

# Command line argument parser
def argumentParser():
    parser = argparse.ArgumentParser(description='Takes in CSV file and returns a CSV')
    parser.add_argument('-f', '--file', type=str, default='input.csv',
                        help='The CSV file to sort')
    return parser.parse_args()

# Open input CSV file and format
def getCsvInput(fileName):
    '''
        Input: String - Name of the CSV file to be opened
        Output: List - list of all CSV elements
    '''
    with open(fileName, 'r') as inputFile:
        reader = csv.reader(inputFile)
        return list(reader)[0]

def main(args):
    csvInput = getCsvInput(args.file)
    print(csvInput)

if __name__=='__main__':
    args = argumentParser()
    main(args)
