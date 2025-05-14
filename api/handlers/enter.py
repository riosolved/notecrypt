from flask import jsonify
import json
import utilities
import bcrypt

def enter(request):
    try:
        utilities.guard()
    except Exception as error:
        return jsonify({
            'error': 'HTTPS is required.'
        }), 403

    try:
        database = utilities.database.instance()
    except Exception as error:
        return jsonify({
            'error': 'Issue with database.'
        }), 500

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
        return jsonify({
            'error': 'Not registered.'
        }), 400

    password_hashed = record[2]

    if not bcrypt.checkpw(
        password.encode('utf-8'),
        password_hashed.encode('utf-8')
    ):
        return jsonify({
            'error': 'Invalid password.'
        }), 400

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
