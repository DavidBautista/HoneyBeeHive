from __future__ import absolute_import
from django.core.mail import send_mail
from HoneyBeeHive.settings import EMAIL_HOST_USER
from celery import shared_task


@shared_task
def mail_sender(subject, message, dest):
    try:
        send_mail(subject, message, EMAIL_HOST_USER, dest) #TODO el html_message esta en django/dev
    except:
        print "something went wrong in send_mail"
        raise