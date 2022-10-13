# Tugas 4 PBP

Daffa Ilham Restupratama <br>
NPM 2106751013 <br>
Kelas PBP B <br>

## Tautan Deploy

- [Halaman Todolist](https://daffailham.herokuapp.com/todolist)

<br>

## Kegunaan ```{% csrf_token %}``` Pada Elemen ```<form>```

Token yang di-*generate* oleh ```{% csrf_token %}``` berguna untuk keamanan dan autentikasi pengguna yang ingin melakukan submisi di dalam form. Token tersebut bersifat unik untuk setiap user di setiap *session*. Dengan adanya token tersebut, orang yang berusaha meretas, menyusupi, atau mengubah data tidak akan dapat melakukannya dengan mudah sebab adanya verifikasi token yang selalu bersifat unik dan acak tersebut. Sistem autentikasi token CSRF ini diimplementasikan dengan memasukkan potongan kode ```{% csrf_token %}``` pada file HTML yang menampilkan submisi form. 

<br>

## Elemen ```<form>``` Manual Tanpa Generator

Membuat kolom masukan pada halaman web tetap bisa dilakukan tanpa generator Form. Ada beberapa cara yang dapat dilakukan untuk mengimplementasikan fitur tersebut, salah satunya menggunakan tag form bawaan HTML. Contoh implementasi dua kolom submisi teks beserta tombol submit bisa berupa kode seperti berikut ini :

```html
<form action="<nama action>" method="<nama method>">
    <label for="kolom1">Isian pertama :</label><br>
    <input type="text" id="kolom1" name="kolom1"><br>
    <label for="kolom2">Isian kedua :</label><br>
    <input type="text" id="kolom2" name="kolom2"><br>
    <button type="submit">Submit</button>
</form>
```
Untuk mengimplementasikannya, potongan kode tersebut ditaruh pada file HTML sesuai dengan halaman web yang kita inginkan dan di posisi yang kita inginkan. Selain tag-tag dan atribut-atribut yang digunakan di atas juga masih terdapat banyak atribut lain yang bisa digunakan sesuai dengan kebutuhan fitur pengguna. Action dan method pada tag form diisi sesuai dengan yang akan meng-*handle* program apabila pengguna memasukkan input dengan menekan tombol submit.

<br>

## Alur Data Submisi Form oleh Pengguna

1) Pertama-tama pengguna memasukkan data berupa teks pada kolom form yang telah disediakan pada halaman *create task* dan disubmit dengan menekan tombol submit yang mentrigger method POST.
   
2) Di dalam fungsi create_task apabila tombol ditekan (method request POST) maka akan dibuat variabel form berupa instansiasi kelas TaskForm dengan mengisikan parameter dari request POST.
   
3) Data form akan divalidasi terlebih dahulu. Apabila valid maka akan dibuat objek baru hasil instansiasi model Task dan menyusun data parameternya dengan user yang login saat ini, tanggal saat ini, judul dari form, dan deskripsi dari form.

4) Objek task disimpan ke dalam database.
   
5) Setelah itu, pengguna akan diarahkan kembali ke halaman utama todolist.
   
6) Halaman utaman menampilkan tabel berisi judul task, deskripsi, dan tanggal yang telah diisikan oleh pengguna sebelumnya. Data tersebut diakses dengan mengkuerikan seluruh objek instansiasi model Task dan memfilternya sesuai dengan user yang login saat ini dan data tersebut di-pass dengan menggunakan context.
   
7) Seluruh task pada kueri ditampilkan pada halaman utama dengan melakukan iterasi seluruh objek di dalam kueri. Iterasi dilakukan di dalam file HTML halaman utama todolist.
   
8) User dapat melihat hasil akhir seluruh task yang telah dibuatnya.

<br>

## Implementasi Tugas

### **Awalan**

1) Pastikan sudah menyalakan virtual environment sebelum memulai proyek dengan menuliskan command berikut di terminal
    ```sh
    env\Scripts\activate.bat
    ```

2) Membuat aplikasi baru bernama **todolist** dengan command di bawah ini dan menambahkan aplikasi ke dalam daftar INSTALLED_APPS di settings.py
    ```sh
    python manage.py startapp todolist
    ```
