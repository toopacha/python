
user_id = input('id?')
user_pwd = input('passwaord?')


'''
if user_pwd == '111111' :
      print('Hello master')
else:
    print('Who are you?')
'''

'''
if user_id == 'toopacha':
    if user_pwd == '111111' :
        print('Hello master')
    else:
        print('wrong passwaord')
else:
    print('Who are you?')
'''

if user_id == 'toopacha' and user_pwd == '111111':
        print('Hello toopacha')
elif user_id == 'hoolaboy' and user_pwd == '111111':
        print('Hello hoolaboy')
else:
        print('wrong passwaord or id')
