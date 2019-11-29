from django.conf.urls import url

from .views import home, test

urlpatterns = [
    url(r'home$', home), 
    url(r'test$', test)
]