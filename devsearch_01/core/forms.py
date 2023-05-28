from django import forms

class UserDetailForm(forms.Form):
    name = forms.CharField(max_length=250, help_text="The name of the user", required=False)
    title = forms.CharField(max_length=250, help_text="Proffesional job's title", required=False)
    about = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), required=False)
    profile_image = forms.ImageField(required=False)
    location = forms.CharField(max_length=250, required=False)