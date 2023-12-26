from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, Form
import random
from django.shortcuts import redirect


def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())


def candidateRegistrationForm(request):
    res = render(request, 'registration_form.html')
    return res


def candidateRegistration(request):
    Context = {}
    if request.method == "POST":
        username = request.POST['username']
        # check the username that already exits
        if len(Candidate.objects.filter(username=username)):
            userStatus = 1
            Context['userStatus'] = userStatus
            return render(request, 'registration_form.html', Context)
        else:
            candidate = Candidate()
            candidate.username = username
            candidate.password = request.POST['password']
            candidate.name = request.POST['name']
            candidate.save()
            userStatus = 2
    else:
        userStatus = 3
    Context['userStatus'] = userStatus
    return render(request, 'registration.html', Context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        candidate = Candidate.objects.filter(username=username, password=password)
        #     user = authenticate(request, username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return redirect('home')  # Replace 'home' with your desired redirect URL
        # return render(request, 'login.html')
        if len(candidate) == 0:
            loginError = "Invalid Username or Password"
            return render(request, 'login.html', {'loginError': loginError})
        else:
            request.session['username'] = candidate[0].username
            request.session['name'] = candidate[0].name
            return redirect('OTS:home')
    return render(request, 'login.html')


def candidateHome(request):
    if 'name' not in request.session.keys():
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def testpaper(request):

    if 'name' not in request.session.keys():
        res = HttpResponseRedirect('login')
    # fetch question from database
    n = int(request.get['n'])
    questions_pool = list(Question.object.all())
    random.shuffle(questions_pool)
    questions_list = questions_pool[:n]
    context = {"questions": questions_list}
    return render(request, 'test_paper.html', context)


def calculateTestResult(request):
    pass


def testResultHistroy(request):
    pass


def showTestResult(request):
    pass


def logOut(request):
    request.session.flush()
    return redirect('OTS:home')


def form_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        form = Form(name=name, email=email, phone=phone , message=message)
        form.save()
        n = 'Thank you for getting in touch! We appreciate you contacting us'
    return redirect('OTS:home')





     


        
