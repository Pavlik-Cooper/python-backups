# from functools import reduce
from django.shortcuts import render,redirect
from django.utils.text import slugify
from django.forms import formset_factory,modelformset_factory
from .forms import TestForm, PostModelForm
# Create your views here.
from .models import Post


#TODO formsets with Jquery, iteritems, reduce

def model_form(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    if form.has_error:
        # print(dir(form))
        # print(form.errors.as_json())
        # print(form.errors.as_text())
        errors = form.errors.items()
        for k, v in errors:
            # print(v.as_text())
            print(v.as_json())
            # print(v.get_json_data())
            # print(dir(v))

    return render(request, 'blog_index.html', {'form':form})


def model_formset(request):
    PostFormSet = modelformset_factory(Post, fields=['title','slug','image'],extra=2)
    form_set = PostFormSet(request.POST or None)
    if form_set.is_valid():
        # form_set.save()
        for form in form_set:
            # print(form.cleaned_data)
            obj = form.save(commit=False)
            if form.cleaned_data.get('title'):
                obj.slug = slugify(form.cleaned_data.get('title'))
                obj.save()
        return redirect('/model-formset')

    return render(request, 'model_formset_view.html', {'formset': form_set})


def formset(request):
    TestFormSet = formset_factory(TestForm,extra=2)
    form_set = TestFormSet(request.POST or None)
    if form_set.is_valid():
        for form in form_set:
            print(form.cleaned_data)

    return render(request,'formset_view.html', {'formset': form_set})



def test_form(request):
    defaults = {
        'description': 'Def desc',
        'stock': 5
    }
    form = TestForm(data=request.POST or None,initial=defaults)

    if request.method == "POST":
        print(request.POST)
        form = TestForm(data=request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)

    if request.method == "GET":
        form = TestForm(user=request.user,initial=defaults)

    return render(request,'test_form.html',{"form":form})