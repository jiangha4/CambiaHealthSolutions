#### Why are these tests helpful?

I have written five test cases for my script. 2 are for the input function. 2 are for
the output function. 1 is for the sorting itself.

The 2 input function tests:
  1. Tests that the given string name from the command line is a valid string that
     points to a valid CSV file.
  2. Tests that the CSV file is valid, can be opened, and read, and that it returns
     a valid CSV reader object.

The 2 output function tests:
  1. Tests that a list of lists to be able to write into a CSV format.
  2. Tests that converting a list to a list of lists functions correctly.

The sorting function tests:
  1. That if all items in the CSV file are utf-8 valid, then I should
     be able to sort on the lower case letter for every item.

These tests are helpful in the future because they insure that the input types are
never changed, that we always get a valid CSV file and that the data inside is valid. This
ensures that we will always be able to open, read and extract all the CSV data. The
sorting function test ensures that we can always convert every item to lower case to be
able to sort properly. The 2 output tests insure that when we try and write to a CSV file,
we are always converting to the right format to be written in a valid CSV format.
