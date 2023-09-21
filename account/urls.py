from django.urls import path 
from .views import fb_views
from .views import cb_views
from django.contrib.auth import views as auth_views 
from django.urls import include
from .views.fb_views import register


urlpatterns = [
    # Predidushiy
    #path(route='login/',view=views.user_login, name='login'),
    
    #url - адреса для входа,выхода, сброс и т.д
    path(route='', view=include('django.contrib.auth.urls')),

    # регистрация
    path(route='register/',view=register, name='register'),

    # Главная страница
    path(route='', view=fb_views.dashboard, name='dashboard'),
    
]

#Детальный образ (django.contrib.auth)

# tobedegi yamasa tomendegi ekewi birzat ekewinda qollaniwga boladi
'''
    #url-adres dlya vxoda (Django)
    path(route='login/',view=cb_views.CustomLoginView.as_view(), name='login'),
    path(route='logout/',view=auth_views.LogoutView.as_view(), name='logout'),

    # url-адреса для смены пароля
    path(route='password-change/',view=auth_views.PasswordChangeView.as_view(), name='password_change'),
    path(route='password-change/done/',view=auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # url-адреса для сброса пароля 
    path(route='password-reset/',view=auth_views.PasswordResetView.as_view(), name='password_reset'),
    path(route='password-reset/done/',view=auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(route='password-reset/<uidb64>/<token>/',view=auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(route='password-reset/complete/',view=auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
'''
