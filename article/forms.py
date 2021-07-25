from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","animal_type","animal_city","animal_age","animal_gender","article_image"]
        
