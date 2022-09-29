import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from todolist.forms import TaskForm
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user.get_username()
    # Mengambil seluruh task sesuai user ter-login saat ini
    tasks = Task.objects.filter(user=request.user)
    context = {
        'username': username,
        'tasks': tasks,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    # Jika method request adalah POST
    if request.method == 'POST':
        # Mengambil data form dari request
        form = TaskForm(request.POST)
        # Mengecek validitas form
        if form.is_valid():
            # Menyusun data dari form ke model Task
            task = Task(
                user = request.user,
                date = datetime.datetime.now(),
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
            )
            # Menyimpan instansiasi task ke database
            task.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            # Kembali ke halaman awal todolist
            return redirect('todolist:show_todolist')

    # Jika method request adalah GET atau lainnya
    else:
        form = TaskForm()
    # Menampilkan halaman create task
    context = {'form':form}
    return render(request, "create_task.html", context)

def register(request):
    # Membuat form registrasi user
    form = UserCreationForm()
    # Jika request method POST (tombol input daftar akun ditekan)
    if request.method == "POST":
        # Menyusun form berdasarkan input pengguna
        form = UserCreationForm(request.POST)
        # Mengecek validitas form
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    # Jika request method POST (tombol input login ditekan)
    if request.method == 'POST':
        # Mengautentikasi user dengan username dan password
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # Jika user ditemukan (username dan password salah)
        if user is not None:
            # Melakukan login
            login(request, user)
            # Membuat response redirect halaman utama
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            # Membuat cookies berisi data last login
            response.set_cookie('last_login', str(datetime.datetime.now()))
            # Mengembalikan response
            return response
        # Jika user tidak ditemukan
        else:
            messages.info(request, 'Username atau Password salah!')
    # Mencetak halaman login
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    # Melakukan logout dan redirect ke halaman login
    logout(request)
    return redirect('todolist:login')
