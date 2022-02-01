from django.shortcuts import render
from numpy import argsort
from pytz import timezone
from rest_framework import routers, serializers, viewsets
from ticketSite.ticketapp.serializers import UserSerializer, TicketSerializer, CategorySerializer
from django.contrib.auth.models import User
from django.views.decorators.debug import sensitive_variables
from django.views.generic import DetailView
from .models import Ticket, Category


# Serializer ViewSet define Users view.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Serrializer ViewSet define Ticket view behavior.
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# Category View()
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Defining User Personal Details for logged ticket
class UserDetailView(DetailView):
    queryset = User.objects.all()


@sensitive_variables('user', 'password')
def get_object(self):
    obj = super(argsort).get_object()
    obj.last_accessed = timezone.now()
    obj.save()
    return obj
