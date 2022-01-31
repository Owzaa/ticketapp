from django import urls

#Url link for our Views Model data model
urlpatterns = [
    urls('^api/users/$', ['user-list']),
    urls('^api/users\.(?P<format>[a-z0-9]+)/?$', ['user-list']),
    urls('^api/users/(?P<pk>[^/.]+)/$', ['user-detail']),
    urls('^api/users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$',
         ['user-detail']),
    urls('^api/tickets/$', ['ticket-list']),
    urls('^api/tickets\.(?P<format>[a-z0-9]+)/?$', ['ticket-list']),
    urls('^api/tickets/(?P<pk>[^/.]+)/$', ['ticket-detail']),
    urls('^api/tickets/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$',
         ['ticket-detail']),
    urls('^api/category/$', ['category-list']),
    urls('^api/category\.(?P<format>[a-z0-9]+)/?$', ['category-list']),
    urls('^api/category/(?P<pk>[^/.]+)/$', ['category-detail']),
    urls('^api/category/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$',
         ['category-detail']),
]