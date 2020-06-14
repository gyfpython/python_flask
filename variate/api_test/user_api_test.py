import requests


def add_user():
    url = 'http://127.0.0.1:8080/user_manage_opt/add_user'
    data = {'username': '123', 'account': '123', 'email': '123', 'password': '123123123', 'role': '1'}
    r = requests.post(url, data)
    print(r)
    print(r.text)


add_user()
