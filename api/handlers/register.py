from flask import jsonify
import json
import utilities
import bcrypt

def register(request):
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

    # NOTE : VALIDATION - Were credentials provided?
    if not email or not password:
        return jsonify ({
            'error': 'Email and password are required.'
        }), 400

    database['cursor'].execute("""
        SELECT *
        FROM users

        WHERE email = %s
    """, (
        email,
    ))

    # NOTE : VALIDATION - Does user exist?
    if database['cursor'].fetchone():
        return jsonify ({
            'error': 'Email is already in use.'
        }), 400


    salt = bcrypt.gensalt()

    password_hashed = bcrypt.hashpw(
        password.encode('utf-8'),
        salt
    )

    # NOTE : Insert the new user.
    database['cursor'].execute("""
        INSERT
        INTO users (
            email,
            password
        ) VALUES (
            %s,
            %s
        )
    """, (
        email,
        password_hashed
    ))

    user_id = database['cursor'].lastrowid

    database['connection'].commit()
    database['cursor'].close()

    # NOTE : SESSION TOKEN
    token = utilities.session.create(user_id, request)

    # NOTE : RESPOND
    response = jsonify({
        'message': 'User registered successfully.'
    })

    utilities.session.header(
        token,
        response
    )

    response.status_code = 201

    return response
