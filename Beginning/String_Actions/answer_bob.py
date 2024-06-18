"""
Function for answers Bob. Bob only ever answers one of five things:
    1. "Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
    2. "Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
    3. "Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
    4. "Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.  
    5. "Whatever." This is what he answers to anything else.
"""


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

