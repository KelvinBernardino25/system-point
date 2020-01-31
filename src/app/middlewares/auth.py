from flask import current_app
from datetime import datetime
from time import time
import jwt

key = current_app.config['SECRET_KEY'] if (
    current_app) else "15291f67d99ea7bc578c3544dadfbb991e66fa69cb36ff70fe30e798e111ff5f"


def encoded_token(id, expires_in=86400):
    return jwt.encode({'auth': id, 'exp': time() + expires_in},
                      key, algorithm='HS256').decode('utf-8')


def decode_token(token):
    id = jwt.decode(token, key, algorithms=['HS256'])['auth']
    return id


def verify_token(token):
    try:
        verified_token = decode_token(token)
    except jwt.ExpiredSignatureError:
        return {"message": "Signature has expired", "status": 401}
    except jwt.InvalidTokenError:
        return {"message": "Invalid Token", "status": 401}
    return {"id": verified_token}
