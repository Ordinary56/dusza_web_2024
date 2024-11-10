from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict
from .forms import *
from .enums import RoleEnum
from .models import *
import django.http as http
import pandas as pd
import django.contrib.auth as auth
# Create your views here.
# TODO: add more views

def login(request : http.HttpRequest) -> http.HttpResponse:
    print(request.method)
    match(request.method):
        case "GET":
            form = UserForm()
            return render(request, "dusza_app/login.html", {'form' : form})
        case "POST":
            username = request.POST['username']
            password = request.POST['password']
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
                case RoleEnum.ORGANIZER:
                    return http.HttpResponseRedirect("/organizer")
    return http.HttpResponse("Érvénytelen kérés")

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
def delete(request : http.HttpRequest) -> http.HttpResponse:
    user : User = request.user
    data = request.GET.dict()
    match(data['source_type']):
        case "category":
            obj = get_object_or_404(Category, category=data['category'])
            obj.delete()
            return redirect("organizer")
        case "programming_language":
            obj = get_object_or_404(ProgLangs, language=data['language'])
            if Team.objects.all().contains(programming_language=obj):
                return http.HttpResponseNotAllowed("Ezt a nyelvet nem törölheted, mert ezzel a nyelvvel már regisztrált egy csapat")
            obj.delete()
            return redirect("organizer")
    return http.HttpResponseForbidden("Nem törölhetsz semmit, nem vagy bejelentkezve")

@login_required
def create(request: http.HttpRequest) -> http.HttpResponse:

    data = request.GET.dict()
    form = None
    context = {
        'create' : 1
    }
    if request.method == "POST":
        payload = request.POST.dict()
        print(request.POST)
        print(payload)
        match(list(payload)[1]):
            case "category":
                Category.objects.create(category=payload['category'])
            case "language":
                new_obj = ProgLangs.objects.create(language=payload['language'])
                print(new_obj)
                new_obj.save()
            case "school":
                User.objects.create(new_user)
                School.objects.create(form.cleaned_data[2:])
            case _:
                pass
        if(request.user.role == RoleEnum.ORGANIZER):
            return redirect("organizer")
        else:
            return redirect("school")
        
    elif request.method == "GET":
        match(data['source_type']):
            case "school":
                form = SchoolForm()
            case "category" :
                form = CategoryForm()
            case "programming_language":
                form = ProgLangForm()
            case "team":
                categories = tuple((index, category) for index,category in enumerate(Category.objects.all()))
                languages = tuple((index, lang) for index, lang in enumerate(ProgLangs.objects.all()))
                form = TeamForm(categories=categories, languages=languages)
        context['form'] = form
        context['type'] = type(form).__name__
        print(context)
        return render(request, "dusza_app/modify.html", context)
    return http.HttpResponseForbidden("Nem vagy bejelentkezve")

@login_required
def export(request: http.HttpRequest) -> http.HttpResponse:
    '''
    Az adott csapat adatait exportálja
    '''
    id = request.GET.get('id')
    if id:
        team = get_object_or_404(Team, id=int(id))
        df = pd.DataFrame([model_to_dict(team)])
        response = http.HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = f"attachment; filename={team.team_name}_data.xlsx"
        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Data')
        return response
    return http.HttpResponse()

# TODO: make custom views for failures 
def csrf_failure(request: http. HttpRequest) -> http.HttpResponse:
    return http.HttpResponse("CSRF token érvénytelen vagy lejárt, kérlek frissítsd újra az oldalt")
