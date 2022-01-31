from ticketSite.ticketapp import serializers
from ticketSite.ticketapp.models import Category


#Ticket Serializer Model
class TicketSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="ID", read_only=True)
    ticket_id = serializers.CharField(_MAX_LENGTH=255)
    title = serializers.CharField(_MAX_LENGTH=200)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())
    user = serializers.PrimaryKeyRelatedField(
        queryset=serializers.UserSerializer.objects.all())
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)
