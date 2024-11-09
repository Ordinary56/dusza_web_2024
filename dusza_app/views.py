from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
import django.http as http
import django.contrib.auth as auth
from django.contrib.auth.hashers import make_password
from .forms import userForm
from .enums import RoleEnum
from .models import Category, ProgLangs, Team, User
# Create your views here.
# TODO: add more views

@csrf_protect
def login(request : http.HttpRequest) -> http.HttpResponse:
    request.user.clean()
    match(request.method):
        case "GET":
            form = userForm()
            return render(request, "dusza_app/login.html", {'form' : form})
        case "POST":
            form = userForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password'] 
                logged_in_user = auth.authenticate(request,username=username, password=password)
                print(username, password,logged_in_user)
                if logged_in_user == None:
                    return http.HttpResponseNotFound("Ilyen felhasználó nem létezik")
                auth.login(request, logged_in_user)

                #TODO: redirect to the corresponding URL page 
                match(logged_in_user.role):
                    case RoleEnum.TEAM:
                        return http.HttpResponseRedirect("/team")
                        pass
                    case RoleEnum.SCHOOL:
                        pass
                    case RoleEnum.ORGANIZER:
                        pass
                return http.HttpResponseBadRequest("Az űrlap nem helyes")
    return http.HttpResponseBadRequest("Érvénytelen kérés")


@csrf_protect
def register(request : http.HttpRequest) -> http.HttpResponse:
    match(request.method):
        case "GET":
            form = userForm()
            return render(request, "dusza_app/register.html", {'form' : form})
       

def index(request: http.HttpRequest) :
    return render(request, "dusza_app/index.html")
@login_required
def TeamView(request: http.HttpRequest) -> http.HttpResponse:
    team = Team.objects.filter(user=request.user).first()
    members = User.objects.all().filter(team=team).exclude(
        username=request.user.username)
    return render(request, "dusza_app/team.html", {'teams' : team, 'members' : members})

@login_required
def SchoolView(request: http. HttpRequest) -> http.HttpResponse:
    #type ingore
    return http.HttpResponse()

@login_required
def OrganizerView(request: http. HttpRequest) -> http.HttpResponse:
    user = request.user
    categories = Category.objects.get()
    progamming_languages = ProgLangs.objects.get()
    return render(request, "dusza_app/organizer.html", {'categories' : categories, 'programming_languages' : progamming_languages})

def modify(request: http.HttpRequest, source_type = "", id = 0) -> http.HttpResponse:
    return http.HttpResponse()

def csrf_failure(request: http. HttpRequest) -> http.HttpResponse:
    return http.HttpResponse()
