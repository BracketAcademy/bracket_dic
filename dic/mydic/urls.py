from django.urls import path
from mydic import views
app_name = 'mydic'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:w_id>/', views.detail, name="detail"),
    path('form', views.form, name="form"),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutuser, name='logoutuser'),
    path('about', views.aboutus, name='about'),
    path('list', views.list, name='list')
]
