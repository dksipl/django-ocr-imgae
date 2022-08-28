from django.urls import path
from app1 import views as app1_views

urlpatterns = [
    path('', app1_views.home, name = 'app1-home'),
    path('display/', app1_views.display, name = 'app1-display'),
]
