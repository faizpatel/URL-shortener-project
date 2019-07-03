import random
import string
from django.conf import settings

SHORTCODE_MIN= getattr(settings, 'SHORTCODE_MIN', 6)

def code(size=6, chars=(string.ascii_lowercase + string.digits)):
    '''new=''
    return ''.join(random.choice(chars) for _ in range(size))
    new+=random.choice(chars)
    return new'''
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance,size=6):
    new=code(size=size)
    Klass=instance.__class__
    qs_exists= Klass.objects.filter(shortcode=new).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new
