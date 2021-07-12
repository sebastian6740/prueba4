from api.libro.libroSLR import LibroSerializado
from api.models import Libro
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated


class LibroAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            libros = Libro.objects.all()
            serializador = LibroSerializado(libros, many=True)

            return Response(serializador.data, status=200)
        except:
            return Response(status=400)

    def post(self, request):
        serializador = LibroSerializado(data=request.data)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=200)
        else:
            return Response(serializador.errors, status=400)
    
    def put(self, request, id):
        libro = Libro.objects.get(id = id)

        serializador = LibroSerializado(libro, data=request.data)

        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=200)
        else:
            return Response(serializador.errors, status=400)
    
    def delete(self, request, id):
        libro = Libro.objects.get(id = id)
        libro.delete()

        return Response(status=200)