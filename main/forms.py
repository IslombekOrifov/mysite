from django import forms

from .models import UserLetter


class UserLetterForm(forms.ModelForm):
    
    class Meta:
        model = UserLetter
        fields = "__all__"
        widgets = {
            'body': forms.Textarea(attrs={"rows":7, "cols":10}),
        }
        