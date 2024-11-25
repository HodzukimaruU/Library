from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Book
from .serializers import BookSerializer
from datetime import datetime

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        min_pages = request.data.get('min_pages')
        max_pages = request.data.get('max_pages')

        filters = Q()

        if start_date:
            filters &= Q(publication_date__gte=datetime.strptime(start_date, '%Y-%m-%d').date())
        if end_date:
            filters &= Q(publication_date__lte=datetime.strptime(end_date, '%Y-%m-%d').date())
        if min_pages:
            filters &= Q(pages__gte=int(min_pages))
        if max_pages:
            filters &= Q(pages__lte=int(max_pages))

        books = Book.objects.filter(filters).order_by('pages')

        serializer = BookSerializer(books, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


# SELECT * 
# FROM core_book
# WHERE publication_date >= '2020-01-01'
#   AND publication_date <= '2023-12-31'
#   AND pages >= 100
#   AND pages <= 500
# ORDER BY pages;
