from __future__ import absolute_import
from django.core.mail import send_mail
from HoneyBeeHive.settings import EMAIL_HOST_USER
from celery import shared_task
from hashlib import sha512
from django.template import loader, Context
from django.utils.translation import ugettext_lazy as _
from HoneyBeeHive.settings import SECRET_KEY, CURRENT_HOST


@shared_task
def activation_mail_sender(email):
    try:
        code = sha512("%s%s" % (SECRET_KEY, email)).hexdigest()
        url = CURRENT_HOST + "/activate_email/?email=%s&code=%s" % (email, code)
        print(url)
        template = loader.get_template('templates/bee/auth/e_activation.html')
        context = Context({
            'email': email,
            'url': url,
        })
        send_mail(_("Welcome to HoneyBeeHive: Activate your account!"), template.render(context), EMAIL_HOST_USER, [email])
    except Exception as e:
        print "something went wrong in send_mail"
        print e
