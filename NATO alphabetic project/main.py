import pandas

#CREATING THE LETTER-CODE DICTIONARY
file = "nato_phonetic_alphabet.csv"
nato_phonetic_input = pandas.read_csv(file)

nato_phonetic_dict = {str(row.letter):str(row.code) for (index, row) in nato_phonetic_input.iterrows()}
print(nato_phonetic_dict)

'''nato_phonetic_dict = {}
for (index, row) in nato_phonetic_input.iterrows():
    nato_phonetic_dict[row.letter]=row.code''' #classical way

#USING THE DICTIONARY TO SPELL EACH LETTER WITH IT'S CODE

user_input = input('Write a word: ').upper()
phonetic_output = {letter:nato_phonetic_dict[letter] for letter in user_input if letter in nato_phonetic_dict.keys()}
print(phonetic_output)
