


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id','user','title', 'ticket_id','status', 
                'content', 'category','date_logged',
                'modified')