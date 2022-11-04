import findspark
findspark.init()

import requests
import json
import unidecode
from pyspark.sql import SparkSession


spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()