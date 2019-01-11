from django import forms
from .models import Book
from django.utils.text import slugify
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'slug',
            'description',
            'publisher'
        ]
    def unique_title(self):
        title = self.cleaned_data["title"]
        slug = slugify(title)
        try:
            book = Book.objects.get(slug=slug)
            raise forms.ValidationError("Title already exists")
        except Book.DoesNotExist:
            return title
        except:
            raise forms.ValidationError("Title already exists")


class SearchField(forms.Form):
    search = forms.CharField
