from django.shortcuts import render
from datetime import date

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer


class BookViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Book.objects.get(id=pk)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        queryset = Book.objects.create(
            name=self.request.data.get('name'),
            genres=self.request.data.get('genres'),
        )

    def update(self, request, pk):
        queryset = Book.objects.get(id=pk)
        queryset.name = self.request.data.get('name')
        queryset.genres = self.request.data.get('genres')
        queryset.save()
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, pk):
        Book.objects.get(id=pk).delete()
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset)
        return Response(serializer.data)


class JournalViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Journal.objects.get(id=pk)
        serializer = JournalSerializer(queryset)
        return Response(serializer.data)

    def create(self, request):
        queryset = Journal.objects.create(
            name=self.request.data.get('name'),
            genres=self.request.data.get('genres'),
        )

    def update(self, request, pk):
        queryset = Journal.objects.get(id=pk)
        queryset.name = self.request.data.get('name')
        queryset.type = self.request.data.get('type')
        queryset.publisher = self.request.data.get('publisher')
        queryset.save()
        serializer = JournalSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, pk):
        Journal.objects.get(id=pk).delete()
        queryset = Journal.objects.all()
        serializer = JournalSerializer(queryset)
        return Response(serializer.data)
