"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    """First page of a form that creates a task"""

    class Meta:
        """Form options."""
        model = Thing
        fields = ['name', 'description', 'quantity']

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "maxlength": 35}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "maxlength": 120}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    def __init__(self, **kwargs):
        """Construct a new form instance with a user instance."""

        super().__init__(**kwargs)

    def clean(self):
        """Clean the deadline datatime data and generate messages for any errors."""

        super().clean()
