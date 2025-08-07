from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.first_name
        token['id'] = str(user.id)
        groups = user.groups.values_list('name', flat=True)
        token['roles'] = list(groups)
        return token