from rest_framework import serializers
from django.contrib.auth.models import User
from ticketSite.ticketapp.models import Category, Ticket
"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
                MY DATABASE MODEL SETUP USING SERIALIZERS TO DEFINE OUR
                
                    API DATA MODEL REPRESENTATION

""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


# This Serializer defines the User API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email',
                  'is_staff')


# This Tickecket Serializer defines the API representation.
class TicketSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'ticket_id', 'user', 'content', 'category',
                  'date_logged', 'modified')


# This Category Serializer defines the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        field = ('id', 'name', 'slug')
