import random
import string
import os


alphabet = string.ascii_letters + string.digits


def app():
    while True:
        i = input(':')
        command = i.split()[0]
        website_name = i.split()[1]
        if command == 'create' or command == 'change':
            output = ''
            # ok you might think im dumb for using 'data/'+website but it ties to use 'data/{website}' but it didn't fucking work so shut up
            with open('data/'+website_name, 'w') as file:
                for i in range(1, 50):
                    output += alphabet[random.randint(1, 59)]
                file.write(output)
        elif command == 'get' and os.path.exists('data/'+website_name):
            with open('data/'+website_name, 'r') as file:
                print('password:', file.read())
    return


if __name__ == '__main__':
    app()
