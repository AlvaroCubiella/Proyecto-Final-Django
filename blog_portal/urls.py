from django.urls import path, reverse_lazy
from blog_portal.views import (MainPageView, ArticleDetailView, 
                                About, SearchArticle)


urlpatterns = [
    path('', MainPageView.as_view(), name='main-page'), 
    path('about/', About.as_view(), name="about"),
    # path('article/create/', CreateArticle.as_view(), name='create-article'),
    path('article/resultado_busqueda/', SearchArticle.as_view(), name='search-article'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),          #pk es de Primary Key (clave primaria, por defecto el ID)
]