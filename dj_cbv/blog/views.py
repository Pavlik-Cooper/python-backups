from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin, ContextMixin
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



class LoginRequiredMixin:
    # @classmethod
    # def as_view(cls,**kwargs):
    #   view =  super().as_view(**kwargs)
    #   return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AboutTamplateView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['title'] = "This is about us"
        return context


class MyView(TemplateResponseMixin, ContextMixin, View):
    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = "This is my custom view"
        return self.render_to_response(context)
        # return HttpResponse('Hello, World!')

    # @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return HttpResponse("post")

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)