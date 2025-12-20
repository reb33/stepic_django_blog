from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]  # new
    filterset_fields = ['author']  # new


class PostDetail(generics.RetrieveUpdateDestroyAPIView): # Представление для GET (один пост), PUT/PATCH (обновление), DELETE (удаление).
    queryset = Post.objects.all()  # Все посты
    serializer_class = PostSerializer  # Использует PostSerializer


class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)
