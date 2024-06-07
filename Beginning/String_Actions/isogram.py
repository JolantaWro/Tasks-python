def is_isogram(sentence):

    sentence = sentence.lower()

    words_set = {char for char in sentence if char.isalpha()}

    words_list = [char for char in sentence if char.isalpha()]

    return len(words_list) == len(words_set)

print(is_isogram("Emily Jung Schwartzkopf"))
