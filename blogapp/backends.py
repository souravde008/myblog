from . models import Users
from django.db.models import Q
from django.contrib.auth.hashers import check_password


class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return Users.objects.get(pk=user_id)
       except Users.DoesNotExist:
          return None


    def authenticate(self, username, password):
        try:
            user = Users.objects.get(
                Q(user_mail=username) | Q(user_phone=username)
            )
        except Users.DoesNotExist:
            return None

        return user if check_password(password,user.user_password) else None


