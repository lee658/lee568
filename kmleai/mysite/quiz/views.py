from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Quiz
from .forms import PostModelForm
from django.contrib.auth.decorators import login_required

def quiz_list(request):
    qs = Quiz.objects.all()
    
    
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
        
    return render(request, 'quiz/quiz_list.html', {
        'quiz_list': qs,
        'titles': titles,
    })

@login_required
def quiz_detail(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz_detail.html', {
        'quiz': quiz,
    })

@login_required
def quiz_new(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            quiz = form.save()
            return redirect(quiz)
    else:
        form = PostModelForm()

    return render(request, 'quiz/quiz_form.html', {
        'form': form,
    })

@login_required
def quiz_edit(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=quiz)
        if form.is_valid():
            quiz = form.save()
            return redirect(quiz) 
    else:
        form = PostModelForm(instance=quiz)
    return render(request, 'quiz/quiz_form.html', {
        'form': form,
    })

