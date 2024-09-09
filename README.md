Hello! this is Lazacil (<http://ischika-afrilla-lazacil.pbp.cs.ui.ac.id/>), siap melayani para lazy pacil 😉😎🤞
---------------------------------------------------------------------------------------------------------------------------------------------------

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Awalnya, saya membuat folder bernama "lazacil" di direktori lokal komputer dan membuka Command Prompt (cmd) di dalam direktori tersebut untuk membuat *virtual environment*. Setelah itu, saya membuat file `requirements.txt` yang berisi daftar *dependencies* yang diperlukan. Setelah proyek Django "lazacil" dibuat, saya mengonfigurasi bagian `ALLOWED_HOSTS` di file `settings.py`, menjalankan server, dan mengakses *localhost* untuk memastikan proyek berjalan dengan baik.

Setelah semua konfigurasi awal selesai, saya menghentikan server, menonaktifkan *virtual environment*, dan menambahkan file `.gitignore`. Kemudian, saya mengunggah kode proyek ke GitHub. Selanjutnya, saya mengakses halaman PWS (Pacil Web Service), membuat proyek baru dengan nama "lazacil", dan menambahkan URL deployment PWS ke dalam `ALLOWED_HOSTS`.

Saya melanjutkan dengan melakukan *push* kode ke PWS, memeriksa status proyek, dan memastikan aplikasi dapat dibuka melalui browser. Setelah itu, saya mengaktifkan kembali *virtual environment* dan membuat aplikasi baru bernama "main" yang saya tambahkan ke `INSTALLED_APPS`. Di dalam aplikasi tersebut, saya membuat folder "template" dan mengisi file `main.html` sesuai desain yang diinginkan.

Setelah template selesai, saya membuat model dasar di `models.py` dan menjalankan migrasi untuk menerapkan perubahan. Kemudian, saya membuat fungsi `show_main` untuk merender `main.html` menggunakan data yang sesuai. Setelah fungsi tersebut selesai, saya memodifikasi template agar dapat menampilkan variabel yang didefinisikan.

Saya mengonfigurasi *routing* dengan membuat `urls.py` di dalam aplikasi "main" dan menghubungkannya dengan fungsi `show_main`. Kemudian, saya menambahkan *routing* tersebut ke file `urls.py` di direktori proyek utama dan mengeceknya di *localhost*. Terakhir, saya membuat *unit test* di `main/tests.py`, menambahkan beberapa tes, dan melakukan *push* kode ke GitHub serta PWS.