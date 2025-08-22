
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index, name="index"),
    path('delete-transaction/<id>/', views.delete_transaction , name="delete_transaction"),
    path('logout/',views.logout_view,name='logout-view'),
    path('login/',views.login_view,name="login-view"),
    path("register/",views.register_view,name="register-view"),
]
