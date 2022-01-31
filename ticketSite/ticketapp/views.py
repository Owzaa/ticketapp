from django.shortcuts import render
from django.views.decorators.debug import sensitive_variables
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
