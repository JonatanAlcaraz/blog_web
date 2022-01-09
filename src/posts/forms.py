from django import forms #importar
from .models import Post, Comment, User_model #importar
from django.contrib.auth.forms import UserCreationForm #importar
#from django.contrib.auth.models import User
from django.forms import widgets 
from django.contrib.auth import get_user_model #importar

User = get_user_model() #importar
class LogInForm(forms.Form): #importar
    username = forms.CharField(
        min_length=4,
        max_length=50,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
            })
    )
    password = forms.CharField(
        min_length=8,
        max_length=70,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'type': 'password',
                'required': True
            })
    )


class SignUp_Form(UserCreationForm): # primero
    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2' , 'first_name' , 'last_name']

        def clean_username(self):
            username = self.cleaned_data['username'] # obtiene el valor de username
            q = User.objects.filter(username=username).exists() # devuelve un booleano si existe ese username
            if q:
                raise forms.ValidationError("Username already in use.")
            else:
                return username

        def clean(self):
            data = super().clean() #obtiene el fomulario 
            if data['password'] != data["password_confirmation"]: # compara y confirma el password
                raise forms.ValidationError("Passwords do not match")
            else:
                return data

class SignUpForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'required': True
            })
    )
    password = forms.CharField(
        min_length=8,
        max_length=70,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'type': 'password',
                'required': True
            })
    )
    password_confirmation = forms.CharField(
        min_length=8,
        max_length=70,
        label=False,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password confirmation',
                'class': 'form-control',
                'type': 'password',
                'required': True
            })
    )
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
                'required': True
            })
    )
    last_name = forms.CharField(
        min_length=3,
        max_length=50,
        label=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
                'required': True
            })
    )
    """email = forms.CharField(
        label=False,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'required': True
            })
    )"""

    def clean_username(self):
        username = self.cleaned_data['username'] # obtiene el valor de username
        q = User.objects.filter(username=username).exists() # devuelve un booleano si existe ese username
        if q:
            raise forms.ValidationError("Username already in use.")
        else:
            return username

    def clean(self):
        data = super().clean() #obtiene el fomulario 
        if data['password'] != data["password_confirmation"]: # compara y confirma el password
            raise forms.ValidationError("Passwords do not match")
        else:
            return data

    def save(self):
        data = self.cleaned_data #obtien el formulario entero 
        data.pop('password_confirmation')# elimina la validacion para no guardarla 
        user = User.objects.create_user(**data)
        profile = User_model(username=username)
        profile.save()


"""class ProfileForm(forms.Form): 
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
"""

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
