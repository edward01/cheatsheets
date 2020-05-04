import getpass
from healthe.models.admin import Admin


def create_account(username, password):
    try:
        Admin.create({
            'username': username,
            'password': password,
        })
        print('--> Done creating "{}" account'.format(username))
    except Exception as e:
        print('ERROR:', e)


if __name__ == "__main__":
    username = input('Enter username: ')
    try:
        p = getpass.getpass()
    except Exception as error:
        print('ERROR:', error)
    else:
        create_account(username, p)
