from django.urls import path
from django.views.generic import TemplateView
from devsearch_01.core import views

app_name='core'
urlpatterns = [

    path("account/<int:pk>/", views.account_detail, name="account"),
    path("project/", TemplateView.as_view(template_name="pages/project.html"), name="project"), 
    
]
