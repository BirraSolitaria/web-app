from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('createPost', views.redirectToCreatePost, name='createPost'),
    path('<int:pk>',views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update',views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete',views.NewsDeleteView.as_view(), name='news_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)