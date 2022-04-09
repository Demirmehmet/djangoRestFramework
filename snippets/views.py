import json

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    if request.method == 'GET':
        result = None
        # TODO Pagination ekle buraya gerekirse diğerlerinede ekle
        # TODO Durum kodunu ekle tüm response değerleri için
        # Query String varsa gelen değere göre filtreleyip döndür
        if request.query_params.get('title') is not None:
            # snippets = Snippet.objects.filter(title=request.query_params.get('title')) # direkt eşitlik
            snippets = Snippet.objects.filter(Q(title__exact=request.query_params.get('title'))
                                              & Q(
                title=request.query_params.get('title')))  # koşullu eşitlik Q kullanımı
            serializer = SnippetSerializer(snippets, many=True)
            result = Response(serializer.data)
        # Yoksa hepsini döndür
        else:
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            result = Response(serializer.data)
        return result

    elif request.method == 'POST':  # Insert yap
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def sample_page(request):
    return render(
        request,
        "samplePage.html",
        {"data": snippet_list(request).data},
    )
