from pymongo import MongoClient

from weblib import mongo_api
import os


def run():
    client = MongoClient(["localhost"], ["27017"])
    collection_download = client["news"]
    collection_upload = client["newses"]["tomitaParserCollection"]
    for news in collection_download.find({}):
        with open("../tomita/input.txt", "w") as file:
            file.write(news['text'])
    os.system("../tomita/tomita-parser cfg.proto")

    politician = []
    attraction = []
    place = ""
    with open("../tomita/output.txt", "r") as file:
        file_output = file.read()
        words = file_output.split()
        for i in range(len(words)):
            if words[i] == "Politician":
                if words[i + 2] not in politician:
                    politician.append(words[i + 2])
            elif words[i] == "Attraction":
                if words[i + 2] not in place:
                    attraction.append(words[i + 2])

    for i in politician:
        collection_upload.insert_one({"Person": i, "News": news['text']})

    for j in attraction:
        collection_upload.insert_one({"Object": j, "News": news['text']})

    politician.clear()
    attraction.clear()
