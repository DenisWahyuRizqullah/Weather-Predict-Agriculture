# Sistem Prediksi Cuaca Berbasis Edge AI

# Arsitektur 
![Weather_predict_architecture_bb](https://github.com/user-attachments/assets/150d4512-954d-43fa-8cad-7183dfb82188)

Rangkaian di atas menggunakan Raspberry Pi 3 Model B sebagai pusat kendali untuk membaca data dari sensor dan menampilkan informasi pada LCD. Sensor yang digunakan adalah DHT11, yang berfungsi untuk mengukur suhu dan kelembapan udara. Sensor ini terhubung ke Raspberry Pi melalui tiga pin: pin VCC (merah) terhubung ke pin 5V pada Raspberry Pi untuk daya, pin GND (hitam) terhubung ke pin ground (GND), dan pin DATA (hijau) terhubung ke pin GPIO4 (pin 7) untuk mengirimkan data. Selain itu, modul LCD 16x2 dengan antarmuka I2C (LCM1602) digunakan untuk menampilkan data yang telah diproses oleh Raspberry Pi. Modul ini terhubung dengan empat kabel, yaitu GND (hitam) ke ground, VCC (merah) ke pin 5V untuk daya, SDA (kuning) ke pin SDA (GPIO2 atau pin 3), dan SCL (biru) ke pin SCL (GPIO3 atau pin 5).

# Flowchart
![Edge-weather drawio](https://github.com/user-attachments/assets/f4d7e8db-9dac-466b-ac4b-759a57660c49)