3) Menambahkan path untuk akses URL ```http://localhost:8000/todolist``` dengan cara memasukkan path baru di dalam urlpatterns di dalam file ```urls.py``` di folder proyek django agar melakukan routing ke todolist.urls
    ```py
    urlpatterns = [
        ...
        path('todolist/', include('todolist.urls')),
    ]
    ```
    
4) Membuat model Task dengan membuat kelas baru di dalam file ```models.py``` di folder todolist yang merupakan subkelas dari ```models.Model``` dan isikan seluruh atribut sesuai dengan yang diinginkan soal
    ```py
    from django.db import models

    class Task(models.Model):
        date = models.DateField()
        title = models.CharField(max_length=200)
        description = models.TextField()
        # on_delete CASCADE agar ketika user terhapus maka task ikut terhapus
        user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ```
    
5) Migrasikan model agar dapat terbaca aplikasi dengan command 
   ```sh
   python manage.py migrate
   ```

<br>

### **REGISTRASI**

6) Mengimplementasikan halaman registrasi akun dengan memasukkan fungsi yang akan meng-*handle* registrasi di dalam file views.py
    ```py
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
   ```
   dan membuat 
    
7) Membuat file HTML (misalkan register.html) yang akan menampilkan halaman web registrasi akun di dalam folder template dan memasukkan tag form yang akan ditampilkan. Bisa juga ditambahkan messages apabila terdapat message akun telah berhasil dibuat.

    ```html
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}
    ```

<br>

### **Login**

8) Membuat fungsi di dalam file views.py yang akan meng-*handle* halaman login dan mengautentikasi user ketika pengguna mencoba login
    ```py
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
    ```

9) Membuat file html (misalkan login.html) untuk menampilkan halaman login kepada pengguna dengan memasukkan form username dan password agar dapat diambil datanya untuk autentikasi user. Sebuah tombol redirect juga dibuat agar pengguna bisa pergi ke halaman registrasi akun.

    ```html
        <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>
    ```

<br>

### **Halaman Utama Todolist**

10) Membuat fungsi di dalam views.py yang akan meng-*handle* tampilan halaman utama yang nantinya berfungsi untuk menampilkan seluruh task yang dibuat oleh user dan tombol untuk menambahkan task.
    ```py
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
    ```

11) Membuat file html (misalkan todolist.html) di dalam folder template yang ditampilkan sebagai halaman utama todolist kepada pengguna. Implementasikan juga tampilan nama username dan iterasikan semua task yang ada di dalam kueri tasks sesuai dengan context yang di-*pass* oleh fungsi. Dua tombol juga dibuat untuk membuat task dan logout.
    ```html
    <h1>Todo List - PBP Tugas 4</h1>

    <br>
    <b>Username: </b>
    <p>{{username}}</p>
    <br>

    <table border="2">
        <tr>
        <th>Title</th>
        <th>Description</th>
        <th>Date</th>
        </tr>
        {% for task in tasks %}
            <tr>
                <td>{{task.title}}</td>
                <td>{{task.description}}</td>
                <td>{{task.date}}</td>
            </tr>
        {% endfor %}
    </table>

    <br>
    <button><a href="{% url 'todolist:create_task' %}">Create Task</a></button>

    <h5>Sesi terakhir login: {{ last_login }}</h5>

    <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
    ```

<br>

### **Halaman Create Task**

12) Membuat fungsi di dalam views.py yang akan meng-*handle* tampilan halaman pembuatan task yang berfungsi untuk menampilkan form inputan oleh pengguna dan tombol untuk mensubmit.

    ```py
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
                # Kembali ke halaman awal todolist
                return redirect('todolist:show_todolist')

        # Jika method request adalah GET atau lainnya
        else:
            form = TaskForm()
        # Menampilkan halaman create task
        context = {'form':form}
        return render(request, "create_task.html", context)
    ```

