def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    user_sentence = set(sentence.lower())
    words =  user_sentence.intersection(alphabet)
    if len(words) == 26:
        return True
    return False
