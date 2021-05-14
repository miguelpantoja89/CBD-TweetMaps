from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Tweet
import tweepy
import datetime
from django.conf import settings
# Create your views here.
def search_hashtag(request):
    hashtag = request.GET.get('search')
    Tweet.objects.all().delete()
    auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    tweets_list = tweepy.Cursor(api.search, q=hashtag+" -filter:retweets",tweet_mode='extended').items()
    for tweet in tweets_list:
        text = tweet._json["full_text"]
        created_at =  tweet.created_at.strftime('%m/%d/%Y %H:%M')
        if(tweet.place is None):
            coordinates = [[['-5.97317','37.38283']]]
        else:
            coordinates = tweet.place.bounding_box.coordinates
            Tweet.objects.create(text="hola", created_at=created_at, titulo=text, latitud=coordinates[0][0][1], longitud=coordinates[0][0][0])
    return redirect("/tweets/api/map")

class MarkersMapView(TemplateView):
    template_name = "map.html"
    def get(self, request):
        marker = Tweet.objects.all()
        marker2 = Tweet.objects.all()[0:11]
        return render(request, self.template_name, {'data':'hola','patata':marker, 'patata2':marker2})

class StatisticsView(TemplateView):
    template_name="statistics.html"
    

class StoreTweetsGoats(TemplateView):
    template_name = "map.html"
    def get(self,request):
        Tweet.objects.all().delete()
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        today = datetime.date.today()
        yesterday= today - datetime.timedelta(days=1)

        bcp47_dictionary = { 'am':'Amharic', 'de':'German', 'ml':'Malayalam', 'sk':'Slovak','ar' : 
'Arabic', 'el':'Greek','dv': 'Maldivian', 'sl':'Slovenian',
'hy': 'Armenian', 'gu' : 'Gujarati', 'mr': 	'Marathi', 'ckb': 'Kurdish','eu' : 
'Basque', 'ht':'Creole',  'ne': 'Nepali','es':	'Spanish', 'ja':'Japanese','en':'English','tl':'Tagalog','und':'Undefined',
'bn':'Bengali', 'iw':'Hebrew', 'no':'Norwegian', 'sv': 'Swedish', 'bs':'Bosnian', 'hi':'Hindi', 'or':'Oriya', 'tl':'Tagalog', 'bg':'Bulgarian', 
'hi-Latn':'Latinized Hindi', 'pa':'Panjabi', 'ta':'Tamil', 'my':'Burmese', 'hu': 'Hungarian', 'ps': 'Pashto', 'te': 'Telugu', 'hr': 'Croatian',
'is': 'Icelandic', 'fa': 'Persian', 'th': 'Thai', 'ca': 'Caralan', 'in': 'Indonesian', 'pl': 'Polish', 'bo': 'Tibetan', 'cs':'Czech', 'it': 'Italian',
'pt': 'Portuguese', 'zh-TW': 'Traditional Chinese', 'da': 'Danish', 'ro': 'Romanian', 'tr': 'Turkish', 'nl': 'Dutch', 'kn': 'Kannada', 'ru': 'Russian', 
'uk': 'Ukranian', 'km': 'Khmer', 'sr':'Serbian', 'ur':'Urdu', 'et': 'Estonian', 'ko': 'Koraean', 'zh-CN': 'Simplified Chinese', 'ug': 'Uyghur', 
'fi': 'Finnish', 'lo':'Lao', 'sd': 'Sindhi', 'vi': 'Vietnamese', 'fr': 'French', 'lv': 'Latvian', 'si': 'Sinhala', 'cy': 'Welsh', 'ka': 'Georgian', 'lt': 'Lituanian'
        }
        tweets_list = tweepy.Cursor(api.search, q="#WeLoveGoats -filter:retweets",tweet_mode='extended').items()
        for tweet in tweets_list:
            text = tweet._json["full_text"]
            created_at =  tweet.created_at.strftime('%m/%d/%Y %H:%M')
            username = tweet.user.screen_name 
            # tweet.id
            # retweet_count
            language = bcp47_dictionary[tweet.lang]
            
            url = "https://twitter.com/"+username+"/status/"+str(tweet.id)

            if(tweet.place is None):
                coordinates = [[['-5.97317','37.38283']]]
                country = 'Spain'
            else:
                country = tweet.place.country
                coordinates = tweet.place.bounding_box.coordinates
            Tweet.objects.create(text=text[0:12], user=username, location=country, url=url, created_at=created_at, titulo=text, latitud=coordinates[0][0][1], longitud=coordinates[0][0][0])
       

    
        return redirect("/tweets/api/map")