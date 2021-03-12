from django.urls import path
from social.views import PostListView,PostDetailView


urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
]