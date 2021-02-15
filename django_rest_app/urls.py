from django.urls import path 
# from django_rest_app.views import articlelist, articledetails
from django_rest_app.views import Articlelist, Articledetails

 
urlpatterns = [

    # path('articlelistapi/',articlelist,name='articlelist'),
    # path('articledetails/<int:pk>/', articledetails, name='articledetails'),
    path('articlelistapi/',Articlelist.as_view(),name='Articlelist'),
    path('articledetails/<int:id>/',Articledetails.as_view(),name='Articledetails'),



]