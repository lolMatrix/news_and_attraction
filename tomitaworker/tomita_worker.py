import os
import time

from tomitaworker import get_database_config
from weblib import mongo_api

config = get_database_config()


def run():
    collection = mongo_api.get_news_list()
    print("Новости получены")
    for news in collection:
        if "tomita" not in news:
            with open("tomitaworker/tomita/input.txt", "w") as file:
                file.write(news['title'] + news['text'])

            os.system("./tomitaworker/tomita/tomita-parser ./tomitaworker/tomita/config.proto")
            politician = []
            attraction = []
            attr_sent = []
            pol_sent = []

            with open("tomitaworker/tomita/output.txt", "r") as file:
                file_output = file.read()
                strings = file_output.split('\n')
                for i in range(len(strings)):
                    if "Politician" in strings[i]:
                        words = strings[i].split("Politician =")
                        if words[1] not in politician:
                            politician.append(words[1].strip().replace("_", " "))
                            counter = 0
                            while "{" in strings[i - counter] or "}" in strings[i - counter] \
                                    or "Fact" in strings[i - counter] or "Politician" in strings[i - counter]:
                                counter += 1

                            pol_sent.append(strings[i - counter])

                    elif "Attraction" in strings[i]:
                        words = strings[i].split("Attraction =")
                        if words[1] not in attraction:
                            attraction.append(words[1].strip().replace("_", " "))

                            counter = 0
                            while "{" in strings[i - counter] or "}" in strings[i - counter] \
                                    or "Fact" in strings[i - counter] or "Attraction" in strings[i - counter]:
                                counter += 1

                            attr_sent.append(strings[i - counter])

            if len(politician) > 0 or len(attraction) > 0:
                news["tomita"] = []

            for i in range(len(politician)):
                news["tomita"].append({"Person": politician[i], "Sentence": pol_sent[i]})

            for j in range(len(attraction)):
                news["tomita"].append({"Attraction": attraction[j], "Sentence": attr_sent[j]})

            mongo_api.update_news(news)

            politician.clear()
            attraction.clear()


def start_tomita():
    while True:
        try:
            run()
        except Exception as e:
            print(f"Ашибка {e}")
        time.sleep(config["sleepTime"])
