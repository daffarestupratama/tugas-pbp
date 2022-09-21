# Tugas Mata Kuliah PBP - Proyek Django

oleh :
Daffa Ilham Restupratama
NPM 2106751013
Kelas PBP B

## Pendahuluan

Repositori ini digunakan sebagai pengerjaan tugas mata kuliah Pemrograman Berbasis Platform. Tugas yang diberikan yaitu berupa proyek aplikasi yang dikerjakan dengan platform framework django. Di bawah ini merupakan jawaban-jawaban untuk menjawab pertanyaan-pertanyaan yang diberikan pada Tugas 2.

## 1. Bagan _Client Requests_ dan _Responses_

![MTV Flowchart](https://raw.githubusercontent.com/daffarestupratama/tugas-pbp-django/main/Flowchart%20MTV%20Django.png "Bagan Requests dan Responses")

Bagan diatas menampilkan bagaimana proyek django bekerja dengan arsitektur MTV. M adalah Model, sebuah layer yang melakukan akses data. T adalah Template, yaitu layer yang menjadi acuan templat yang akan ditampilkan di layar browser pengguna. V adalah View, yaitu layer yang menjadi pusat penghubung antara model dan template.

Agar aplikasi django dapat dijalankan dan ditampilkan di layar pengguna, pertama-tama pengguna melakukan user request. User request ini didasarkan pada url yang dimasukkan pengguna ke bilah url/search di browsernya. URL tersebut akan di-breakdown pada setiap tanda garis miring (slash). Contohnya pada proyek ini URL-nya adalah https://daffailham.herokuapp.com/katalog/, maka akan dipecah menjadi "daffailham.herokuapp.com" yang menjadi domainnya, lalu string "katalog", dan string kosong (""). Dengan demikian, mulanya link akan di-handle oleh urls.py yang ada di folder proyek. Setelah itu karena di belakang domain terdapat string "katalog" maka akan dialihkan ke urls.py yang ada di folder katalog. Setelah itu karena di belakangnya lagi merupakan string kosong, maka path yang diambil yaitu memanggil fungsi show_katalog() di dalam file views.py di folder katalog. 

Di dalam view, data akan diambil dari model yang telah dibuat. Model dapat dianalogikan sebagai sebuah cetakan dari data-data yang ada. Cetakan ini diisi oleh data-data dari database file json. Sehingga, data-data dapat masuk dan diproses di view.  Setelah didapatkan data-datanya, data tersebut dimasukkan ke dalam template yang telah tersedia yang berupa file html sehingga akan tercipta file html yang telah lengkap terisi data. File tersebut akan dikembalikan ke view untuk ditampilkan di layar browser pengguna. Tampilan itulah yang akhirnya menjadi http response.

## 2. _Virtual Environment_

Dalam pengembangan aplikasi menggunakan platform django dibutuhkan berbagai packages dan dependencies sesuai dengan kebutuhan pengembangan aplikasi yang diinginkan. Fungsinya adalah untuk menyediakan fitur-fitur yang dapat langsung digunakan oleh sang pengembang aplikasi. Packages dan dependencies tersebut juga memiliki versinya masing-masing. Oleh karena pentingnya kehadiran packages dan dependencies, hal tersebut harus diinstal ketika proses pengembangan, debugging, dan deployment. Namun nantinya akan terdapat masalah ketika jumlah pengembang dan perangkat yang digunakan lebih dari satu. Bisa jadi packages yang terinstal di satu perangkat berbeda versi dengan yang ada di perangkat dari pengembang lain. Untuk itu digunakanlah sistem bernama virtual environment.

Virtual environment merupakan suatu tools yang tersedia pada django yang berfungsi untuk menciptakan suatu environment terisolasi agar tertutup dan tidak dapat diakses dari luar atau hanya dapat diakses dari dalam project tersebut saja. Seluruh package dan dependency yang dibutuhkan untuk suatu proyek django tidak diinstal secara global di perangkat pengembang, tetapi diinstal secara lokal di dalam direktori proyek masing-masing. Dengan demikian setiap proyek dapat dijalankan menggunakan packages-nya masing-masing sesuai dengan versi yang dibutuhkannya. Dan apabila terdapat banyak proyek di dalam suatu perangkat, proyek-proyek tersebut tidak saling mempengaruhi satu sama lain. 

Packages dalam virtual environment juga umumnya memiliki size yang besar dan terkadang bersifat redundant. Oleh karena itu apabila kita ingin memasukkan proyek kita ke dalam repositori daring dan men-deploy proyek, maka kita tidak perlu mengunggah package-package tersebut sebab django secara otomatis akan menge-list seluruh packages beserta versinya di dalam file requirements.txt. Cara kita untuk mengecualikan package-package yang terinstal pada virtual environment yaitu dengan memasukkan env/venv ke dalam file gitignore.

Seperti yang telah dijelaskan sebelumnya, virtual environment sangat penting dan telah menjadi hal yang tidak terpisahkan saat kita membuat proyek aplikasi dengan django. Kita bisa saja membuat proyek django tanpa menggunakan virtual environment dan hanya mengandalkan packages yang diinstal secaara global, namun nantinya akan terdapat banyak kendala yang dapat dialami. Apabila proyek tersebut dikerjakan di perangkat berbeda yang terinstal packages berbeda versi, maka bisa jadi ada package yang tidak kompatibel sehingga proyek aplikasi tersebut menjadi tidak bisa dijalankan. Tidak hanya itu, apabila ada lebih dari satu proyek di perangkat kita dan proyek-proyek tersebut menggunakan versi package yang berbeda, maka akan ada proyek yang tidak bisa berjalan karena packages yang terinstal secara global hanya terinstal satu versi saja.

## Implementasi Tugas

1.) Fungsi pada views.py yang ada pada proyek ini bernama show_katalog. Fungsi ini melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML untuk ditampilkan.Implementasinya yaitu dengan cara mengimpor kelas CatalogItem models.py. Selanjutnya di dalam fungsi show_katalog dibuat sebuah variabel yang menyimpan seluruh objek dari CatalogItem, dan variabel bernama context yang berisi data-data yang akan di-return dan ditampilkan di file HTML. Setelah itu fungsi tersebut mengembalikan fungsi render yang diisi argumen berupa request, string file html yang dituju (yakni katalog.html), dan variabel context yang berisi data-data tadi.

