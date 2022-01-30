from django.shortcuts import render
from django.views.decorators.debug import sensitive_variables
from django.core.mail send_email




# Defining User Personal Details for logged ticket
@sensitive_variables ('user','password', 'username')
    def process_info(user):
    username = user.username
    first_name = user.first_name
    last_name = user.last_name
    e_mail = user.e_mail
    date_logged = user.date_logged
    status_query = user.status
    password = user.password

# Sending e_mail back to users e_mail with ticket_logged()
    def send_email(subject,message,from_email,auth_user,auth_password,connection):
        subject = user.Ticket
        message = user.stringfy(content)
       
 
