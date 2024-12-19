from django.shortcuts import render
from django.http import HttpResponse
from django import forms

users=['andrew',"urban",'wizard','superadmin']
info={}

class UserRegister(forms.Form):
    username=forms.CharField(max_length=30, label='Логин')
    password=forms.CharField(widget=forms.PasswordInput(),min_length=8,label='Пароль')
    confirm_password=forms.CharField(widget=forms.PasswordInput(),min_length=8,label='Повторите пароль')
    age=forms.IntegerField(max_value=199,min_value=18,label='Возраст')

def check_user(username,password,repeat_password,age):
    is_ok=True

    if username.lower() in users:
        info['error']= 'Пользователь уже существует'
        is_ok=False
    if int(age)<=18:
        info['error']='Возраст должен быть больше 18 лет'
        is_ok=False
    if password!=repeat_password:
        info['error']='Пароли должны совпадать'
        is_ok=False
    return is_ok

def sign_up_by_django(request):
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            chk_password=form.cleaned_data['confirm_password']
            age=form.cleaned_data['age']
            if not check_user(username,password,chk_password,age):
                return render(request,'fifth_task/django_sign_up.html',info)
            else:
                return HttpResponse(f'Приветствуем {username}, {age} лет!')
    else:
        info['form']=UserRegister()
    return render(request,'fifth_task/django_sign_up.html',context=info)

def sign_up_by_html(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        chk_password=request.POST.get('confirm_password')
        age=request.POST.get('age')
        if not check_user(username,password,chk_password,age):
            return render(request,'fifth_task/registration_page.html',info)
        else:
            return HttpResponse(f'Приветствуем {username}, {age} лет!')
    return render(request,'fifth_task/registration_page.html',context=info)
