import string
import random

def code_generator(size=6,char=string.ascii_letters+string.digits):
    return ''.join(random.choice(char) for _ in range(size))