13) Membuat file html (misalkan create_task.html) di dalam folder template yang ditampilkan sebagai halaman pembuatan tugas kepada pengguna.
    ```py
    <h1>Create Task</h1>

    <form method="POST">
        {% csrf_token %}
        <table>  
            {{ form.as_table }}  
            <tr>  
                <td></td>
                <td><input type="submit" value="Create Task"/></td>  
            </tr>  
        </table>  
    </form>
    ```

<br>

### **Akhiran**

14) Membatasi akses halaman agar hanya dapat diakses oleh pengguna terautentikasi yang telah login. Apabila ternyata belum login, maka pengguna akan dialihkan ke halaman login. Fitur ini dapat diimplementasikan dengan menaruh dekorator berikut ini pada fungsi-fungsi yang dibatasi aksesnya :
    ```py
    @login_required(login_url='/todolist/login/')
    ```


15) Menambahkan path ke dalam urlpatterns di dalam file urls.py di folder todolist dengan url dan nama fungsi yang bersesuaian
    ```py
    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('create-task/', create_task, name='create_task'),
    ]
    ```
    
16)  Melakukan deployment dengan melakukan push kode ke repository github. Halaman aplikasi dapat diakses melalui link yang telah diset di heroku dan secret repository.

<br>
<br>


# Tugas 5 PBP

Lanjutan dari Tugas 4 dengan menambahkan styling pada web app yang telah dibuat sebelumnya
<br>

## Perbedaan Inline, Internal, dan External CSS

Inline | Internal | External
--- | --- | ---
Diimplementasikan pada baris tag HTML | Diaplikasikan pada heading section HTML | Diimplementasikan dengan membuat file CSS terpisah dan di-link dengan file HTML yang didesain
Style berlaku hanya pada tag yang diberi styling CSS | Style berlaku pada satu file HTML | Style dapat berlaku pada banyak file HTML, tergantung seberapa banyak file HTML yang me-link
Cara menggunakannya dengan atribut style="" di dalam tag HTML | Cara menggunakannya dengan melakukan styling dengan selector dan ditaruh di dalam tag <style></style> di heading HTML | Menggunakan selector di dalam file CSS terpisah
<br>

## Tag-Tag HTML5

1) ```<html>``` digunakan untuk merepresentasikan root dari file HTML, dapat diisikan atribut language (lang) untuk bahasa yang digunakan
2) ```<head>``` digunakan sebagai container metadata, diletakkan di dalam tag <html> dan sebelum tag <body>
3) ```<body>``` digunakan untuk mendefinisikan body halaman, sampir seluruh elemen yang akan ditampilkan di halaman ditaruh di dalam tag ini
4) ```h1-h6``` digunakan sebagai heading text
5) ```<br>``` digunakan untuk single line break text
6) ```<button>``` digunakan untuk membuat tombol
7) ```<p>``` digunakan untuk membuat dan menuliskan teks

<br>

## Tipe-Tipe CSS Selector

1) Element selector : menyeleksi berdasarkan tipe element HTML
    ```css
    p {
        text-align: center;
        color: red;
    }
    ```
2) ID selector : menyeleksi berdasarkan ID, dituliskan dengan diawali tanda pagar. Contoh berikut menampilkan selector untuk memilih elemen dengan ```id="para1"```
    ```css
    #para1 {
        text-align: center;
        color: red;
    }
    ```
3) Class selector : menyeleksi berdasarkan atribut *class*, dituliskan dengan diawali tanda titik. Contoh berikut menampilkan selector untuk memilih elemen dengan ```class="center"```
    ```css
    .center {
        text-align: center;
        color: red;
    }
    ```
4) Universal selector : memilih secara universal atau keseluruhan elemen dengan menuliskan tanda bintang
    ```css
    * {
    text-align: center;
        color: blue;
    }
    ```
<br>

## Implementasi Tugas

1) Meng-embed file css dari Bootstrap dengan memasukkan linknya di head HTML
    ```css
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    ```
2) Menggunakan desain-desain yang tersedia pada Bootstrap dengan mengubah atribut kelas pada elemen-elemen HTML
3) Untuk mengetahui sintaks-sintaksnya dapat merujuk lagi pada dokumentasi yang tersedia pada website Bootstrap