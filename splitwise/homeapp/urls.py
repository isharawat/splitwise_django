from django.urls import path
from .views import my_home_page


urlpatterns = [
    path('', my_home_page ),
]
