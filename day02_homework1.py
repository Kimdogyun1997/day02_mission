#1

import random as r
import os
path=os.chdir('../')
print(path)

secret = r.randint(1,10)
print(secret)
guess = r.randint(1,10)
print(guess)
if guess < secret:
    print('too low')
elif guess > secret:
    print('too high')
else:
    print('just right')








