from cs50 import get_int
import math

i = 0
d = 0
card = get_int("Number: ")
while not card > 0:
    card = get_int("Number: ")
# get final number
# this makes sure I can check the card number later and stores card
t = card;
# loop for adding up the digits in the card number
while t > 0:
    i = t % 10
    t = math.floor(t / 10)
    d = d + i
    i = t % 10
    t = math.floor(t / 10)
    #adds the digits, not the products
    p = 2 * i
    if p > 9:
        p = p - 9
    d = d + p
#calculates the ones place of the above equation
checksum = d % 10

# checks the card checksum or says invalid
if checksum == 0:
    #checks the type of card
    #American Express
    # checks if the card is 15 digits
    Amexpress = card % 100000000000000
    if card > 339999999999999 and card < 380000000000000:
        #gets the 14th digit in the card
        if math.floor(Amexpress / 10000000000000) == 4 or math.floor(Amexpress / 10000000000000) == 7:
            #if all true, prints AMEX
            print("AMEX")
        else:
            print("INVALID")
    #Visa
    #checks if the card starts with 4 and is 13 or 16 digits
    elif ((card > 3999999999999 and card < 5000000000000) or (card > 3999999999999999 and card < 5000000000000000)):
        #outputs Visa
        print("VISA")
    #Mastercard
    #checks if the card is 16 digits and starts 51 - 55
    elif card > 5099999999999999 and card < 5600000000000000:
        print("MASTERCARD");
    else:
        #if doesn't meet any of the criteria prints invalid
        print("INVALID");
else:
    #if doesn't meet checksum, prints invalid
    print("INVALID");