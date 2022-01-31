from unittest.util import _MAX_LENGTH
from django.forms import IntegerField
from serializers import Ticket
from ticketSite.ticketapp import serializers


class TicketSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ticket_id = serializers.CharField(_MAX_LENGTH=200)
    title = serializers.CharField(_MAX_LENGTH=200)
    content = serializers.TextField()
