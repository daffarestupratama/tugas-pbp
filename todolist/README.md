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

```sh
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

1) .

<br>

## Implementasi Tugas

1) Pastikan sudah menyalakan virtual environment sebelum memulai proyek dengan menuliskan command berikut di terminal
    ```sh
    env\Scripts\activate.bat
    ```

2) Membuat aplikasi baru bernama **todolist** dengan command di bawah ini dan menambahkan aplikasi ke dalam daftar INSTALLED_APPS di settings.py
    ```sh
    python manage.py startapp todolist
    ```
3) Menambahkan path untuk akses URL ```http://localhost:8000/todolist``` dengan cara memasukkan path baru di dalam urlpatterns di dalam file ```urls.py``` di folder proyek django agar melakukan routing ke todolist.urls
    ```sh
    urlpatterns = [
        ...
        path('todolist/', include('todolist.urls')),
    ]
    ```
    
4) Membuat model Task dengan membuat kelas baru di dalam file ```models.py``` di folder todolist yang merupakan subkelas dari ```models.Model``` dan isikan seluruh atribut sesuai dengan yang diinginkan soal
    ```sh
    from django.db import models
    from django.core.validators import MaxValueValidator, MinValueValidator 
    
    class WatchlistItem(models.Model):
        watched = models.BooleanField()
        title = models.CharField(max_length=50)
        rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
        release_date = models.DateField()
        review = models.TextField()
    ```

5) Menambahkan minimal 10 data untuk objek sesuai dengan model Mywatchlist yang telah dibuat tadi dengan membuat file baru berformat JSON di dalam folder fixtures di dalam folder mywatchlist. File JSON dibuat dengan syntax seperti berikut ini.
    ```sh
    [
    {
        "model":"mywatchlist.WatchlistItem",
        "pk":<nomor kode id>,
        "fields":{
            "watched":"<True/False>",
            "title":"<judul>",
            "rating": "<nilai 1-5>",
            "release_date": "<YYYY-MM-DD>",
            "review": "<deskripsi ulasan>"
        }
    },
    ...
    ]
    ```
    
6) Migrasikan data agar dapat terbaca aplikasi dengan command ```python manage.py makemigrations``` dan ```python manage.py migrate```

7) Membuat routing untuk masing-masing URL yang bersesuaian untuk mengambil file HTML, JSON, dan XML dengan membuat fungsi yang menerima argumen berupa request dan mengembalikan HttpResponse di dalam file views.py
    ```sh
    def show_html(request):
    data_watchlist = WatchlistItem.objects.all()
    context = {
        'watchlist': data_watchlist,
        'nama': 'Daffa Ilham Restupratama',
        'id': '2106751013'
    }
    return render(request, "watchlist_data.html", context)

    def show_xml(request):
        data = WatchlistItem.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
    def show_json(request):
        data = WatchlistItem.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
    ...
    ```
    
8) Menambahkan path ke dalam urlpatterns di dalam file urls.py di folder mywatchlist dengan url dan nama fungsi yang bersesuaian
    ```sh
    urlpatterns = [
        path('', show_mywatchlist, name='show_mywatchlist'),
        path('html/', show_html, name="show_html"),
        path('xml/', show_xml, name="show_xml"),
        path('json/', show_json, name="show_json"),
        path('xml/<int:id>', show_xml_by_id, name="show_xml_by_id"),
        path('json/<int:id>', show_json_by_id, name="show_json_by_id"),
    ]
    ```
    
9) Melakukan deployment dengan melakukan push kode ke repository github. Halaman aplikasi dapat diakses melalui link yang telah diset di heroku dan secret repository.

<br>
