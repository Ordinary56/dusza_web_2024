from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import django.http as http
import django.contrib.auth as auth
from django.contrib.auth.hashers import make_password
from .forms import *
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
                    return http.HttpResponseNotFound("Hibás felhasználónév vagy jelszó")
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
    return http.HttpResponseBadRequest("Érvénytelen kérés")
       

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
    teams = Team.objects.all()
    schools = School.objects.all()
    return render(request, "dusza_app/organizer.html", {'categories' : categories, 'programming_languages' : progamming_languages, 'schools' : schools, 'teams' : teams})

@login_required
def modify(request: http.HttpRequest) -> http.HttpResponse:
    if not request.user:
        return http.HttpResponseForbidden("Erre a kérésre nem vagy jogosult")
    # data -> ?source_type=programming_language|category|team|school
    # &|id=requested_id|category=requested_category|language=requested_language
    data = request.GET.dict()
    obj = None
    form = None
    context = {
        'form' : form,
        'type' : lambda: type(form).__name__
    }
    match(data['source_type']):
        case "programming_language":
            obj = get_object_or_404(ProgLangs, language=data['language'])
            form = ProgLangForm(instance=obj)
        case "category":
            obj = get_object_or_404(Category, category=data['category'])
            form = CategoryForm(instance=obj)
        case "school":
            obj = get_object_or_404(School, id=data['id'])
            form = SchoolForm(instance=obj)
            pass
        case "team":
            obj = get_object_or_404(Team, id=data['id'])
            pass
        case _:
            return http.HttpResponseNotFound("A módosítani kívánt objektum nem található")
    context['form'] = form
    return render(request, "dusza_app/modify.html", context)

@login_required
def delete(request : http.HttpRequest, object_type: str, identifier : str) -> http.HttpResponse:
    user : User = request.user
    match(object_type):
        case "category":
            obj = get_object_or_404(Category, category=identifier)
            obj.delete()
            return redirect("organizer")
        case "programming_language":
            obj = get_object_or_404(ProgLangs, language=identifier)
            if Team.objects.contains(programming_language=obj):
                return http.HttpResponseNotAllowed("Ezt a nyelvet nem törölheted, mert ezzel a nyelvvel már regisztrált egy csapat")
            obj.delete()
            return redirect("organizer")
    return http.HttpResponseForbidden("Nem törölhetsz semmit ha nem vagy bejelentkezve")

@login_required
def create(request: http.HttpRequest, object_type:str, value: str) -> http.HttpResponse:
    match(object_type):
        case "programming_language":
            new_obj = ProgLangs.objects.create(language=value)
            return redirect("organizer")
        case "category":
            new_obj = Category.objects.create(category=value)
            return redirect("organizer")
        case "team":
            extracted_values = value.split('_')
            pass
        case "school":
            pass
        case _:
            return http.HttpResponseBadRequest()
    return http.HttpResponseForbidden("Nem hozhatsz létre semmit, mert nem vagy bejelentkezve")

@login_required
def export(request: http.HttpRequest) -> http.HttpResponse:
    
    return http.HttpResponse()

logout = lambda request : auth.logout(request) 
# TODO: make custom views for failures 
def csrf_failure(request: http. HttpRequest) -> http.HttpResponse:
    return http.HttpResponse("CSRF token érvénytelen vagy lejárt, kérlek frissítsd újra az oldalt")
