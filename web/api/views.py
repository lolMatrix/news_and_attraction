from bson import json_util
from django.shortcuts import render

# Create your views here.
from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

client = MongoClient('localhost', 27017)

@api_view(['GET'])
def get_all_news(request):
    news_list = client['newses']['news'].find({})
    return Response(json.loads(json_util.dumps(list(news_list))))

@api_view(['POST'])
def save_news(request):
    client['newses']['news'].insert_one(dict(request.data))
    return Response({"status": "ok"})
