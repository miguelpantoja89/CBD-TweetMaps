from django.conf.urls import url 
from Tweets import views 
from django.urls import path
from .views import MarkersMapView, StoreTweetsGoats, search_hashtag, StatisticsView
 
urlpatterns = [ 
    path("api/map/", MarkersMapView.as_view(), name='mapa'),
    path("api/weLove", StoreTweetsGoats.as_view(), name='welove'),
    path("api/search", search_hashtag, name='searching'),
    path("api/stats", StatisticsView.as_view(), name='stats'),
   
]