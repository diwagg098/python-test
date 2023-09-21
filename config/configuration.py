import os
from dotenv import load_dotenv, find_dotenv
# Load environment
load_dotenv(find_dotenv())
app_code = os.getenv("APP_CODE", "test")
class Configuration(object):
     # Basic
     DEBUG = os.getenv("DEBUG") == "True"
     PORT = int(os.getenv("PORT", 5000))