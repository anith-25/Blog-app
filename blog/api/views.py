from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import BlogDetailSerializer, BlogListSerializer, BlogCreateSerializer
from ..models import Blog
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed

class BlogListAPIView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all().order_by("-publication_date")
        pagination = PageNumberPagination()
        page = pagination.paginate_queryset(blogs, request)
        serializer = BlogListSerializer(instance=page, many=True)
        return pagination.get_paginated_response(serializer.data)
    

class BlogDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogDetailSerializer(blog)
        return Response(serializer.data)
    

class BlogCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            Blog.objects.create(title=request.data["title"], content=request.data["content"], author=user)
            return Response({"message": "Blog Successfully Created"})
        return Response({"error": serializer.error_messages})
    

class BlogUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if not blog.author == request.user:
            raise AuthenticationFailed
        serializer = BlogCreateSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Blog Successfully Updated"})
        return Response({"error": serializer.error_messages})
    

class BlogDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if not blog.author == request.user:
            raise AuthenticationFailed
        blog.delete()
        return Response({"message": "Blog Successfully Deleted"})


