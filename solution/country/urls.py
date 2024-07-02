from django.urls import path

from country.views import *

app_name = "country"
urlpatterns = [
    path("", CountryListView.as_view()),
    path("<str:alpha2>/", CountryView.as_view()),
]