from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect
import django.http as http
from .forms import userForm
from .enums import RoleEnum
from .models import User
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
                logged_in_user = User.objects.filter(Username=username, 
                                                  Password=password).first()
                if logged_in_user == None:
                    return http.HttpResponseNotFound("Ez a felhasználó nem létezik")
                request.session['user'] = logged_in_user
                #TODO: redirect to the corresponding URL page 
                match(logged_in_user.Role):
                    case RoleEnum.TEAM:
                        return http.HttpResponseRedirect("/team", logged_in_user)
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

def TeamView(request: http.HttpRequest) -> http.HttpResponse:
    user : User = request.session.get('user')
    if user == None:
        return http.HttpResponseServerError("Hibás felhasználó")
    return render(request, "dusza_app/team.html")