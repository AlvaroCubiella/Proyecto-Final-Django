from django.urls import reverse_lazy
from multiprocessing import context, get_context
from django.template import loader
from django.contrib.staticfiles import storage
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View, CreateView
from blog_portal.models import Article, Portal
from blog_portal.forms import Search

import os

def index(request):
    return render(request, 'blog_portal/index.html')

# Calculo las cantidad de pag. a generar a partir de la cantidad de articulos encontrados
def set_pages(instance):
    articles = instance.objects.all()
    pages = len(articles)/4
    if round(pages) < pages:
        pages = round(pages) + 1
    else:
        pages = round(pages)
    pages = range(1, pages+1)
    return pages

class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # type: ignore
        context['headline'] = Article.objects.filter(is_headline=True).order_by('date_updated').first()
        context['portal'] = Portal.objects.order_by('date_updated').first()
        return context 

class MainPageView(BaseView, TemplateView):
    queryset = Article.objects.all()
    context_object_name = "articles"
    template_name = "blog_portal/index.html"

    def get(self, request):
        context = self.get_context_data()
        # Cargo los articulos ordenados por fecha. Reverse es para poner la fecha mas reciente primera en la lista
        article = Article.objects.order_by('date_created').reverse()    # En la ultima clase vi que se puede usar '-date_created', 
                                                                        # pero preferi dejarlo asi, como me salio a mi en el barco.           
        left_col = article[0::2]                                        # Obtengo los impares de la lsita para armar la columna izquierda
        rigth_col = article[1::2]                                       # Obtengo los pares de la lsita para armar la columna derecha
        
        # Armo la cabecera del html
        head = {
            'title':'Trabajando a la mar',
            'headline':'Bienvenido al mundo de la Oceanografía Fisica',
            'sub':'Un trabajo de Alvaro Cubiella para Coderhouse',
            # 'pages': pages,           
        }
    
        # Armo la vista de la nota mas reciente
        new = {
            'date_created': left_col[0].date_created,    
            'title': left_col[0].title,
            'short_content': left_col[0].short_content,
            'image': left_col[0].image,
            'id': left_col[0].id,
        }
        
        # Paso la lista de los articulos para la columna izquierda
        left_col = {
            'left_col': left_col,
        }
        
        # Paso la lista de los articulos para la columna derecha
        rigth_col = {
            'rigth_col': rigth_col,
        }
        context['head'] = head
        context['new'] = new
        context['left_col'] = left_col
        context['rigth_col'] = rigth_col
        
        return render(request, self.template_name, context)

# class CreateArticle(CreateView):
#     model = Article
#     fields = ['title', 'short_content', 'content', 'author', 'image', 'is_headline', 'image']
#     template_name = "blog_portal/article_form.html"
#     success_url = reverse_lazy("main-page")

class About(BaseView, TemplateView):

    template_name = "blog_portal/about.html"

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog_portal/article_detail.html"
    
    def get(self, request, pk):
        context = get_object_or_404(self.model, pk=pk)
        return render(request, self.template_name, {'articles':context, 'pk':pk})

class SearchArticle(BaseView, TemplateView):
    article = Article.objects.all()
    template_name = "blog_portal/search_article.html"

    def post(self, request):
        context = self.get_context_data()
        text = request.POST['text'] 
        article = Article.objects.filter(title__icontains = text).all() 
        left_col = article[0::2]            # Obtengo los impares de la lsita para armar la columna izquierda
        rigth_col = article[1::2]           # Obtengo los pares de la lsita para armar la columna derecha

        # Armo la lista de los articulos para la columna izquierda
        left_col = {
            'left_col': left_col,
        }
        
        # Armo la lista de los articulos para la columna derecha
        rigth_col = {
            'rigth_col': rigth_col,
        }

        context['left_col'] = left_col
        context['rigth_col'] = rigth_col
        
        return render(request, self.template_name, context)