def check_username_valid(username: str):
    invalid_string = ['=', '\'', '\"', '!', ';', "%"]
    for string in invalid_string:
        if string in username:
            return False
    return True
