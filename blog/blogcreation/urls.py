from django.urls import path
from.import views

urlpatterns = [
    path('base/',views.base,name="base"),
    path('bloglist/',views.bloglist,name="bloglist"),
    path('create_blog/',views.create_blog,name="blogcreate"),
]