from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog_portal.models import Article, Publisher, Portal
from blog_portal.views import BaseView

class PanelLogin(LoginView):
    template_name = 'blog_portal/panel_login.html'
    next_page = reverse_lazy("index-panel")

class PanelLogout(LogoutView):
    template_name = 'blog_portal/panel_logout.html'

class PanelView(LoginRequiredMixin, BaseView, ListView):
    queryset = Article.objects.all()
    template_name = "blog_portal/article_list.html"    
    context_object_name = "articles"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['short_content','title' , 'content', 'author', 'image', 'is_headline', 'image']
    template_name = "blog_portal/article_form.html"
    success_url = reverse_lazy("index-panel")

class ArticleDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Article
    success_url = reverse_lazy('index-panel')

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author', 'image', 'is_headline', 'image']
    success_url = reverse_lazy('index-panel')