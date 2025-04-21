from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Profile
from .models import Quiz, Category
from django.db.models import Q


# Create your views here.
@login_required(login_url = 'login')
def all_quiz_view(request) :

    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)

    quizzes = Quiz.objects.order_by('-created_at')
    categories = Category.objects.order_by('name')


    context = {"user_profile" : user_profile , "quizzes" : quizzes, "categories" : categories}
    return render(request, 'all-quiz.html' , context)

@login_required(login_url = 'login')
def search_view(request, category):

    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)

    #search by Categ
    if request.GET.get('q') != None :
        q = request.GET.get('q')
        query = Q(title__icontains = q) | Q(description__icontains = q)
        quizzes = Quiz.objects.filter(query).order_by('-created_at')
    elif category != " " :
        quizzes = Quiz.objects.filter(category__name = category).order_by('-created_at')
    else :
        quizzes = Quiz.objects.order_by('-created_at')
    
    categories = Category.objects.all()

    context = {"user_profile" : user_profile , "quizzes" : quizzes, "categories" : categories}
    return render (request, 'all-quiz.html', context)

@login_required(login_url='login')
def quiz_view(request, quiz_id) :  
    
    user_object = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user_object)

    if request.method == "POST" :
        print("POST METHOD")
        pass

    quiz = Quiz.objects.filter(id = quiz_id).first()
    if quiz != None :
        context = {"user_profile" : user_profile , "quiz" : quiz}
    else :
        return redirect('all_quiz')

    # context = {"user_profile" : user_profile}
    return render(request , 'quiz.html' , context)