from django.urls import path, include,re_path
from .views import BookDetail,BookList, show_view

urlpatterns = [
    path('', BookList.as_view()),
    path('<slug:slug>/', BookDetail.as_view()),
]
