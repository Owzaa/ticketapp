from dataclasses import fields
from django.contrib import admin
from django.forms import fields_for_model
from .models import Ticket, Order, Status, Category, Person


# Register your models here.
class Person(admin.ModelAdmin):
    fields = ('first_name', 'last_name')


class Ticket(admin.ModelAdmin):
    fields = ('user', 'title', 'Status', 'tickeck_id', 'date_logged', 'e_mail')


class Order(admin.ModelAdmin):
    fields_for_model = ('first_name', 'last_name', 'date_logged', 'Status')


class Status(admin.ModelAdmin):
    fields = ('Status')


class Category(admin.ModelAdmin):
    fields = ('name')
