import string
import random
char= string.ascii_letters+string.digits
def passowrd(length):
    x1= "".join(random.choice(char) for i in range(length))
    return x1
    
c=passowrd(7)
print(c)