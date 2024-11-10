from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
import django.http as http
import django.contrib.auth as auth
from django.contrib.auth.hashers import make_password
from .forms import CategoryForm, ProgLangForm, userForm
from .enums import RoleEnum
from .models import *
# Create your views here.
# TODO: add more views

@csrf_protect
def login(request : http.HttpRequest) -> http.HttpResponse:
    match(request.method):
        case "GET":
            form = userForm()
            return render(request, "dusza_app/login.html", {'form' : form})
        case "POST":
            form = userForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                logged_in_user = auth.authenticate(request, username=username, password=password)
                # Sajnos admint is be lehetne írni :(
                if logged_in_user == None or logged_in_user.is_superuser: #type: ignore
                    return http.HttpResponseNotFound("Ilyen felhasználó nem létezik")
                auth.login(request, logged_in_user)
                
                # MyPy itt hibát dob
                match(logged_in_user.role): #type: ignore
                    case RoleEnum.TEAM:
                        return http.HttpResponseRedirect("/team")
                    case RoleEnum.SCHOOL:
                        return http.HttpResponseRedirect("/school")
                        pass
                    case RoleEnum.ORGANIZER:
                        return http.HttpResponseRedirect("/organizer")
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
    logged_user : User = request.user
    team = Team.objects.filter(user=logged_user).first()
    members = User.objects.all().filter(team=team)
    return render(request, "dusza_app/team.html", {'teams' : team, 'members' : members})

@login_required
def SchoolView(request: http. HttpRequest) -> http.HttpResponse:
    logged_user : User = request.user # type: ignore
    teams = Team.objects.all().filter(school=logged_user.school)
    return render(request, "dusza_app/school.html", {'teams' : teams})

@login_required
def OrganizerView(request: http. HttpRequest) -> http.HttpResponse:
    user = request.user
    categories = Category.objects.all()
    progamming_languages = ProgLangs.objects.all()
    schools = School.objects.all()
    return render(request, "dusza_app/organizer.html", {'categories' : categories, 'programming_languages' : progamming_languages})

def modify(request: http.HttpRequest) -> http.HttpResponse:
    data = request.GET.dict()
    print(data)
    match(data['source_type']):
        case "programming_language":
            obj = get_object_or_404(ProgLangs, language=data['language'])
            proglang_form = ProgLangForm(instance=obj)
            return render(request, "dusza_app/modify.html", {'form' : proglang_form})
        case "category":
            obj = get_object_or_404(Category, category=data['category'])
            category_form = CategoryForm(instance=obj)
            return render(request, "dusza_app/modify.html", {'form' : category_form})
    return http.HttpResponseBadRequest("Érvénytelen kérés")


def logout(request: http.HttpRequest) -> None:
    logout(request)
# TODO: make custom views for failures 
def csrf_failure(request: http. HttpRequest) -> http.HttpResponse:
    return http.HttpResponse()
