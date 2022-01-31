from inspect import _Object
from django.shortcuts import render
from django.views.decorators.debug import sensitive_variables
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.db import Ticket, context


# Defining User Personal Details for logged ticket
@sensitive_variables('user', 'password')
def process_info(user, first_name, last_name, e_mail, date_logged,
                 status_query, password):
    {
        user: object.username,
        first_name: object.first_name,
        last_name: object.last_name,
        e_mail: object.e_mail,
        date_logged: object.date_logged,
        status_query: object.status,
        password: object.password,
    }


# Sending e_mail back to users e_mail with ticket_logged()
def send_email(request):
    subject = request.POST.get('subject', {{process_info.status_query}})
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/templates/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
