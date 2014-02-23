from project_management.models import UserWorker
from django.utils.html import simple_email_re
from django.core.exceptions import ObjectDoesNotExist
from hashlib import sha512
from django.template import loader, Context
from project_management.tasks.auth_tasks import mail_sender


def send_activation_mail(user):
    code = sha512("%s%s" % (user.username, user.email)).hexdigest()
    url = "http://127.0.0.1:8000/activate_email/?username=%s&code=%s" % (user.username,  code)
    print(url)
    template = loader.get_template('templates/project_management/auth/activate_email.html')
    context = Context({
        'username': user.username,
        'url': url,
    })
    try:
        mail_sender.delay('Bienvenido a Caribbean Tradders: Activa tu cuenta', template.render(context), [user.email])
    except:
        print "something went wrong in send_mail"


def activate_user(username, code):
    user = UserWorker.objects.get(username=username)
    if code == sha512("%s%s" % (username, user.email)).hexdigest():
        user.email_active = True
        user.is_active = True
        user.save()
        return True
    else:
        return False


def is_valid_email(email):
    if simple_email_re.match(email):
        try:
            UserWorker.objects.get(email=email)
            return False
        except ObjectDoesNotExist:
            return True
    return False
