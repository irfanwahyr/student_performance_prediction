# Proyek Akhir: Menyelesaikan Permasalahan Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

* banyaknya mahasiswa yang melakukam pengunduran diri (dropout)
* faktor yang mempengaruhi dropout

### Cakupan Proyek

Cakupan proyek kali ini akan melakukan prediksi mahasiswa, yaitu prediksi berdasarkan kondisi finansial mahasiswa. dengan begitu akan terlihat faktor dari finansial mahasiswa yang menentukan apakah kondisi finansial berpengaruh pada status dropout. akan dianalisis juga dataset tersebut dengan dashboard sehingga gambaran permasalahan akan jelas. sehingga berdasarkan cakupan tersebut, maka akan digunakan tools sebagai berikut.
* [dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
* bahasa pemrograman Python
* metabase dan supabase untuk visualisasi dataset serta sebagai database online untuk analisis data
* serta library python pendukung pemrosesan serta untuk machine learning

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
1. Buka terminal atau PowerShell.
2. Buat sebuah folder baru bernama submission dengan menjalankan perintah berikut.
```
mkdir submission
```

3. Pindah ke folder terbaru tersebut menggunakan perintah berikut.
```
cd submission
```

4. Buat sebuah virtual environment dengan menjalankan perintah berikut.
```
pipenv install
```

5. Aktifkan virtual environment dengan menjalankan perintah berikut.
```
pipenv shell
```

6. Instal semua library yang dibutuhkan menggunakan perintah berikut.
```
pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn joblib streamlit
```

## Business Dashboard

dashboard dapat diakses pada [link](http://localhost:3000/public/dashboard/88f48d98-3a7f-4f9d-8655-14363bbbc486)

pada dashboard menunjukkan beberapa visualisasi. keterangan setiap visualisasi adalah sebagai berikut.
- distribusi status menunjukkan distribusi status mahasiswa. terlihat banyak mahasiswa yang Graduate, disusul Dropout, dan terakhir Enrolled.
- pada GDP, banyak mahasiswa memiliki GDP dibawah 0, tapi juga banyak di atas 0.
- pada Debtor, ternyata lebih banyak mahasiswa yang tidak memiliki Hutang.
- untuk tingkat inflasi ternyata bermacam-macam. mulai dari yang terendah -0.8, sampai yang tertinggi 3.7. dan juga persebaran mahasiswa terlihat di titik2 nya
- pada tingkat pengangguran mahasiswa, terlihat banyak yang memiliki rasio di atas 13.9
- dan terakhir, terkait biaya UKt. ternyata 88% mahasiswa sudah membayar uang kuliah.


## Menjalankan Sistem Machine Learning

prototype dapat diakses pada [link](https://studentperformanceprediction-vdbb2zlhfau5o7spjzgjvx.streamlit.app/)

cara melakukan prediksi
- input kondisi mahasiswa apakah debtor/memiliki hutang (ya atau tidak)
- input kondisi apakah mahasiswa membayar biaya kuliah terkini (ya atau tidak)
- input tingkat pengangguran (minimal 0.0)
- input tingkat inflasi
- input jumlah GDP

jika semua value sudah diinput, tekan Prediksi, maka hasilnya ada 2 kemungkinan:
*Mahasiswa diprediksi akan Graduate atau Mahasiswa diprediksi akan Dropout*

## Conclusion

dari analisis dan modelling dari pengaruh finansial terhadap pengunduran diri (dropout) mahasiswa adalah ada pengaruh finansial pada dropout mahasiswa. dari hasil prediksi yang dilakukan, hasilnya model dapat memprediksi status mahasiswa akan dropout atau tidak jika memiliki kondisi dan nilai tertentu. pada dashboard juga terlihat hubungan antara data yang terkait dan sebagai hasil analisis awal pengaruh kondisi finansial mahasiswa terhadap pengunduran diri (dropout)

### Rekomendasi Action Items

Berikut beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target.

* memberikan beasiswa pada mahasiswa yang bermasalah terkait finansial,
* memberikan keringanan terkait UKT (biaya pendidikan kuliah) pada mahasiswa yang terkena masalah finansial,
* menambah jangka waktu pembayaran UKT (biaya pendidikan kuliah).

semua saran bertujuan untuk meringankan mahasiswa terkait finansial, sehingga tidak terbebani terkait biaya kuliah, dan bisa berdampak pada menurunnya dropout (pengunduran diri).