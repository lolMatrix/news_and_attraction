import os
from weblib import mongo_api


def run():
    collection = mongo_api.get_news_list()
    for news in collection["news"]:
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
            collection["tomita"] = ({"Person": i, "News": news['text']})

        for j in attraction:
            collection["tomita"] = ({"Object": j, "News": news['text']})

        mongo_api.save_news(collection)
        politician.clear()
        attraction.clear()


def start_tomita():
    while True:
        run()
