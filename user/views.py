from django.shortcuts import render

# Create your views here.
def login(request):
    template_name = 'user/login_page.html'
    return render(request,template_name)