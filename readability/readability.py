from cs50 import get_string
import string

letters = 0
words = 1
other = 0
total = 0
sentences = 0

##gets text from user
t = get_string("Text: ")
#Counts the amount of letters, sentences, and  words in text
for total in range(len(t)):
    if t[total].isalnum():
        letters = letters + 1
    elif t[total].isspace():
        words = words + 1
    elif t[total] == '.' or t[total] == '!' or t[total] == '?':
        sentences = sentences + 1
    else:
        other = (other + 1)
#finds the average of letters per 100 words "L"
L = (letters / words) * 100
#finds the average number of sentences per 100 words "S"
S = (sentences / words) * 100
#Calculates Grade
index = (0.0588 * L) - (0.296 * S) - 15.8
#If statement for printing above grade 16, before grade 1, or grade
if index < 1:
    print("Before Grade 1")
elif index > 1 and index < 16:
    print(f"Grade {round(index)}")
elif index >= 16.5:
    print("Grade 16+")