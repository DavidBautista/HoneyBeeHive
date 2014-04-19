from bee.models import UserBee
from django.utils.html import simple_email_re
from django.core.exceptions import ObjectDoesNotExist
from hashlib import sha512
from django.template import loader, Context
from bee.tasks.auth_tasks import mail_sender
from HoneyBeeHive.settings import SECRET_KEY, CURRENT_HOST


def send_activation_mail(user):
    code = sha512("%s%s" % (SECRET_KEY, user.email)).hexdigest()
    url = "http://%s/activate_email/?email=%s&code=%s" % (CURRENT_HOST, user.email,  code)
    print(url)
    template = loader.get_template('templates/bee/auth/e_activation.html')
    context = Context({
        'email': user.email,
        'url': url,
    })
    try:
        mail_sender.delay('Bienvenido a HoneyBeeHive: Activa tu cuenta', template.render(context), [user.email])
    except:
        print "something went wrong in send_mail"


def activate_user(email, code):
    user = UserBee.objects.get(email=email)
    print code
    print sha512("%s%s" % (SECRET_KEY, user.email)).hexdigest()
    if code == sha512("%s%s" % (SECRET_KEY, user.email)).hexdigest():
        print "se activaaa"
        user.email_active = True
        user.is_active = True
        user.save()
        return True
    else:
        print "no se activaa"
        return False


def is_valid_email(email):
    if simple_email_re.match(email):
        try:
            UserBee.objects.get(email=email)
            return False
        except ObjectDoesNotExist:
            return True
    return False
