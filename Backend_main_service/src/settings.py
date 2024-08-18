from dotenv import load_dotenv
import os

load_dotenv()

class settings:
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    BEARER_URL=os.environ.get("BEARER_URL")
    ACCESS_TOKEN_LIFETIME=os.environ.get("ACCESS_TOKEN_LIFETIME")
    SECRET=os.environ.get("SECRET")
    KAFKA_PORT=os.environ.get("KAFKA_PORT")
    KAFKA_IP=os.environ.get("KAFKA_IP")
    KAFKA_TOPIC=os.environ.get("KAFKA_TOPIC")
    KAFKA_TOPIC=os.environ.get("KAFKA_TOPIC")
    SMTP_HOST = os.environ.get("SMTP_HOST")
    SMTP_PORT = os.environ.get("SMTP_PORT")
    SMTP_SENDER=os.environ.get("SMTP_SENDER")
    SMTP_PASS=os.environ.get("SMTP_PASS")
    
    