2.) Routing untuk memetakan fungsi yang telah dibuat pada file views.py dibuat dengan cara variabel urlpatterns ditambahkan path yang diisi argumen berupa string 'katalog/' dan meng-include file urls.py yang ada pada katalog dengan include('katalog.urls'). Lalu pada urlpatters di dalam file urls.py yang ada pada folder katalog juga ditambahkan path yang diisi argumen berupa string kosong dan memanggil fungsi show_katalog. Sehingga saat dijalankan url "<nama-domain.tld>/katalog/", browser akan menampilkan file html yang dijalankan pada fungsi show_katalog.

3.) Pemetaan data ke HTML dari database dilakukan dengan membuat template page berupa file html di dalam folder template di dalam folder katalog. Nama file html harus sesuai dengan yang ada pada fungsi show_katalog agar ketika fungsi show_katalog dipanggil maka file html dapat ditampilkan. Lalu untuk memasukkan data, digunakan sintaks django berupa {{nama_variabel}} agar variabel data dapat ditampilkan pada halaman html.

4.) Deployment dilakukan dengan membuat akun di suatu platform penyedia layanan cloud server, pada proyek ini yang digunakan yaitu Heroku. Setelah membuat akun dan membuat aplikasi pada platform Heroku, akan didapatkan API key dan nama aplikasi. API Key dan nama aplikasi dimasukkan ke dalam secret variable repository sehingga secrets.HEROKU_API_KEY dan secrets.HEROKU_APP_NAME di dalam file dpl.yml masing-masing disubstitusi dengan kode API key dan nama aplikasi heroku. Sehingga ketika di-deploy, github dapat mengetahui API key dan nama aplikasi di heroku yang akan dijadikan tempat untuk deployment.

## Tautan Aplikasi yang Telah Dideploy

[Halaman Utama](https://daffailham.herokuapp.com)

[Halaman Katalog](https://daffailham.herokuapp.com/katalog/)
