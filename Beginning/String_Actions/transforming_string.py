"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    prefix_word = "un"
    new_word = prefix_word + word
    return new_word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    new_list = []
    index_word = vocab_words[0]

    for index, word in enumerate(vocab_words):
        if index > 0:
            new_list.append(index_word + word)
        
    fix_list = [vocab_words[0]] + new_list
    sentence = " :: ".join(fix_list)
    return sentence


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    new_word = ""

    if word.endswith("ness"):
        end_word = word[-5]
        if end_word == "i":
            new_word  = word[:-5]+ "y"
        else:
            new_word = word[:-4]
    return new_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    user_sentence = ""
    new_verb = ""

    if sentence.endswith("."):
        user_sentence = sentence[:-1]

    list_word = user_sentence.split(" ")
    new_verb = list_word[index]

    return new_verb + "en"
