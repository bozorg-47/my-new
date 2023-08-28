from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def homepage(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_homepage.html')
    context = {
        'mymembers': mymembers,
  }
    return HttpResponse(template.render(context,request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
    
# def images(request):
#     template = loader.get_template('images.html')
#     return HttpResponse(template.render())

# def chat(request):
#     template = loader.get_template('chat.html')
#     return HttpResponse(template.render())

# def videos(request):
#     template = loader.get_template('videos.html')
#     return HttpResponse(template.render())

# def maps(request):
#     template = loader.get_template('maps.html')
#     return HttpResponse(template.render())