import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv('ACCOUNT_ID')
ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
REGION = os.getenv('REGION') or "auto"
BUCKET_NAME= os.getenv('BUCKET_NAME')

info = {
    "ACCOUNT_ID": ACCOUNT_ID,
    "ACCESS_KEY_ID": ACCESS_KEY_ID,
    "SECRET_ACCESS_KEY": SECRET_ACCESS_KEY,
    "REGION": REGION,
    "BUCKET_NAME": BUCKET_NAME
}

for value in info.values():
    if not value:
        raise ValueError("Missing environment variable")