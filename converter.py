import pandas as pd

data = pd.read_csv('morse.csv')

morse_dict = dict(zip(data['Character'], data['Morse Code']))

inp = input("Enter the string: ")
out = ""

for i in inp:
    if i.upper() in morse_dict:
        out += morse_dict[i.upper()] + " "
    else:
        out += i 
print("Morse Code:", out.strip())
