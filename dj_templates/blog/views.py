from django.shortcuts import render
from django.views import generic
from blog.models import Post
# Create your views here.

#
# def home(request):
#     return render(request,'index.html',{})
#

class Index(generic.ListView):
    template_name = 'index.html'
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.order_by("-created_at")


class Show(generic.DeleteView):
    model = Post
    context_object_name = "post"
    template_name = "show.html"