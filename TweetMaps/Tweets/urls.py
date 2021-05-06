from django.conf.urls import url 
from Tweets import views 
from django.urls import path
from .views import MarkersMapView
 
urlpatterns = [ 
    path("api/map/", MarkersMapView.as_view()),
   
]