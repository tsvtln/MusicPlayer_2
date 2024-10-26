from django.urls import path
from profiles.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]
