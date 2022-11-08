from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from blog_portal.models import Article, Publisher, Portal
from blog_portal.views import BaseView

class PanelView(BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "blog_portal/article_list.html"    
    context_object_name = "articles"

class ArticleCreateView(CreateView):
    model = Article
    fields = ['short_content','title' , 'content', 'author', 'image', 'is_headline', 'image', 'date_published']
    template_name = "blog_portal/article_form.html"
    success_url = reverse_lazy("index-panel")

class ArticleDeleteView(BaseView, DeleteView):
    model = Article
    success_url = reverse_lazy('index-panel')
