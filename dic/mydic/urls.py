from django.urls import path
from mydic import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:w_id>/detail', views.detail, name="detail")
]