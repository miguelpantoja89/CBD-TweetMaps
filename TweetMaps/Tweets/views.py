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
        #'Bengali': 'bn'	'Hebrew': 'iw'	'Norwegian': 'no'	'Swedish': 'sv'
# 'Bosnian': 'bs'	'Hindi': 'hi'	'Oriya': 'or'	'Tagalog': 'tl'
# 'Bulgarian': 'bg'	'Latinized Hindi': 'hi-Latn'	'Panjabi': 'pa'	'Tamil': 'ta'
# 'Burmese': 'my'	'Hungarian': 'hu'	'Pashto': 'ps'	'Telugu': 'te'
# 'Croatian': 'hr'	'Icelandic': 'is'	'Persian': 'fa'	'Thai': 'th'
# 'Catalan': 'ca'	'Indonesian': 'in'	'Polish': 'pl'	'Tibetan': 'bo'
# 'Czech': 'cs'	'Italian': 'it'	'Portuguese': 'pt'	'Traditional Chinese':'zh-TW'
# 'Danish': 'da'	'Japanese': 'ja'	'Romanian': 'ro'	'Turkish': 'tr'
# 'Dutch': 'nl'	'Kannada': 'kn'	'Russian': 'ru'	'Ukrainian': 'uk'
# 	'Khmer': 'km'	'Serbian': 'sr'	'Urdu': 'ur'
# 'Estonian': 'et'	'Korean': 'ko'	'Simplified Chinese': 'zh-CN'	'Uyghur': 'ug'
# 'Finnish': 'fi'	'Lao': 'lo'	'Sindhi': 'sd'	'Vietnamese': 'vi'
# 'French': 'fr'	'Latvian': 'lv'	'Sinhala': 'si'	'Welsh': 'cy'
# 'Georgian': 'ka'	'Lithuanian': 'lt'
        bcp47_dictionary = { 'am':'Amharic', 'de':'German', 'ml':'Malayalam', 'sk':'Slovak','ar' : 
'Arabic', 'el':'Greek','dv': 'Maldivian', 'sl':'Slovenian',
'hy': 'Armenian', 'gu' : 'Gujarati', 'mr': 	'Marathi', 'ckb': 'Kurdish','eu' : 
'Basque', 'ht':'Creole',  'ne': 'Nepali','es':	'Spanish', 'ja':'Japanese','en':'English','tl':'Tagalog','und':'Undefined',
        }
        tweets_list = tweepy.Cursor(api.search, q="#WeLoveGoats -filter:retweets",tweet_mode='extended').items()
        for tweet in tweets_list:
            text = tweet._json["full_text"]
            created_at =  tweet.created_at.strftime('%m/%d/%Y %H:%M')
            username = tweet.user.screen_name 
            # tweet.id
            # retweet_count
            # bcp47_dictionary[tweet.lang]
            
            url = "https://twitter.com/"+username+"/status/"+str(tweet.id)

            if(tweet.place is None):
                coordinates = [[['-5.97317','37.38283']]]
                country = 'Spain'
            else:
                country = tweet.place.country
                coordinates = tweet.place.bounding_box.coordinates
            Tweet.objects.create(text=text[0:12], user=username, location=country, url=url, created_at=created_at, titulo=text, latitud=coordinates[0][0][1], longitud=coordinates[0][0][0])
       

    
        return redirect("/tweets/api/map")