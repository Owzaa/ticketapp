from multiprocessing import context
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid
"""""" """""" """""" """""" """""" """""" """"""
# Author: Olwethu Theo Nyondo
# Database Model
# User => ticket(); Model
# Generating ticket Model per User{id}.
"""""" """""" """""" """""" """""" """""" """"""


#  Initialize ticket function:
def generate_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]  #generating unique ticket id


# Defining our Database Model Class
class Ticket(models.Model):
    # Choices Model for Categories[Sales, IT, Accounts]
    CATEGORY_CHOICES = (
        ('SL', "SALES"),
        ('ACTS', "ACCOUNTS"),
        ('IT', "INFORMATION TECHNOLOGY"),
    )

    # Status Query Selection_List

    STATUS_QUERY = (
        ('NL', 'NEWLY LOGGED'),
        ('IP', 'IN PROGRESS'),
        ('RS', 'RESOLVED'),
    )

    # Ticket Model Fields
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    e_mail = models.EmailField()
    content = models.TextField()
    category = models.ForeignKey("Category",
                                 choices=CATEGORY_CHOICES,
                                 max_length=None,
                                 on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    date_logged = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    status = models.ForeignKey(
        "Status",
        max_length=None,
        choices=STATUS_QUERY,
        on_delete=models.CASCADE,
    )

    # return End-user Title and ticket_id
    def __str__(self):
        return "{} = {}".format(self.title, self.ticket_id)

# Save the ticket created by our User

    def save(self, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()
        super(self).save(**kwargs)

# Pagination Status_Query and pagination List === 10

    class Status(models.Model):
        model = "Status"
        paginate_by = 10

    def get_context_data(self, **kwargs):
        context['now'] = timezone.now()
        return context(self.Status, **kwargs)
# Ticket log Order class by recent ticket date logged with our refference => Person Looged the Ticket

    class Order(models.Model):

        class Meta:
            ordering = [
                [User],
                [{
                    'first_name',
                    'last_name',
                    'date_logged',
                    'Status',
                }],
            ]


# Defining Category Model and Choice encapsulation
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name


# Defining our GPS Model & merging it with gps_cord Model
class Gps_Cord(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name