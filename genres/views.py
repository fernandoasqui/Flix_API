# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalDefaultPermission

# class based view


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# o formato abaixo é em funtion based view
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         # retorna a lista de todos os generos do banco
#         genres = Genre.objects.all()
#         # serializando na mão com list comprehension
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         # salva no banco de dados
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name': new_genre.name},
#             status=201,
#         )


# @csrf_exempt
# def genre_detail_view(request, pk):
#     # similar ao select from x where id = id
#     genre = get_object_or_404(Genre, pk=pk)
#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)
#     elif request.method == 'PUT':
#         # pegar o que o user enviou no corpo
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {'id': genre.id, 'name': genre.name}, status=201
#         )
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse(
#             {'message': 'Gênero excluido com sucesso!'}, status=204
#         )
