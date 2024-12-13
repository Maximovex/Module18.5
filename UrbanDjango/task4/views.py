from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'fourth_task/index.html')

def store_render(request):
    context={'games': ["Atomic Heart", "Cyberpunk 2077"]}

    return render(request,'fourth_task/store.html',context=context)

class bin_render(TemplateView):
    template_name = 'fourth_task/bin.html'