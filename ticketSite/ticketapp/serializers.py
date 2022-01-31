from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from ticketSite.ticketapp.models import Person
from ticketapp import Ticket, Category, Status
"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
                MY DATABASE MODEL SETUP USING SERIALIZERS TO DEFINE OUR
                
                    API DATA MODEL REPRESENTATION

""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


# This Serializer defines the User API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        {}

    model = [User, Person]
    fields = [('url', 'username', 'first_name', 'last_name', 'email',
               'is_staff')]


# This Serializer defines the API representation.
class TicketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        {}

    model = [Ticket]
    fields = [('id', 'title', 'ticket_id', 'user', 'content', 'category',
               'date_logged', 'status', 'gps_cord')]


# This Serializer defines the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        {}

    model = [Category]
    fields = ('name', 'slug')


# This Serializer defines Status_Queries
class StatusViewSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        {}

    model = [Status]
    fields = [('name', 'slug')]
