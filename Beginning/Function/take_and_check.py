def get_data():
    user_answer = input("Enter word: ")
    return take_return_type(user_answer)

def take_return_type(user_info):
    return type(user_info).__name__
