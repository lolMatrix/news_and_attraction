from bson import json_util, ObjectId
from django.shortcuts import render

# Create your views here.
from django.template import loader
from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from web import api

config = api.get_database_config()
client = MongoClient(config['host'], config['port'])

db = config['db_name']
collection = config['collection']


@api_view(['GET'])
def get_all_news(request):
    news_list = client[db][collection].find({}).sort("_id", -1)
    return Response(json.loads(json_util.dumps(list(news_list))))


@api_view(['POST'])
def save_news(request):
    try:
        req = dict(request.data)
        if client[db][collection].count_documents(req) < 1:
            client[db][collection].insert_one(req)
    except Exception as e:
        print(f"произошли шоколадки {e}")
    return Response({"status": "ok"})


@api_view(['PUT'])
def update_news(request):
    update = dict(request.data)
    filter = {
        '_id': ObjectId(update['_id']['$oid'])
    }
    update.pop("_id", None)
    client[db][collection].update_one(filter, {'$set': update}, upsert=False)
    return Response({})


def get_news_html(request):
    return render(request, "index.html")


@api_view(['GET'])
def get_news_page(request, page: int):
    if page == 0:
        page = 1

    news_list = client[db][collection].find({}).sort("_id", -1).limit(10).skip(10 * page)
    return Response(json_util.dumps(list(news_list)))


@api_view(['GET'])
def get_count_pages(request):
    news_count = client[db][collection].count_documents({})
    pages = news_count // 10
    return Response(json.loads(json_util.dumps({"count": pages})))
