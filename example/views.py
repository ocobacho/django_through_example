
from django.shortcuts import render
from .models import Company
# Create your views here.
def index_view(request):

    company, created = Company.objects.get_or_create(name="Company 1")
    company2, created2 = Company.objects.get_or_create(name="Company 2")
    company.groups.get_or_create(name="group 1")
    company.groups.get_or_create(name="group 2")
    company2.groups.get_or_create(name="group 3")

    queryset = Company.groups.through.objects.all().order_by('-id')

    context = {
        "queryset": queryset
    }

    return render(request, 'example/index.html', context)