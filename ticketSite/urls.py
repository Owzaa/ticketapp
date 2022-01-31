from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ticketSite.ticketapp.views import UserViewSet, TicketViewSet, CategoryViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/tickets', TicketViewSet)
router.register(r'api/category', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))
]