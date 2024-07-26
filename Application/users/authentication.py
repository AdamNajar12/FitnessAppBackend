import jwt
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'email': user.email,
        'role': user.role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    # Retirer l'appel à .decode('utf-8')
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')



class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
           payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
           print(f"Decoded Payload: {payload}")  # Ajoutez cette ligne pour vérifier le contenu du token
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
              raise exceptions.AuthenticationFailed('Invalid token')


        user = get_user_model().objects.filter(id=payload['user_id']).first()
        if user is None:
            print(f"User with id {payload['user_id']} not found in the database")
            raise exceptions.AuthenticationFailed('User not found!')

        print(f"Authenticated User: {user}")

        return (user, None)