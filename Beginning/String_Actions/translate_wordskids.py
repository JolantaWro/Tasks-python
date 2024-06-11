"""
Rule 1
If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
For example:
"apple" -> "appleay" (starts with vowel)
"xray" -> "xrayay" (starts with "xr")
"yttria" -> "yttriaay" (starts with "yt")


Rule 2
If a word begins with a one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.
For example:
"pig" -> "igp" -> "igpay" (starts with single consonant)
"chair" -> "airch" -> "airchay" (starts with multiple consonants)
"thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)

Rule 3
If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
For example:
"quick" -> "ickqu" -> "ay" (starts with "qu", no preceding consonants)
"square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")

Rule 4
If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.
Some examples:
"my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
"rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")
"""


def translate(text):
    text = text.lower()
    list_text = text.split()
    vowels = ["a", "e", "i", "o", "u", "xr", "yt"]
    consonant = ["ch", "thr"]
    consonants = list("bcdfghjklmnpqrstvwxyz")
    if text[0] in vowels or text[:2] in vowels:
        return text + "ay"
    elif text[0] in vowels:
        return text[1:] + text[0] + "ay"
    elif text[:2] in consonant:
        return text[2:] + text[0:2] + "ay"
    elif text[:3] in consonant:
        return text[3:] + text[0:3] + "ay"
    
# print(translate("Apple"))
# print(translate("xray"))
# print(translate("yttria"))
# print(translate("pig"))
# print(translate("chair"))
# print(translate("thrush"))
