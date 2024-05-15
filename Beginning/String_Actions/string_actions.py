def string_to_lower(x):
    if not isinstance(x, str):
        raise TypeError ("Your value must be string")
    return x.lower()

def string_to_upper(x):
    if not isinstance(x, str):
        raise TypeError ("Your value must be string")
    return x.upper()

text = "Hello world, this is a test. Hello again!"
replacements = {
    "Hello": "Hi",
    "test": "example",
    "again": "once more"
}

def replace_words(text, replacements):
    for old_word, new_word in replacements.items():
        text = text.replace(old_word, new_word)
    return text

modified_text = replace_words(text, replacements)
print(modified_text)




