# Sistem Prediksi Cuaca Berbasis Edge AI

## Arsitektur 
![Weather_predict_architecture_bb](https://github.com/user-attachments/assets/150d4512-954d-43fa-8cad-7183dfb82188)

Rangkaian di atas menggunakan Raspberry Pi 3 Model B sebagai pusat kendali untuk membaca data dari sensor dan menampilkan informasi pada LCD. Sensor yang digunakan adalah DHT11, yang berfungsi untuk mengukur suhu dan kelembapan udara. Sensor ini terhubung ke Raspberry Pi melalui tiga pin: pin VCC (merah) terhubung ke pin 5V pada Raspberry Pi untuk daya, pin GND (hitam) terhubung ke pin ground (GND), dan pin DATA (hijau) terhubung ke pin GPIO4 (pin 7) untuk mengirimkan data. Selain itu, modul LCD 16x2 dengan antarmuka I2C (LCM1602) digunakan untuk menampilkan data yang telah diproses oleh Raspberry Pi. Modul ini terhubung dengan empat kabel, yaitu GND (hitam) ke ground, VCC (merah) ke pin 5V untuk daya, SDA (kuning) ke pin SDA (GPIO2 atau pin 3), dan SCL (biru) ke pin SCL (GPIO3 atau pin 5).

## Flowchart
![Edge-weather drawio](https://github.com/user-attachments/assets/f4d7e8db-9dac-466b-ac4b-759a57660c49)

Flowchart di atas menjelaskan alur kerja sistem prediksi cuaca menggunakan data suhu dan kelembapan dengan model ANN (Artificial Neural Network). Berikut adalah penjelasan detail untuk setiap langkah pada flowchart:

1. Mulai (Start)
Proses dimulai dengan menjalankan sistem prediksi cuaca.
2. Input: Data Suhu dan Kelembapan
Sistem menerima input berupa data suhu dan kelembapan. Data ini dapat berasal dari sensor DHT11 yang dihubungkan ke Raspberry Pi.
3. Prediksi Cuaca Menggunakan Model ANN
Data suhu dan kelembapan diproses menggunakan model prediksi cuaca berbasis ANN (Artificial Neural Network). Hasilnya adalah prediksi apakah cuaca akan hujan atau cerah.
4. Apakah Cuaca Hujan?
Sistem mengevaluasi hasil prediksi:
- Jika cuaca diprediksi hujan, maka nilai is_raining diset menjadi 1, dan data hujan (rain_data) diperbarui.
- Jika cuaca diprediksi tidak hujan, maka nilai is_raining diset menjadi 0, dan rain_data diperbarui sesuai dengan kondisi ini.
5. Apakah Ada Lebih dari 2 Data Hujan dalam 8 Jam Terakhir?
Sistem mengecek jumlah data hujan yang tercatat dalam 8 jam terakhir:
- Jika lebih dari 2 data hujan, berarti penyiraman tidak diperlukan. Sistem akan menampilkan simbol "W" (watering not needed) di layar LCD.
- Jika kurang dari atau sama dengan 2 data hujan, berarti penyiraman diperlukan. Sistem akan menampilkan simbol "X" di layar LCD.
6. Menampilkan Data pada LCD
Sistem menampilkan informasi berikut pada layar LCD:
- Suhu
- Kelembapan
- Prediksi cuaca (hujan atau cerah)
- Data hujan yang tercatat.
7. Akhir (End)
Setelah semua data ditampilkan, proses selesai, dan sistem siap untuk iterasi berikutnya.
