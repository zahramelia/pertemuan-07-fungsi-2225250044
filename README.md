
# Pertemuan 07 - Fungsi, Parameter, Return Value, dan Scope

## Identitas
- Nama: Zahra Amelia
- NIM: 2225250044
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan
Mempelajari penggunaan fungsi dalam Python, termasuk parameter, return value, dan scope variabel, serta menerapkannya untuk menyelesaikan permasalahan matematika. Program utama menyediakan menu untuk menghitung luas bangun datar, jumlah bilangan, dan faktorial dengan validasi input.

## Cara Menjalankan Program

Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek.

### Menjalankan Latihan

```bash
python latihan/01_salam.py
python latihan/02_luas_persegi_panjang.py
python latihan/03_jumlah_n.py
python latihan/04_statistik_sederhana.py
python latihan/05_scope.py
```

### Menjalankan Program Utama

```bash
python praktik/utilitas_matematika.py
```

## Penjelasan Fungsi

- `luas_persegi_panjang(p, l)`: menghitung luas persegi panjang berdasarkan panjang dan lebar.
- `luas_segitiga(a, t)`: menghitung luas segitiga berdasarkan alas dan tinggi.
- `jumlah_n(n)`: menghitung jumlah bilangan dari 1 sampai n menggunakan perulangan.
- `faktorial(n)`: menghitung faktorial bilangan menggunakan perulangan.
- `tampilkan_menu()`: menampilkan pilihan menu program.
- `baca_nonnegatif()`: memastikan masukan berupa bilangan bulat nonnegatif.

## Pengujian Program

| Pengujian | Input | Hasil yang Diharapkan | Status |
|---|---|---|---|
| Luas persegi panjang | p = 8, l = 5 | 40.0 | Berhasil |
| Luas segitiga | a = 10, t = 6 | 30.0 | Berhasil |
| Jumlah bilangan | n = 10 | 55 | Berhasil |
| Faktorial | n = 5 | 120 | Berhasil |
| Faktorial nol | n = 0 | 1 | Berhasil |

## Refleksi

Melalui latihan ini, saya mempelajari cara membuat dan memanggil fungsi, menggunakan parameter dan return value, serta memahami perbedaan variabel lokal dan variabel di luar fungsi. Saya juga belajar membagi program menjadi beberapa fungsi agar kode lebih terstruktur, mudah dibaca, dan mudah digunakan kembali.
