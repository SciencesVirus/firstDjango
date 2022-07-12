from django.urls import path
from account import views
from article.urls import app_name, urlpatterns

app_name = 'account'
urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout')
]