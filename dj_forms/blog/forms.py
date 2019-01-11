from django import forms
from django.utils import timezone
from .models import Post

class PostModelForm(forms.ModelForm):
    title = forms.CharField(min_length=2)
    class Meta:
        model = Post
        fields = ['content', 'image','height_field','width_field','draft']
        labels = {'title': "Cheesy title"}
        help_texts = {'content': 'Help text: Be brief, please'}
        error_messages = {
            "title": {
                'required':"Hands up!",
                'min_length':'Min len'
            }
        }
        # exclude

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.Textarea()
        self.fields['content'].required = True

        # print(self.fields)

        for field in self.fields:
            self.fields[field].error_messages = {
                "required": f"You know, {field} is required"
            }


    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.publish = timezone.now()
        if commit:
            obj.save()
        return obj


choices = [
    ("bronze","Bronze"),
    ("silver","Silver"),
    ("gold", "Gold"),
]
years = [y for y in range(1995,2013)]

class TestForm(forms.Form):
    title = forms.CharField(strip=True,min_length=2, max_length=15, required=True)
    description = forms.CharField(label="Short desc",initial="Foobar")
    featured = forms.BooleanField(initial=True)
    stock = forms.IntegerField(min_value=1,max_value=15,error_messages={'min_value':"Hands up!","max_value":"Stop it!"})
    # RadioSelect don't work with crispy
    # types = forms.CharField(widget=forms.RadioSelect(choices=choices))
    # types = forms.CharField(widget=forms.Select(choices=choices))
    types = forms.ChoiceField(choices=choices)
    date = forms.DateField(widget=forms.SelectDateWidget(years=years),initial="1999-04-10")
    year = forms.IntegerField(widget=forms.Select(choices=[(x,x) for x in range(1999, 2013)]))

    def __init__(self,user=None, *args,**kwargs):
        super().__init__(*args,**kwargs)
        if user:
            if str(user) != "AnonymousUser":
                self.fields['title'].initial = user.username
            else:
                self.fields['title'].initial = user

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 2:
            raise forms.ValidationError("Description should be more than 1 char")
        return description

