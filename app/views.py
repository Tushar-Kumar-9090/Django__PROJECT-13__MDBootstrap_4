from django.shortcuts import render

# Create your views here.

def md_bootstrap(request):
    return render(request, 'md_bootstrap.html')


def md_bootstrap_courosal(request):
    return render(request, 'md_bootstrap_courosal.html')