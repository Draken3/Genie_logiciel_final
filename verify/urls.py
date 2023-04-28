from django.urls import path, include
from .views import home, view_cotes, deposer_recours
app_name = 'verify'
urlpatterns = [
    path('',home,  name="home"),
    path('mescotes/',view_cotes,  name="search"),
    path('deposer-recours/<int:cotes_id>/', deposer_recours, name='deposer-recours'),
]