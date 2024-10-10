# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29640188"))
API_HASH = getenv("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")
BOT_TOKEN = getenv("BOT_TOKEN", "7730834429:AAE8NYNj4Tp-OaTww2-R9H4n5fjrtwXWdLE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7504263874").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://syangshibo1:mongodbdatabase500@cluster0.vtkrte7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", -4543190195")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002279546936"))
