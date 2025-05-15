from flask import jsonify, make_response
import json
import utilities
import bcrypt

def enter(request):
    try:
        utilities.guard()
    except Exception as error:
        response = jsonify({
            'error': 'HTTPS is required.'
        })

        # TODO : MAKE THE FOLLOWING RE-USABLE AND APPLY IN /register AS WELL
        response.headers['Access-Control-Allow-Origin'] = 'https://client.localhost'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        response.status_code = 403

        return response

    if request.method == 'OPTIONS':
        response = make_response()

        response.headers['Access-Control-Allow-Origin'] = 'https://client.localhost'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        return response

    try:
        database = utilities.database.instance()
    except Exception as error:
        response = jsonify({
            'error': 'Issue with database.'
        })

        response.headers['Access-Control-Allow-Origin'] = 'https://client.localhost'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        response.status_code = 500

        return response

    # TODO : WHAT IF THE REQUEST IS COMING IN WITH AN EXISITING SESSION
    # - VALIDATE
    # - RETURN EARLY

    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    database['cursor'].execute("""
        SELECT *
        FROM users

        WHERE email = %s
    """, (
        email,
    ))

    record = database['cursor'].fetchone()

    if not record:
        response = jsonify({
            'error': 'Not registered.'
        })

        response.headers['Access-Control-Allow-Origin'] = 'https://client.localhost'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        response.status_code = 400

        return response

    password_hashed = record[2]

    if not bcrypt.checkpw(
        password.encode('utf-8'),
        password_hashed.encode('utf-8')
    ):
        response = jsonify({
            'error': 'Invalid password.'
        })

        response.headers['Access-Control-Allow-Origin'] = 'https://client.localhost'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        response.headers['Access-Control-Allow-Credentials'] = 'true'

        response.status_code = 400

        return response

    database['cursor'].close()

    # NOTE : SESSION TOKEN
    user_id = record[1]

    token = utilities.session.create(user_id, request)

    # NOTE : RESPOND
    response = jsonify({
        'message': 'Access granted.'
    })

    utilities.session.header(
        token,
        response
    )

    response.status_code = 200

    return response
