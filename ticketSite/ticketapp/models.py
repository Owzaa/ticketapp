from collections import UserList
from django.contrib import timezone
from multiprocessing import context
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import lat, long
import uuid
"""""" """""" """""" """""" """""" """""" """"""
# Database Model
# User => ticket(); Model
# Generating ticket Model per User{id}.
"""""" """""" """""" """""" """""" """""" """"""


#  Initialize ticket function:
def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]  #generating unique ticket id


# Defining the Person Model
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# Defining our Database Model Class
class Ticket(models.Model):

    # Data Model for Categories[Sales, IT, Accounts]
    class Meta:
        Categories = [
            {
                'Sales': "Sales"
            },
            {
                'Accounts': "Accounts"
            },
            {
                'IT': "IT"
            },
        ]

# Status Query Selection_List

    class Meta:
        Status_Query = [
            {
                'Newly logged': 'Newly Logged'
            },
            {
                'In Progress': 'In Progress'
            },
            {
                'resolved': 'Resolved'
            },
        ]

# Support System Data Mmodel & encapsulation of Person Object...

    title = models.CharField(max_length=255)
    user = models.ForeignKey(Person=User, on_delete=models.CASCADE)
    gps_cord = models.GeometryField(lat, long)
    e_mail = models.EmailField()
    content = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    date_logged = models.DateTimeField(auto_now=True)
    Status = models.ForeignKey('Status_Query', on_delete=models.CASCADE)
    modified = models.ForeignKey('Status', on_delete=models.CASCADE)

    # return End-user Title and ticket_id
    def __str__(self):
        return "{} = {}".format(self.title, self.ticket_id)

# Save the ticket created by our User

    def save(self, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()
        super(Self).save(**kwargs)


# Ticket log Order class by recent ticket date logged with our refference => Person Looged the Ticket
class Order(models.Model):

    class Meta:
        ordering = [
            [UserList],
            [{
                'first_name',
                'last_name',
                'date_logged',
                'Status',
            }],
        ]


# Pagination Status_Query and pagination List === 10
class Status(models.Model):
    model = 'Status'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context['now'] = timezone.now()
        return context(self.Status, **kwargs)


# Defining Category Model and Choice encapsulation
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    # Returning Category Name
    def __str__(self):
        return self.name


# Defining our GPS Model & merging it with gps_cord Model
