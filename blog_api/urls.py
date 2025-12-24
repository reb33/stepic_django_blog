from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import PostDetail, PostList, UserPostList

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='post_list'),
    path('user/<int:id>/', UserPostList.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # new
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),  # new
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # new
]
