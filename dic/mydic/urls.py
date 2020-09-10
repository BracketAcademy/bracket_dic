from django.urls import path
from mydic import views
app_name='midic'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:w_id>/', views.detail, name="detail")
]