from flask import jsonify
import utilities

def activation(request):
   data = request.get_json()

   recepient = data.get('recepient')

   utilities.account.activation.email(recepient)

   response = jsonify({
      'message': 'Activation link sent.' 
   })

   response.status_code = 200

   return response
