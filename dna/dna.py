import sys

## open the CSV file and DNA sequence
csv_file = open(sys.argv[1])
csv_file = csv_file.read()
csv_file = csv_file.split('\n')
dna_file = open(sys.argv[2])
dna_file = dna_file.read()

headers = csv_file.pop(0)
dna_sequences = {}
headers = headers.split(',')
csv_file.pop()

##loads in dict from csv file
for row in csv_file:
    row = row.split(',')
    row_dict = {}
    for i in range(len(headers) - 1):
        row_dict[headers[i+ 1]] = row[i + 1]

    dna_sequences[row[0]] = row_dict

dna_compare = {}

##for each STR compute longest run of consecutive repeats in the DNA sequence
    ##for each position in the sequence: compute how many times the STR repeats starting at that position
        ##len(s) in Python will get you the length
        ##slicing
    ##for each position keep checking successive substrings until the STR repeats no longer

for each in headers[1:]:
    longest = 0
    for i in range(len(dna_file) - len(each)):
        if dna_file[i:i+len(each)] == each:
            counter = 1
            y = i + len(each)
            while True:
                if dna_file[y:y+len(each)] == each:
                    counter += 1
                    y += len(each)
                else:
                    break
            if counter > longest:
                longest = counter

    dna_compare[each] = longest

##compare the STR counts against each row in the CSV file
for each in dna_sequences:
    if dna_sequences[each] == dna_compare:
        print(each)
    ##save STR counts in some data structure
    ##for each row in the data, check if each STR count matches. If so, print out the person's name.
        ##int(x)
        ##need to checky every column other than the first column