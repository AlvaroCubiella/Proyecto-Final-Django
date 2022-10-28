from django.urls import path
from blog_portal.views import MainPageView, ArticleDetailView, About


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'),
    path('about/', About.as_view(), name="about"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),          #pk es de Primary Key (clave primaria, por defecto el ID)
]