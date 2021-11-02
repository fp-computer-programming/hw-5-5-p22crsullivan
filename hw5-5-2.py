# Author: CRS 11/02/21
word = input("Please enter a six letter word.")
letter_1 = word[0]
letter_2 = word[1]
letter_3 = word[2]
letter_4 = word[3]
letter_5 = word[4]
letter_6 = word[5]
dash = "-"
print(dash.join(letter_1 + letter_3 + letter_5))
print(dash.join(letter_2 + letter_4 + letter_6))