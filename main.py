import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
# columns: letter, code
nato_dict = {
    row.letter: row.code for (index, row) in nato_df.iterrows()
}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
phonetic_code_list = [nato_dict[letter] for letter in user_input]
print(phonetic_code_list)
