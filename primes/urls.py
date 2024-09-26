from django.urls import path
from . import views

urlpatterns = [
    path("", views.input_page, name="input_page"),
    path("primes/", views.output_page, name="output_page"),
]
