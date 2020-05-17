import string
import random


def code_generator(size=6, char=string.ascii_letters + string.digits):
    return ''.join(random.choice(char) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)

    Klass = instance.__class__
    qs_exits = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exits:
        return create_shortcode(size=size)

    return new_code


def ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
