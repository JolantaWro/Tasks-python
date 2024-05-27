def get_data():
    user_answer = input("Enter number: ")
    return take_return_type(user_answer)

def take_return_type(user_info):
    result = int(user_info)
    return type(result).__name__


get_data()