from django import forms
from devsearch_01.core.models import Project, Image

class UserDetailForm(forms.Form):
    name = forms.CharField(max_length=250, help_text="The name of the user", required=False)
    title = forms.CharField(max_length=250, help_text="Proffesional job's title", required=False)
    about = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), required=False)
    profile_image = forms.ImageField(required=False)
    location = forms.CharField(max_length=250, required=False)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('image_project', 'title', 'about', 'link', )

    def save(self, commit=True):
        project = super().save(commit=False)

        # Check if no images were submitted
        if not self.cleaned_data['image_project']:
            # Create a default image and attach it to the project
            project.image_project.clear()

            default_image = Image.objects.create()
            project.image_project.add(default_image)

        
        project = super().save(commit=True)
        
        return project
