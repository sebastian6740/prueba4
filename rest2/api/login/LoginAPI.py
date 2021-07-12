from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token



class LoginAPI(APIView):
    def post(slf, request):
        data = request.data

        username = data['usuario']
        password = data ['clave']

        try:
            user = User.objects.get(username = username)
        except:
            return Response({"Error", "usuario no valido"}, status=400)

        clave_valida = check_password(password, user.password)

        if(clave_valida):
            token, created = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status=201)
        
        else:
            return Response({"Error": "contraseña invalida"}, status=400)


class LogoutAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            token = data['token']

            token = Token.objects.filter(key=token)
            token.delete()

            return Response(status=200)
        except:
            return Response(status=400)