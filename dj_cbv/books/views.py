from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView,ListView, CreateView, DeleteView, UpdateView
# Create your views here.
from .models import Book, Publisher
from .forms import BookForm
from django.http import Http404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import BaseUpdateView,ModelFormMixin
from django.urls import reverse


class MultipleObjectsErrorHandler:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectsReturned:
                obj = self.model.objects.filter(slug=slug)[0]
            return obj
        raise Http404


class BookDetail(MultipleObjectsErrorHandler,BaseUpdateView, DetailView):
    model = Book
    template_name = 'show.html'
    form_class = BookForm

    # the code below can be used with ModelFormMixin
    # def post(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #         self.object = self.get_object()
    #         form = self.get_form()
    #         if form.is_valid():
    #             return self.form_valid(form)
    #         else:
    #             return self.form_invalid(form)
    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["button_title"] = "Update"
        print(context)
        return context



class BookList(ListView):
    model = Book
    template_name = "_index.html"
    context_object_name = 'books'
    queryset = Book.objects.order_by("created_at")
    publisher = None

    def get_queryset(self):
        if self.kwargs.get('publisher',None):
            self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
            self.queryset = Book.objects.filter(publisher=self.publisher)

        return self.queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.publisher:
            context['publisher'] = self.publisher
        print(context)
        return context


class BookCreate(CreateView):
    model = Book
    template_name = "create.html"
    # fields = ['title','description']
    # success_url = "/books"
    form_class = BookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_title"] = "Create"
        print(context)
        return context

    def form_valid(self, form):
        print(form)
        print(form.instance)
        form.instance.author = self.request.user
        messages.success(self.request,f"{form.instance.title} was created")
        return super().form_valid(form)
    #
    # def get_success_url(self):
    #     return reverse('books.index')


class BookUpdate(MultipleObjectsErrorHandler, SuccessMessageMixin,UpdateView):
    model = Book
    template_name = "update.html"
    form_class = BookForm
    # success_url = "/books"
    success_message = "%(title)s was created at %(created_at)s"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["button_title"] = "Update"
        print(context)
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            created_at=self.object.created_at,
        )


class BookDelete(MultipleObjectsErrorHandler,DeleteView):
    model = Book
    template_name = "delete.html"
    # success_url = "/books"

    def get_success_url(self):
        messages.info(self.request, f"{self.object.title} was deleted")
        return "/books"