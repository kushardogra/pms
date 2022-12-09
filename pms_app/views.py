from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import player, coach, team
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("player")
        else:
            return redirect("signin")
            print("Wrong Password")
    else:
        return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password2, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        print('user created')
        return redirect("signin")
    else:
        return render(request, 'register.html')


# def home(request):
#     return render(request, 'player_profile.html.html')

def add_coach(request):
    if request.method == 'POST':
        coach_name = request.POST['coach_name']
        coach_age = request.POST['coach_age']
        coach_emailID = request.POST['coach_emailID']
        coach_mobileNum = request.POST['coach_mobileNum']
        coach_addressLine1 = request.POST['coach_addressLine1']
        coach_addressLine2 = request.POST['coach_addressLine2']
        coach_addressLine3 = request.POST['coach_addressLine3']
        coach_image = request.POST['coach_image']

        add_coach = coach.objects.create_coach(coach_name=coach_name, coach_age=coach_age,coach_emailID=coach_emailID,coach_mobileNum=coach_mobileNum,coach_addressLine1=coach_addressLine1, coach_addressLine2=coach_addressLine2, coach_addressLine3=coach_addressLine3, coach_image=coach_image)
        add_coach.save()
        return redirect('coach')
    else:
        return render (request, 'add_coach.html')


def add_player(request):
    return render(request,'add_player.html')

def add_team(request):
    return render(request,'add_team.html')

def team_profile(request):
    return render(request,'bulls_profile.html')

def coaches(request):
    return render(request,'coaches.html')

def player_profile(request):
    return render(request,'mj_profile.html')

def coach_profile(request):
    return render(request,'pj_profile.html')

def player(request):
    return render(request,'player_profile.html')

def team(request):
    return render(request,'teams.html')

def logout(request):
    auth.logout(request)
    return redirect("signin")