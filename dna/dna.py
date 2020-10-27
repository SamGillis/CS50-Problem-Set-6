import sys

## open the CSV file and DNA sequence
    ##first row has name as the first column and the
        ##csv reader and DictReader
        ##sys.argv for command-line arguments
        #once you've opened a text file f using open(filename), you can read its contents using f.read()
    ##remaining row corresponds to a person
##for each STR compute longest run of consecutive repeats in the DNA sequence
    ##for each position in the sequence: compute how many times the STR repeats starting at that position
        ##len(s) in Python will get you the length
        ##slicing
    ##for each position keep checking successive substrings until the STR repeats no longer
##compare the STR counts against each row in the CSV file
    ##save STR counts in some data structure
    ##for each row in the data, check if each STR count matches. If so, print out the person's name.
        ##int(x)
        ##need to checky every column other than the first column