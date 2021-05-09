from django.conf.urls import url 
from Tweets import views 
from django.urls import path
from .views import MarkersMapView, StoreTweetsGoats, HeatMapView
 
urlpatterns = [ 
    path("api/map/", MarkersMapView.as_view(), name='mapa'),
    path("api/weLove", StoreTweetsGoats.as_view(), name='welove'),
    path("api/heatmap", HeatMapView.as_view(), name='heat')
   
]