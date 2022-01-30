from django.db import models
from django.contrib.auth.models impoprt User
import uuid
import django.contrib import 
from django.contrib.gis.db import models

""""""""""""""""""""""""""""""""""""""""""
# Database Model
# User => ticket(); Model
# Generating ticket Model per User{id}.

""""""""""""""""""""""""""""""""""""""""""
#  Initialize ticket function:
def generate_ticket_id();
    return str(uuid.uuid4()).split("-")[-1] #generating unique ticket id


# Defining our Database Model Class
class Ticket(models.Model):

# Data Model for Categories
    class Meta:
        Categories = [
         {'Sales': "sales"},
         {'Accounts': "accounts"},
         {'IT': "it"},      
        ] 

# Status Query Selection_List    
    class Meta:
        Status_Query = [  
           {'Newly logged': 'Newly Logged'},
           {'In Progress': 'In Progress'},
           {'resolved': 'resolved'},        
        ]           


# Support System Data Mmodel  
    title =models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gps_cord = models.GeometryField(lat,long)
    e_mail = models.EmailField()
    content = models.TextField()
    category = models.ForeignKey("Categories", on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=255, blank=True)
    date_logged = models.DateTimeField(auto_now=True)
    status =models.ForeignKey("Status_Query", on_delete=models.CASCADE)  
    modified = models.ForeignKey("Status",on_delete=models.CASCADE)


# return End-user Title and ticket_id
    def __str__(self):
    return"{} = {}".format(self.title,self.ticket_id)

# Save the ticket created by our User
    def save (self, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_ticket_id()
                super(Ticket, self).save(*args, **kwargs)



# Ticket log Order class by recent ticket date logged with our refference => Person Looged the Ticket
class Order(models.Model):
    class Meta:
    ordering = [
           {
           'User'
           },
        {
            'first_name',
            'last_name',
            'date_logged',
            'Status',
        }
    ]




# Pagination Status_Query and pagination List === 10
class Status(models.Model):
    model = status
    paginate_by = 10

    def get_context_data(self,**kwargs)
    context['now'] = timezone.now()
    return context

# Defining Category Model and Choice encapsulation
class Category (models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
    return self.name

# Defining our GPS Model & merging it with gps_cord Model 
class Gps_Details (models.Model):
    model = gps_cord
    slug =models.SlugField()

    def get_context_data(self,**kwargs):
        return self.location


    





