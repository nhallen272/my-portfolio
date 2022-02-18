from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Subscriber, Project
from .forms import ContactForm, SubscribeForm
from django.core.mail import BadHeaderError, send_mail

MIN_PK = 1

# Create your views here.
def index(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = Subscriber(email=form.cleaned_data["email"])
            subscriber.save()

    projects = Project.objects.all().order_by('-created_on')
    context = {'projects': projects, 'form':form}
    return render(request, 'index.html', context)

def about(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subscriber = Subscriber(email=form.cleaned_data["email"])
            subscriber.save()

    context = {"form":form}
    return render(request, 'about.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            from_email = form.cleaned_data["email"]            
            body = form.cleaned_data["body"]
            # send email to me
            send_mail(
            'Message from ' + name,
            body,
            from_email,
            'nh.allen272@gmail.com',
            fail_silently=False,
            )
    context = {'form': form}
    return render(request, 'contact.html', context)


def project_index(request):  #add a page number parameter
    projects = Project.objects.all().order_by('-created_on')
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context) 


# load a specific page of a project
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    prev_pk = pk - 1
    next_pk = pk + 1
    max_p = Project.objects.all().count()  

    if prev_pk < 1:
        prev_pk = 1
    
    if next_pk > max_p:
        next_pk = 1
        
    context = {'project': project, 
               'max_p': max_p,
               'next_pk':next_pk,
               'prev_pk':prev_pk} 
    return render(request, 'project_detail.html', context)


# display all projects with the specified category argument
def project_category(request, cat):
    projects = Project.objects.filter(categories__title__contains=cat).order_by('-created_on')
    context = {'projects': projects, 
               'cat': cat}
    return render(request, 'project_category.html', context)
