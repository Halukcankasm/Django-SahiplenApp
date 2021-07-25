import article
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
#from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def addArticle(request):
    form = ArticleForm(request.POST or None ,request.FILES or None)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("index")
    

    return render(request,"addarticle.html",{"form":form}) 

def detail(request,id):
    #article = Article.objects.filter(id = id).first
    article = get_object_or_404(Article,id = id)
    context = {
        "article":article
    } 

    return render(request,"detail.html",context)

@login_required(login_url="user:loginUser")
def update(request,id):

    article = get_object_or_404(Article, id = id)

    form = ArticleForm(request.POST or None , request.FILES or None,instance= article)

    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("article:dashboard")
    
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:loginUser")
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)

    article.delete()

    messages.success(request,"Makale başarıyla silindi")

    return redirect("article:dashboard")

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()
    return render(request,"deneme2.html",{"articles":articles})

def detail(request,id):
    #articles = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)

    context = {"article":article}

    return render(request,"detail.html",context)


    