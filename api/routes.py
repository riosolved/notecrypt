from flask import Blueprint, request
import handlers

api = Blueprint('api', __name__)

@api.route('/enter', methods=['OPTIONS', 'POST'])
def enter():
    return handlers.enter(request)

@api.route('/register', methods=['OPTIONS', 'POST'])
def register():
    return handlers.register(request)

@api.route('/session/validate')
def authenticated():
    return handlers.session.validate(request)
