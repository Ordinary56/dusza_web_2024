from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.decorators import login_required
import django.http as http
import django.contrib.auth as auth
from .forms import userForm
from .enums import RoleEnum
from .models import Team, User
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

                logged_in_user: User|None = auth.authenticate(Username=username, Password=password)
                if logged_in_user == None or logged_in_user.is_superuser:
                    return http.HttpResponseNotFound("Ilyen felhasználó nem létezik")
                auth.login(request, logged_in_user)

                #TODO: redirect to the corresponding URL page 
                match(logged_in_user.Role):
                    case RoleEnum.TEAM:
                        return http.HttpResponseRedirect("/team")
                        pass
                    case RoleEnum.SCHOOL:
                        pass
                    case RoleEnum.ORGANIZER:
                        pass
                return http.HttpResponseBadRequest("Az űrlap nem helyes")
    return http.HttpResponseBadRequest("Érvénytelen kérés")

def index(request: http.HttpRequest) :
    return render(request, "dusza_app/index.html")
def register(request: http.HttpRequest) :
    return render(request, "dusza_app/register.html")

@login_required
def TeamView(request: http.HttpRequest) -> http.HttpResponse:
    return render(request, "dusza_app/team.html")

def SchoolView(request: http. HttpRequest) -> http.HttpResponse:
    #type ingore
    return http.HttpResponse()

def OrganizerView(request: http. HttpRequest) -> http.HttpResponse:
    user : User|None = request.session.get('user')
    return http.HttpResponse()


def csrf_failure(request: http. HttpRequest) -> http.HttpResponse:
    return http.HttpResponse()
