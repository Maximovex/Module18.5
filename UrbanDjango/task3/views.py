from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'third_task/index.html')

def store_render(request):
    return render(request,'third_task/store.html')

class bin_render(TemplateView):
    template_name = 'third_task/bin.html'