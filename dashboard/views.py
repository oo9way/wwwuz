from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app.models import Website
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http.response import HttpResponseNotFound
from django.contrib import messages
from dashboard.forms import WebsiteForm
from django.utils.translation import gettext as _


@login_required(login_url='/users/sign-in/')
def dashboard(request):
    data = Website.objects.filter(owner=request.user).order_by('-created_at')
    data = Paginator(data, 10)
    
    page = request.GET.get('page', 1)

    try:
        rows = data.page(page)
    except PageNotAnInteger:
        rows = data.page(1)
    except EmptyPage:
        rows = data.page(data.num_pages)

    return render(request, 'dashboard.html', {'rows':rows})


@login_required(login_url='/users/sign-in/')
def website_view(request, pk):
    try:
        website = Website.objects.get(id=pk, owner=request.user)
    except:
        return HttpResponseNotFound()
    
    return render(request, 'website_details.html', {'website':website})


@login_required(login_url='/users/sign-in/')
def website_delete(request, pk):
    try:
        website = Website.objects.get(id=pk, owner=request.user)
    except:
        return HttpResponseNotFound()
    
    if request.method == "POST":
        try:
            obj = Website.objects.get(id=request.POST['website_id'], owner=request.user)
        except:
            messages.error(request, _("Object not found"), extra_tags='danger')
            return redirect(reverse('dashboard:home'))
        
        obj.delete()
        messages.info(request, _("Website is deleted"))
        return redirect(reverse('dashboard:home'))
    
    return render(request, 'website_delete.html', {'website':website})


@login_required(login_url='/users/sign-in/')
def website_edit(request, pk):
    try:
        website = Website.objects.get(id=pk, owner=request.user)
    except:
        return HttpResponseNotFound()
    
    form = WebsiteForm(instance=website)

    if request.method == "POST":
        form = WebsiteForm(instance=website, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Website edited successfuly'))
            return redirect(reverse('dashboard:home'))
        
        messages.error(request, f'{form.errors}', extra_tags='danger')
        return redirect(reverse('dashboard:home'))
        

    return render(request, 'website_edit.html', {'website':website, 'form':form})


@login_required(login_url='/users/sign-in/')
def website_create(request):
    form = WebsiteForm()

    if request.method == "POST":
        form = WebsiteForm(request.POST)

        if form.is_valid():
            website = form.save(commit=False)
            website.owner = request.user
            website.save()

            messages.success(request, _("Added new website"))
            return redirect(reverse('dashboard:home'))
        
        messages.error(request, _("Something went wrong"), extra_tags='danger')

    return render(request, 'website_create.html', {'form':form})