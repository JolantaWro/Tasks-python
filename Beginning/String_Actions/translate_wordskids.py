def translate(text):
    text = text.lower()
    vowels = ["a", "e", "i", "o", "u", "xr", "yt"]
    if text[0] in vowels or text[:2] in vowels:
        return text + "ay"

    
print(translate("Apple"))
print(translate("xray"))
print(translate("yttria"))

