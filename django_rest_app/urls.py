from django.urls import path,include 
# from django_rest_app.views import articlelist, articledetails
# from django_rest_app.views import (Articlelist, Articledetails,genericArticleView,GenericArticleView)
from django_rest_app.views import GenericArticleView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', GenericArticleView, basename='article')
 
urlpatterns = [

    # path('articlelistapi/',articlelist,name='articlelist'),
    # path('articledetails/<int:pk>/', articledetails, name='articledetails'),
    # path('articlelistapi/',Articlelist.as_view(),name='Articlelist'),
    # path('articledetails/<int:id>/',Articledetails.as_view(),name='Articledetails'),
    # path('generic/article/',genericArticleView.as_view(),name='GenericArticleView'),
    # path('generic/article/<int:id>/',genericArticleView.as_view(),name='GenericArticleView'),
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>/', include(router.urls)),
]