import hmac
import hashlib
import base64
import time
import os
import json

SESSION_SECRET_KEY = b''

def initialize(secret):
    if not secret:
        raise ValueError("SESSION_SECRET_KEY not set in environment.")

    SESSION_SECRET_KEY = secret.encode('utf-8')

# NOTE : CREATE SIGNED TOKEN
def create(
    user_id,
    request
):
    try:
        # NOTE : BASE
        ip_address = request.remote_addr
        user_agent = request.headers.get('User-Agent')

        payload_json = json.dumps({
            "user_id": user_id,
            "ip_address": ip_address,
            "user_agent": user_agent,
            "expiration": int(time.time()) + 3600, # NOTE : Expires in 1 hour.
        }).encode()

        payload_base64 = base64.urlsafe_b64encode(
            payload_json
        ).decode()

        # NOTE : SIGN
        signature = hmac.new(
            SESSION_SECRET_KEY,
            payload_base64.encode(),
            hashlib.sha256
        ).digest()

        signature_base64 = base64.urlsafe_b64encode(
            signature
        ).decode()

        # NOTE : TOKEN
        return f"{payload_base64}.{signature_base64}"

    except Exception as error:
        print(f"[SESSION] Error: {error}")

        return None

def validate(token):
    try:
        payload_base64, signature_base64 = token.split(".")

        expected_signature = hmac.new(
            SESSION_SECRET_KEY,
            payload_base64.encode(),
            hashlib.sha256
        ).digest()

        expected_signature_base64 = base64.urlsafe_b64encode(
            expected_signature
        ).decode()

        if not hmac.compare_digest(
            expected_signature_base64,
            signature_base64
        ):
            return None

        payload_json = base64.urlsafe_b64decode(
            payload_base64.encode()
        )

        payload = json.loads(payload_json)

        if payload["expiration"] < time.time():
            return None

        return payload["user_id"]

    except Exception as error:
        print(f"[SESSION][Validate] Error: {error}")

        return None

def header(
    token,
    response
):
    print(f"token: {token}")

    if not token:
        return

    response.set_cookie(
        'session',
        token,
        # NOTE : Prevents JavaScript access (mitigates XSS)
        httponly=True,
        # NOTE : Cookie only sent over HTTPS
        secure=True,
        samesite='Strict'
    )

    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Expose-Headers'] = 'Set-Cookie'
