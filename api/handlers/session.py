from flask import jsonify
import utilities

def validate(request):
    token = request.cookies.get('session')

    user_id = utilities.session.validate(token)

    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401

    return jsonify({'message': 'You are authenticated!'})
