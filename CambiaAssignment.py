# -----------------------------------------------------------------------------
# Cambia Health Solutions Assignment
# Author: David Jiang
# Email: davidjiang.haohan@gmail.com
# -----------------------------------------------------------------------------

import argparse

def argumentParser():
    parser = argparse.ArgumentParser(description='Takes in CSV file and returns a CSV')
    parser.add_argument('-f', '--file', type=str, default='input.csv',
                        help='The CSV file to sort')
    return parser.parse_args()

if __name__=='__main__':
    args = argumentParser()
    print(args)
