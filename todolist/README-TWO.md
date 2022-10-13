# Tugas 6 PBP

Daffa Ilham Restupratama <br>
NPM 2106751013 <br>
Kelas PBP B <br>

## Perbedaan Asynchronous Programming dengan Synchronous Programming

- Asynchronous programming adalah suatu pendekatan metode dalam pemrograman platform dimana suatu proses berjalan secara paralel/beriringan tanpa saling menunggu antara satu dengan yang lainnya. Dengan demikian, sisi klien dapat tetap menjalankan proses-proses yang lainnya setelah melakukan proses request tanpa menunggu terlebih dahulu meskipun proses request sebelumnya belum selesai direspon oleh sisi server. Manfaat dari pendekatan ini adalah waktu proses yang lebih singkat dan user experience yang lebih lancar.
- Synchronous programming merupakan pendekatan metode yang berkebalikan dengan asynchronous programming. Pada tiap-tiap prosesnya, program secara keseluruhan harus menunggu proses tersebut hingga selesai untuk menjalankan proses lainnya karena proses-proses tersebut tidak dapat berjalan secara paralel/beriringan. Akibatnya waktu untuk menjalankan seluruh proses menjadi lebih lambat.
<br>

## Paradigma Event-Driven Programming

Event-driven programming merupakan sebuah paradigma pemrograman dimana flow dari program ditentukan dari semua event atau peristiwa yang terjadi pada program. Event tersebut paling umum berupa input perintah dari pengguna, namun tidak menutup kemungkinan juga berupa pesan dari pengguna lain, event dari program lain yang telah ditautkan, hasil sensor, dan lain sebagainya. <br>
Contoh dari penerapan event-driven programming pada Tugas 6 PBP ini contohnya seperti pada fitur penambahan task dengan modal. Apabila tombol ditekan pengguna, maka modal akan muncul. Selanjutnya apabila pengguna memasukkan input task dan menekan save maka task baru akan terbuat dan muncul pada halaman todolist. <br>
## Penerapan asynchronous programming pada AJAX

Asynchronous programming pada AJAX diterapkan dengan mengambil data pada database yang telah diserialisasikan menjadi file JSON. Untuk melakukan penambahan data diperlukan fungsi POST, sedangkan untuk membaca data diperlukan fungsi GET. Halaman yang akan diterapkan asynchronous programming menggunakan AJAX di dalamnya harus memuat script Javascript untuk mengakses data-data tersebut secara asinkronus dan melakukan manipulasi pada DOM.

## Implementasi Tugas

1) Membuat fungsi baru di dalam views yang mengembalikan data task berdasarkan user yang sedang login saat ini berupa file yang telah diserialisasi menjadi JSON
    ```py
    @login_required(login_url='/todolist/login/')
    def tasks_json(request):
        data = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
2) Membuat path URL yang mengarah kepada fungsi tadi
    ```py
    from todolist.views import tasks_json

    urlpatterns = [
        ...
        path('json/', tasks_json, name='tasks_json'),
    ]
    ```
3) Mengambil data task menggunakan AJAX GET di dalam page
    ```js
    $.get('/todolist/json/', function(tasks, status){
        let content = '';
        for (let i=0; i<tasks.length; i++){
        content += `
        <div class="card text-white bg-dark mb-3">
            <div class="card-header" style="padding: 15px 10px 10px 10px">
                <h5 class="card-title">${tasks[i].title}</h5>
            </div>
            <div class="card-body">
                <p class="card-text">${tasks[i].description}</p>
                <p class="card-text"><small class="text-muted">${tasks[i].date}</small></p>
            </div>
        </div>
        `;
        $('.content').html(content);
        }
    })
    ```

4) Membuat tombol add task (berbeda dengan create task pada tugas 4 sebelumnya) yang menampilakn modal dan berisi input task baru.
    ```html
    <!-- script modal pada header -->
   <script>
      const myModal = document.getElementById('myModal')
      const myInput = document.getElementById('myInput')

      myModal.addEventListener('shown.bs.modal', () => {
      myInput.focus()
      })
   </script>

   <!-- Tombol add task pakai ajax -->
   <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Add Task
   </button>

   <!-- Modal -->
   <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
          <div class="modal-content">

              <div class="modal-header">
                  <h1 class="modal-title fs-5" id="exampleModalLabel">Add Task</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>

              <div class="modal-body">
                  <form action="" method="POST">
                      {% csrf_token %}
                      <div class="form-outline form-white mb-4">
                          <input type="text" class="form-control form-control-lg"
                          name="title" id="title" placeholder="Title" required/>
                      </div>
                      <div class="form-outline form-white mb-4">
                          <input type="text" class="form-control form-control-lg"
                          name="description" id="description" placeholder="Description" required/>
                      </div>

                      <div class="modal-footer">
                          <button type="submit" class="btn btn-primary" id="add-task">Save</button>
                      </div>
                  </form>
              </div>
              
          </div>
      </div>
   </div>
    ```

5) Membuat fungsi baru di dalam views untuk menambahkan data task baru
    ```py
   def add_task(request):
       # Jika method request adalah POST
       if request.method == "POST":
           # Mengambil data form dari request
           judul = request.POST.get('title')
           deskripsi = request.POST.get('description')
           # Membuat instansiasi task baru
           task = Task(user=request.user, title=judul, description=deskripsi, date=datetime.datetime.now())
           # Menyimpan ke database
           task.save()
       return HttpResponse('')
    ```
6) Membuat path URL yang mengarah kepada fungsi tadi
    ```py
    from todolist.views import add_task

    urlpatterns = [
        ...
        path('add/' , add_task, name='add_task'),
    ]
    ```

7) Menghubungkan form di dalam modal dengan path ```/todolist/add```
    ```js
    $(document).ready( function(){
        $('#add-task').click( function(){
            let title= $('#title').val();
            let description = $('#description').val();
            let CSRFtoken = $('input[name="csrfmiddlewaretoken"]').val();
        $.post('/todolist/add/', {
            title: title,
            description: description,
            csrfmiddlewaretoken: CSRFtoken
            }, function(){
                $('.modal').hide();
                $('.backdrop').hide();
                ...
    ```