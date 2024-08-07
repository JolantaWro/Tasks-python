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
    

print(translate("apple"))
print(translate("ear"))
print(translate("igloo"))
print(translate("object"))
print(translate("under"))
print(translate("equal"))
# print(translate("pig")) fix it!
# print(translate("koala"))
print(translate("xenon"))
