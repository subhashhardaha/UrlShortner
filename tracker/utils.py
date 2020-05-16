import string
import random


def code_generator(size=6, char=string.ascii_letters + string.digits):
    return ''.join(random.choice(char) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)

    Klass = instance.__class__
    qs_exits = Klass.obects.filter(shortcode=new_code).exists()
    if qs_exits:
        return create_shortcode(size=size)

    return new_code
