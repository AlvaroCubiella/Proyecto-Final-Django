from django.urls import path
from Panel.views import (PanelView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView,
                        PanelLogin, PanelLogout, ProfileView, ProfileUpdate, ProfileRegister)

urlpatterns = [
    path('', PanelView.as_view(), name='index-panel'),
    path('article/create', ArticleCreateView.as_view(), name ="article-create" ),
    path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update" ),
    path('article/<pk>/delete', ArticleDeleteView.as_view(), name ="article-delete" ),
    path('profile/', ProfileView.as_view(), name="panel-profile"),
    path('login/', PanelLogin.as_view(), name = 'panel-login'),
    path('logout/', PanelLogout.as_view(), name = 'panel-logout'),
    path('register/', ProfileRegister.as_view(), name = 'panel-register'),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="panel-profile_up"),
    
]