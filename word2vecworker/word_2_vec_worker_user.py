#!/usr/bin/env python
from pyspark.sql import SparkSession
from pyspark.ml.feature import Word2VecModel

MODEL_PATH = "model"

spark = SparkSession \
    .builder \
    .appName("word2vec") \
    .getOrCreate()

model = Word2VecModel.load(MODEL_PATH)
count = 10

while(True):
    try:
        word = input("[INPUT] Введите слово из словаря: ")
        if(word == "--exit"):
            break
        elif(word == "--count"):
            count = int(input("[INPUT] Введите кол-во синонимов: "))
            print(count)
        else:
            model.findSynonyms(word, count).show(n=count)
    except Exception as ex:
        print("[ERROR] Данного слова нет в словаре!")

spark.stop()