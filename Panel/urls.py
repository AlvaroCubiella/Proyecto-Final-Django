from django.urls import path
from Panel.views import (PanelView, ArticleCreateView, ArticleDeleteView)

urlpatterns = [
    path('', PanelView.as_view(), name='index-panel'),
    path('article/create', ArticleCreateView.as_view(), name ="article-create" ),
    # path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update" ),
    path('article/<pk>/delete', ArticleDeleteView.as_view(), name ="article-delete" ),
    
]