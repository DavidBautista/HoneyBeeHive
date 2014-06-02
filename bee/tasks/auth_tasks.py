from __future__ import absolute_import
from django.core.mail import send_mail
from HoneyBeeHive.settings import EMAIL_HOST_USER
from celery import shared_task
from hashlib import sha512
from django.template import loader, Context
from django.utils.translation import ugettext as _
from HoneyBeeHive.settings import SECRET_KEY, CURRENT_HOST, PRETTY_CURRENT_HOST, STATIC_URL
from django.utils.translation import activate


@shared_task
def activation_mail_sender(email, lang_code):
    try:
        code = sha512("%s%s" % (SECRET_KEY, email)).hexdigest()
        url = "/activate_email/?email=%s&code=%s" % (email, code)
        print(url)
        activate(lang_code)
        template_text = loader.get_template('templates/bee/auth/e_activation.txt')
        template_html = loader.get_template('templates/bee/auth/e_activation.html')
        context = Context({
            'email': email,
            'url': url,
            'CURRENT_HOST': CURRENT_HOST,
            'PRETTY_CURRENT_HOST': PRETTY_CURRENT_HOST,
            'STATIC_URL': STATIC_URL
        })
        text_message = template_text.render(context)
        html_message = template_html.render(context)
        print html_message
        send_mail(_("Activate your HoneyBeeHive account"), text_message, EMAIL_HOST_USER, [email],
                  html_message=html_message)
    except Exception as e:
        print "something went wrong in send_mail"
        print e
        raise e
