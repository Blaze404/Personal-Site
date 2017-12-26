from django.shortcuts import render, reverse
from . models import Projects
from django.views.generic.edit import CreateView
from .models import Projects

# Create your views here.
def homepage(request):
    all_projects = Projects.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'psite/blaze.html', context)


class AddProject(CreateView):
    model = Projects
    fields = ['title', 'description', 'resources_used', 'repo', 'cover']

    def get_success_url(self):
        return reverse('psite:homepage')