def response(hey_bob):
    answer = ""
    sentence = hey_bob.strip()

    if len(hey_bob.strip()) == 0:
        answer = "Fine. Be that way!" 
    elif sentence.isupper() and sentence.endswith("?"):
        answer = "Calm down, I know what I'm doing!"
    elif sentence.endswith("?"):
        answer = "Sure."
    elif sentence.isupper():
        answer = "Whoa, chill out!" 
    else:
        answer = "Whatever." 
    return answer

print(response("Are you hungry?"))
print(response("WHAT?"))
print(response("Okay if like my  spacebar  quite a bit?   "))
print(response("WHAT"))
print(response("Does this cryogenic chamber make me look fat?"))