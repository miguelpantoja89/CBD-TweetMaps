from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Tweet
import tweepy
import datetime
from django.db.models import Max
from django.conf import settings

class AllTweetsView(TemplateView):
    template_name="tweets.html"
    def get(self, request):
        tweets = Tweet.objects.all()
        half = int(len(tweets)/2)
        tw1 = tweets[0:half]
        tw2 = tweets[half:(len(tweets))]
        
        return render(request, self.template_name, {'tweets1':tw1, 'tweets2':tw2})
class MarkersMapView(TemplateView):
    template_name = "map.html"
    def get(self, request):
        marker = Tweet.objects.all()
        marker2 = Tweet.objects.all()[0:4]
        tweet_max_rt = Tweet.objects.aggregate(num_retweets=Max('num_retweets'))['num_retweets']
        tweet_RT = Tweet.objects.filter(num_retweets=tweet_max_rt)[0]
        idiomas = Tweet.objects.values('language').distinct()
        lang = []
        tweets_byLang = []
        for i in idiomas:
            lang.append(i['language'])
            tweets_byLang.append(Tweet.objects.filter(language=i['language']).count())
        totalL= zip(lang,tweets_byLang)
        return render(request, self.template_name, {'data':'hola','patata':marker, 'patata2':marker2, 'maxRT':tweet_RT, 'idiomas':totalL})

class StatisticsView(TemplateView):
    template_name="statistics.html"
    def get(self,request):
        source_type_app = Tweet.objects.filter(source='App').count()
        source_type_web = Tweet.objects.filter(source='Web').count()
        countries = Tweet.objects.values('location').distinct()
        tweets = Tweet.objects.all()
        times_m = []
        times_t = []
        fecha_semana= []
        cantidad_tweet_dia = []
        mid_day = datetime.time(12,0,0)
        for t in tweets:
            if(t.posted.time() < mid_day):
                times_m.append(t.posted.time())
            if(t.posted.time() > mid_day):
                times_t.append(t.posted.time())
            if(t.posted.date() > datetime.datetime.now().date() - datetime.timedelta(days=7)):
                fecha_semana.append(t.posted.date().strftime('%A'))
        l,m,x,j,v,s,d = 0,0,0,0,0,0,0
        for f in fecha_semana:
            if(f =='Monday'):
                l+=1
            if(f =='Tuesday'):
                m+=1
            if(f =='Wednesday'):
                x+=1
            if(f =='Thursday'):
                j+=1
            if(f =='Friday'):
                v+=1
            if(f =='Saturday'):
                s+=1
            if(f =='Sunday'):
                d+=1
        cantidad_tweet_dia.append(l)
        cantidad_tweet_dia.append(m)  
        cantidad_tweet_dia.append(x)  
        cantidad_tweet_dia.append(j)  
        cantidad_tweet_dia.append(v)  
        cantidad_tweet_dia.append(s)  
        cantidad_tweet_dia.append(d)  

        paises = []
        tweets_byCountry = []
        for i in countries:
            paises.append(i['location'])
            tweets_byCountry.append(Tweet.objects.filter(location=i['location']).count())
        return render(request, self.template_name, {'web':source_type_web, 'app':source_type_app, 'paises':paises, 'tweetsPorPais':tweets_byCountry, 'horasM':len(times_m), 'horasT':len(times_t), 'semanaLast': cantidad_tweet_dia})
    

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
'hy': 'Armenian', 'gu' : 'Gujarati', 'mr':     'Marathi', 'ckb': 'Kurdish','eu' : 
'Basque', 'ht':'Creole',  'ne': 'Nepali','es':    'Spanish', 'ja':'Japanese','en':'English','tl':'Tagalog','und':'Undefined',
'bn':'Bengali', 'iw':'Hebrew', 'no':'Norwegian', 'sv': 'Swedish', 'bs':'Bosnian', 'hi':'Hindi', 'or':'Oriya', 'tl':'Tagalog', 'bg':'Bulgarian', 
'hi-Latn':'Latinized Hindi', 'pa':'Panjabi', 'ta':'Tamil', 'my':'Burmese', 'hu': 'Hungarian', 'ps': 'Pashto', 'te': 'Telugu', 'hr': 'Croatian',
'is': 'Icelandic', 'fa': 'Persian', 'th': 'Thai', 'ca': 'Catalan', 'in': 'Indonesian', 'pl': 'Polish', 'bo': 'Tibetan', 'cs':'Czech', 'it': 'Italian',
'pt': 'Portuguese', 'zh-TW': 'Traditional Chinese', 'da': 'Danish', 'ro': 'Romanian', 'tr': 'Turkish', 'nl': 'Dutch', 'kn': 'Kannada', 'ru': 'Russian', 
'uk': 'Ukranian', 'km': 'Khmer', 'sr':'Serbian', 'ur':'Urdu', 'et': 'Estonian', 'ko': 'Koraean', 'zh-CN': 'Simplified Chinese', 'ug': 'Uyghur', 
'fi': 'Finnish', 'lo':'Lao', 'sd': 'Sindhi', 'vi': 'Vietnamese', 'fr': 'French', 'lv': 'Latvian', 'si': 'Sinhala', 'cy': 'Welsh', 'ka': 'Georgian', 'lt': 'Lituanian'
        }
        tweets_list = tweepy.Cursor(api.search, q="#WeLoveGoats -filter:retweets",tweet_mode='extended').items()
        for tweet in tweets_list:
            text = tweet._json["full_text"]
            created_at =  tweet.created_at.strftime('%Y-%m-%d %H:%M')
            username = tweet.user.screen_name 
            # tweet.id
            # retweet_count
            idioma =  bcp47_dictionary[tweet.lang]
            if('Web' in tweet.source):
                source_type = 'Web'
            else:
                source_type = 'App'
            
            url = "https://twitter.com/"+username+"/status/"+str(tweet.id)

            if(tweet.place is None):
                coordinates = [[['-5.97317','37.38283']]]
                country = 'Spain'
            else:
                country = tweet.place.country
                coordinates = tweet.place.bounding_box.coordinates
            Tweet.objects.create(text=text[0:12], user=username, location=country, url=url, posted=created_at, titulo=text, latitud=coordinates[0][0][1], longitud=coordinates[0][0][0], language=idioma,num_retweets=tweet.retweet_count,
            source=source_type)
       

    
        return redirect("/tweets/api/map")