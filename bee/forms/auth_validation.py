from bee.models import UserBee
from django.utils.html import simple_email_re
from django.core.exceptions import ObjectDoesNotExist
from hashlib import sha512
from django.template import loader, Context
from bee.tasks.auth_tasks import activation_mail_sender
from HoneyBeeHive.settings import SECRET_KEY, CURRENT_HOST


def send_activation_mail(user):
    code = sha512("%s%s" % (SECRET_KEY, user.email)).hexdigest()
    url = CURRENT_HOST + "/activate_email/?email=%s&code=%s" % (user.email, code)
    print(url)
    try:
        activation_mail_sender.delay(user.email)
    except Exception as e:
        print e


def activate_user(email, code):
    user = UserBee.objects.get(email=email)
    print code
    print sha512("%s%s" % (SECRET_KEY, user.email)).hexdigest()
    if code == sha512("%s%s" % (SECRET_KEY, user.email)).hexdigest():
        user.email_active = True
        user.is_active = True
        user.save()
        return True
    else:
        return False


def is_valid_email(email):
    if simple_email_re.match(email):
        try:
            UserBee.objects.get(email=email)
            return False
        except ObjectDoesNotExist:
            return True
    return False
