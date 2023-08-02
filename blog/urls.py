
from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.List.as_view(),name='starting_page'),
    path('posts/',views.Postview.as_view(),name='all_post'),
    path('posts/<slug:slug>/',views.Detail.as_view(),name='specific_post'),#posts/my-first-post/
    path('readlater/',views.Readlater.as_view(),name='readlater'),#posts/my-first-post/

]
