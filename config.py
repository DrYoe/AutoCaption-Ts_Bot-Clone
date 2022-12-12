import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 12158462))
      API_HASH = os.environ.get("API_HASH", "0b962717d931f4480c46d56c85d409a5")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "yoenaung")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 1348153685 )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://yoenaung:yoenaung@cluster0.t67tc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
