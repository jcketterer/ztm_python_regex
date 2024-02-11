# 8 characters long
# contain any letters, numbers, $%#@

import re

password = input('Please enter your selected password: ')

if re.fullmatch(r"^([a-zA-Z0-9@#$%]){8,}\d", password):
    print('match')
else:
    print('no match')
    
    