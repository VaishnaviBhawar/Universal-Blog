from django import forms
from .models import Post,Category,Comment

choice=Category.objects.all().values_list('name','name')

choices=[]
for item in choice:
    choices.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category','snippet', 'body','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
              'body': forms.Textarea(attrs={'class': 'form-control'}),


        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            #'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
