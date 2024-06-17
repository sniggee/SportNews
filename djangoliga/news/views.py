from django.http import HttpResponse
from rest_framework import generics

from .models import Info, Comment
from .serializer import InfoSerializer, UsersSerializers, CommentSerializer
from common.models import Sport
from django.views.generic import View
from django.contrib.auth.models import User
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class Infopost(generics.ListCreateAPIView):
    queryset = Info.objects.filter(sport=Sport.objects.get(name="Футбол"))
    serializer_class = UsersSerializers


class Info_get_post_path(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.filter(sport=Sport.objects.get(name="Футбол"))
    serializer_class = InfoSerializer


class Infopost_Basket(generics.ListCreateAPIView):
    queryset = Info.objects.filter(sport=Sport.objects.get(name="Баскетбол"))
    serializer_class = InfoSerializer


class Info_get_post_path_Basket(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.filter(sport=Sport.objects.get(name="Баскетбол"))
    serializer_class = InfoSerializer

class Infopost_Hokey(generics.ListCreateAPIView):
    queryset = Info.objects.filter(sport=Sport.objects.get(name="Хоккей"))
    serializer_class = InfoSerializer


class Info_get_post_path_Hokey(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.filter(sport=Sport.objects.get(name="Хоккей"))
    serializer_class = InfoSerializer


class GetComments(View):
    def get(self, request, news_id):
        news = Info.objects.get(id=news_id)
        
        comments = [
            CommentSerializer(comment).data for comment in Comment.objects.filter(news=news)
        ]
        
        return HttpResponse(json.dumps(comments))
    
@method_decorator(csrf_exempt, name="dispatch")
class CreateComment(View):
    def post(self, request):
        data = json.loads(request.body)
        
        news = Info.objects.get(id=int(data.get("news")))
        
        comment = Comment.objects.create(
            user=User.objects.get(username=data.get("user")),
            text=data.get("text"),
            news=news
        )
        
        return HttpResponse(json.dumps(CommentSerializer(comment).data), status=201)