import pandas
is_on = True

data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        is_on = False
    except KeyError:
        print("Only letters for the game please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()