from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Information
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required

def information_list(request):
    qs = Information.objects.all()

    titles = request.GET.get('srchTitle', '')
    if titles:
        condition = Q(title__icontains=titles) | Q(contents__icontains=titles)
        qs = qs.filter(condition)
    
    paginator = Paginator(qs, 4)
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)
    return render(request, 'information/information_list.html', {
        'information_list': qs,
        'titles': titles,
    })

@login_required
def information_detail(request, pk):
    information = Information.objects.get(pk=pk)
    return render(request, 'information/information_detail.html', {
        'information': information,
    })

@login_required
def information_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            information = form.save()
            return redirect(information)
    else:
        form = PostModelForm()

    return render(request, 'information/information_form.html', {
        'form': form,
    })

@login_required
def information_edit(request, pk):
    information = Information.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=information)
        if form.is_valid():
            information = form.save()
            return redirect(information)
    else:
        form = PostModelForm(instance=information)

    return render(request, 'information/information_form.html', {
        'form': form,
    })
