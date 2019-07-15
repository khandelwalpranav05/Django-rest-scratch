from .views import BlogPostRudView,BlogPostAPIView
from django.urls import path

urlpatterns = [
	path('',BlogPostAPIView.as_view(),name = 'post-create'),
    path('<int:pk>/',BlogPostRudView.as_view(),name = 'post-rud'),
]
