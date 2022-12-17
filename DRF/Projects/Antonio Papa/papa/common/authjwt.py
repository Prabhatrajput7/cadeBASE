import datetime, jwt
from papa import settings
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from app.models import User

class JWTauth(BaseAuthentication):

    def authenticate(self, request):
        is_ambassador = 'api/ambassador' in request.path

        token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('unauthenticated')

        # So if you are not mean, you should not access the ambassador site and the opposite so we can login.
        if (is_ambassador and payload['scope'] != 'ambassador') or (not is_ambassador and payload['scope'] != 'admin'):
            raise exceptions.AuthenticationFailed('Invalid Scope!')

        user = User.objects.get(pk=payload['user_id'])

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        # self.user, self.auth = user_auth_tuple
        # TypeError: cannot unpack non-iterable User object
        return (user, None)

    @staticmethod
    def generate_jwt(id, scope=None):
        payload = {
            'user_id': id,
            'scope': scope,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
        }

        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')