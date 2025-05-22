from flask import Blueprint, request
import handlers

api = Blueprint('api', __name__)

@api.route('/enter', methods=['OPTIONS', 'POST'])
def enter():
    return handlers.enter(request)

@api.route('/account/register', methods=['OPTIONS', 'POST'])
def register():
    return handlers.register(request)

# TODO
@api.route('/account/activate', methods=['GET'])
def activate():
    return handlers.activate(request)

# TODO
@api.route('/account/activation/email', methods=['OPTIONS', 'POST'])
def activation():
    return handlers.activation(request)

# TODO
@api.route('/session/validate')
def session_validate():
    return handlers.session.validate(request)

# TODO
@api.route('/password/reset')
def password_reset():
    return handlers.password.reset(request)
