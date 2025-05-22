import os
from flask import request, jsonify

def guard():
    if os.environ.get('ENVIRONMENT') == 'local':
        return

    proto = request.headers.get('X-Forwarded-Proto', request.scheme)

    if proto != 'https':
        print(f"[DATABASE][Instance] Error: {error}")

        raise RuntimeError("HTTPS is required")
