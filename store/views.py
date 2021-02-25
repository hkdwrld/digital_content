from django.shortcuts import render
from django.http import HttpResponse
from .models import Picture
from taggit.managers import TaggableManager
from django.http import JsonResponse
from taggit.models import Tag

# Create your views here.


def home(request):
    template_name = 'store/index.html'
    pictures = Picture.objects.all().order_by('-date_uploaded')
    context = {
        'pictures': pictures
    }
    return render(request, template_name, context)


def auto_complete(request):
    if 'term' in request.GET:
        qs = Tag.objects.filter(name__istartswith=request.GET.get('term'))
        tags=list()
        for tag in qs:
            tags.append(tag.name)
        return JsonResponse(tags,safe=False)
