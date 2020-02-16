from django.urls import path

from . import views

app_name = 'simple_bee'
urlpatterns = [
    # /simple_bee/
    path('', views.index, name='index'),
    # /simple_bee/1/
    path('<int:bee_robot_id>/', views.detail, name='detail'),
    # /simple_bee/register/
    path('register/', views.register, name='register'),
    # /simple_bee/register_confirm/
    path('register_confirm/', views.register_confirm, name='register_confirm'),
    # /simple_bee/1/decommission/
    path('<int:bee_robot_id>/decommission/', views.decommission, name='decommission'),
    # /simple_bee/1/delete/
    path('<int:bee_robot_id>/delete/', views.delete, name='delete'),
    # /simple_bee/1/put/
    path('<int:bee_robot_id>/put/', views.put, name='put'),
    # /simple_bee/random/
    path('random/', views.random, name='random'),
    # /simple_bee/1/get/
    path('<int:bee_robot_id>/get/', views.get, name='get')

]