from flask import Blueprint, request
import handlers

api = Blueprint('api', __name__)

@api.route('/enter', methods=['POST'])
def enter():
    return handlers.enter(request)

@api.route('/register', methods=['POST'])
def register():
    return handlers.register(request)

@api.route('/session/validate')
def authenticated():
    return handlers.session.validate(request)
