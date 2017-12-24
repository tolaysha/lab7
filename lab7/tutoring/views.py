from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from datetime import datetime
from tutoring.models import Education, Subjects, Regions, Tutors
from tutoring.registration import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


class OrdersView(View):
    def get(self, request):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', locals())


class OrderView(View):
    def get(self, request, id):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', locals())


def main(request):
    return render(request, 'main.html', locals())


def prog_lang(request, prog_lang):
    name = ['C++', 'Python', 'Java']
    cpp_info = 'C++ — компилируемый, статически типизированный язык программирования общего назначения. Синтаксис C++ унаследован от языка C. Одним из принципов разработки было сохранение совместимости с C. Тем не менее, C++ не является в строгом смысле надмножеством C; множество программ, которые могут одинаково успешно транслироваться как компиляторами C, так и компиляторами C++, довольно велико, но не включает все возможные программы на C.'
    java_info = 'Java — сильно типизированный объектно-ориентированный язык программирования, разработанный компанией Sun Microsystems (в последующем приобретённой компанией Oracle). Приложения Java обычно транслируются в специальный байт-код, поэтому они могут работать на любой компьютерной архитектуре, с помощью виртуальной Java-машины. Дата официального выпуска — 23 мая 1995 года.'
    python_info = 'Python — высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. Синтаксис ядра Python минималистичен. В то же время стандартная библиотека включает большой объём полезных функций.'
    info = [cpp_info, java_info, python_info]
    data1 = {'lang': {'id': prog_lang}}
    data2 = {'langs': [{'id': 'cpp', 'lang_name': 'C++', 'info': cpp_info},
                       {'id': 'java', 'lang_name': 'Java', 'info': java_info},
                       {'id': 'python', 'lang_name': 'Python', 'info': python_info}]}
    return render(request, 'prog_lang.html', locals())


def db(request):
    return render(request, 'db.html', locals())


class UniversitiesList(ListView):
    model = Education
    template_name = "universities.html"


class SubjectsList(ListView):
    model = Subjects
    template_name = "subjects.html"


class RegionsList(ListView):
    model = Regions
    template_name = "regions.html"


class TutorsList(ListView):
    model = Tutors
    template_name = "tutors.html"


def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success/')
        else:
            error = "Пользователь не найден"
    return render(request, 'login.html', locals())


@login_required()
def success(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'success.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            # ...
            return HttpResponseRedirect('/login/')
        else:
            form = RegistrationForm()
    return render(request, 'registration2.html', {'form': form})
