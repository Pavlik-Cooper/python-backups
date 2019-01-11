"""dj_cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from blog.views import AboutTamplateView, MyView
from books.views import BookDetail,BookList, BookCreate,BookUpdate,BookDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about/', TemplateView.as_view(template_name='about.html')),
    path('about/', MyView.as_view(template_name='about.html')),

    path('books/', BookList.as_view(),name="books.index"),
    path('books/create/', BookCreate.as_view()),
    path('books/<slug:slug>/update/', BookUpdate.as_view()),
    path('books/<slug:slug>/delete/', BookDelete.as_view(),name="books.delete"),
    path('books/<slug:slug>/', BookDetail.as_view(), name="book_detail"),
    path('books/publishers/<publisher>/', BookList.as_view()),
    # re_path(r'^books/$', BookList.as_view()),
    # re_path(r'^books/(?P<slug>[\w-]+)/$', BookDetail.as_view()),
]
