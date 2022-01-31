from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from ticketSite.ticketapp.serializers import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from django.views.decorators.debug import sensitive_variables
from .models import Ticket, Category


# ViewSet define Users view.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# ViewSet define Ticket view behavior.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# Category View()
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Defining User Personal Details for logged ticket
@sensitive_variables('user', 'password')
def process_info(user, first_name, last_name, e_mail, date_logged,
                 status_query, password):
    user = user.objects.all()
    first_name = first_name.objects.all()
    last_name = last_name.objects.all()
    e_mail = e_mail.objects.all()
    date_logged = date_logged.objects.all()
    status_query = status_query.objects.all()
    password = password.object.all()
