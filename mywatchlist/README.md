# Tugas 3 PBP

Daffa Ilham Restupratama <br />
NPM 2106751013 <br />
Kelas PBP B

## Link Deploy

- [Halaman Mywatchlist](https://daffailham.herokuapp.com/mywatchlist)
- [Link HTML](https://daffailham.herokuapp.com/mywatchlist/html)
- [Link JSON](https://daffailham.herokuapp.com/mywatchlist/json)
- [Link XML](https://daffailham.herokuapp.com/mywatchlist/xml)

## Perbedaan HTML, JSON, dan XML

HTML | JSON | XML
--- | --- | ---
Bahasa markup | Notasi objek JavaScript | Bahasa Markup
Berfungsi untuk menampilkan webpage | Berfungsi untuk transfer data | Berfungsi untuk transfer data
Menggunakan tag | Menggunakan format array | Menggunakan tag dan lebih terstruktur berbentuk tree
Banyak integrasi framework | kurang aman | lebih aman
Support comments | Tidak support comments | Support comments
Menampilkan data array sesuai dengan framework atau template yang telah dibuat | Support array | Tidak support array
Support banyak text encoding | Hanya support UTF-8 | Support lebih bayak text encoding

## Pentingnya _Data Delivery_ Pada Implementasi Platfowm

Aplikasi berbasis platform pastinya memiliki data yang dinamis. Dengan kata lain, data tersebut pasti sering berubah-ubah dan tidak statis saja. Data tersebut secara kontinyu akan diakses oleh aplikasi untuk ditampilkan kepada klien. Untuk itu, data delivery penting untuk diimplementasikan agar proses pengaksesan data dapat berjalan secara lancar.

## Implementasi Tugas

1) Pastikan sudah menyalakan virtual environment sebelum memulai proyek dengan menuliskan command berikut di terminal
    ```sh
    env\Scripts\activate.bat
    ```

2) Membuat aplikasi baru bernama **mywatchlist** dengan command di bawah ini dan menambahkan aplikasi ke dalam daftar INSTALLED_APPS di settings.py
    ```sh
    python manage.py startapp mywatchlist
    ```
3) Menambahkan path untuk akses URL ```http://localhost:8000/mywatchlist``` dengan cara memasukkan path baru di dalam urlpatterns di dalam file ```urls.py``` di folder proyek django agar melakukan routing ke mywatchlist.urls
    ```sh
    urlpatterns = [
        ...
        path('mywatchlist/', include('mywatchlist.urls')),
    ]
    ```
    
4) Membuat model Mywatchlist dengan membuat kelas baru di dalam file ```models.py``` di folder mywatchlist yang mengambil parameter ```models.Model``` dan berisikan seluruh atribut sesuai dengan yang diinginkan soal
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

## Screenshot Postman

