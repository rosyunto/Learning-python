import json

#username = input('what\'s your name: ')
filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
    
except FileNotFoundError:
    username = input('what\'s your name: ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print('We will remember you when you come back! ' + username + '!')
else:
    print('Welcome back ' + uesrname + '!')
