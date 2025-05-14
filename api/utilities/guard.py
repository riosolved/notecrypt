from flask import request, jsonify 

def guard():
    proto = request.headers.get('X-Forwarded-Proto', request.scheme)

    if proto != 'https':
        print(f"[DATABASE][Instance] Error: {error}")

        raise RuntimeError("HTTPS is required")
