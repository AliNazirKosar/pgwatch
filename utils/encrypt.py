# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("ENCRYPT_KEY")

fernet = Fernet(SECRET_KEY)

def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypt_password: str) -> str:
    return fernet.decrypt(encrypt_password.encode()).decode()