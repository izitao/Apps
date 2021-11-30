import pandas

#CREATING THE LETTER-CODE DICTIONARY
file = "nato_phonetic_alphabet.csv"
nato_phonetic_input = pandas.read_csv(file)

nato_phonetic_dict = {str(row.letter):str(row.code) for (index, row) in nato_phonetic_input.iterrows()}
print(nato_phonetic_dict)


#USING THE DICTIONARY TO SPELL EACH LETTER WITH IT'S CODE

def generate_phonetic():

    user_input = input('Write a word: ').upper()
    try:
        phonetic_output = {letter:nato_phonetic_dict[letter] for letter in user_input}
        #classical way
        '''nato_phonetic_dict = {}
        for (index, row) in nato_phonetic_input.iterrows():
        nato_phonetic_dict[row.letter]=row.code'''
    except KeyError:
        print("Sorry, only alphabets are allowed as input.")
        generate_phonetic()
    else:
        print(phonetic_output)

generate_phonetic()
