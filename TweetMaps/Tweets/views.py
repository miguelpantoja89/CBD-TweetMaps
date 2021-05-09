from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Tweet
import tweepy
import datetime
from django.conf import settings
# Create your views here.
class MarkersMapView(TemplateView):
    template_name = "map.html"
    def get(self, request):
        marker = Tweet.objects.all()
        return render(request, self.template_name, {'data':'hola','patata':marker})

class HeatMapView(TemplateView):
    template_name = "heatmap.html"
    def get(self, request):
        marker = Tweet.objects.all()
        return render(request, self.template_name, {'data':'hola','patata':marker})


class StoreTweetsGoats(TemplateView):
    template_name = "map.html"
    def get(self,request):
        Tweet.objects.all().delete()
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        today = datetime.date.today()
        yesterday= today - datetime.timedelta(days=1)
        tweets_list = tweepy.Cursor(api.search, q="#WeLoveGoats -filter:retweets",tweet_mode='extended').items()
        for tweet in tweets_list:
            text = tweet._json["full_text"]
            created_at =  tweet.created_at.strftime('%m/%d/%Y %H:%M')
            if(tweet.place is None):
                coordinates = [[['-5.97317','37.38283']]]
            else:
                coordinates = tweet.place.bounding_box.coordinates
            Tweet.objects.create(text='Prueba', created_at=created_at, titulo=text, latitud=coordinates[0][0][1], longitud=coordinates[0][0][0])
       

        # marker = Tweet.objects.all()
        # return render(request, self.template_name, {'data':'hola','patata':marker})
        return redirect("/tweets/api/map")