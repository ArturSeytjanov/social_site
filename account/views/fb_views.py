from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from ..forms import LoginForm
from django.contrib.auth.decorators import login_required
from ..forms import UserRegistrationForm

# TIPS
def user_login(request):
    # Пойск выполнено POST
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request=request, 
                username=cd['username'], 
                password=cd['password']
            )
            # Успех 
            if user is not None:
                if user.is_active:
                    login(request=request, user=user)
                    return HttpResponse('Вы вошли успешно в страницу')
            
            # Не найден
            else:
                return HttpResponse('Аккаунт не найден')
        # неправильный доступ
        else:
            return HttpResponse('неправильный ник или пароль    ')
    
    # Поиск как GET
    else:
        form = LoginForm()
    
    context = {
        'form':form
    }

    return render(request=request, template_name='account/login.html', context=context)

@login_required
def dashboard(request):
    context = {
        'section': 'dashboard'
    }
    return render(
        request=request,
        template_name='account/dashboard.html', 
        context=context
    )

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создать новый обьект пользователя, но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
                user_form.cleaned_data['password2']
            )
            # Сохранить обьект
            new_user.save()

            context = {
                'new_user':new_user
            }

            return render(
                request=request,
                template_name='account/register_done.html',
                context=context
            )

    else:
        user_form = UserRegistrationForm()


    context = {
        'user_form':user_form
    }

    return render(
        request=request,
        template_name='account/register.html',
        context=context
    )