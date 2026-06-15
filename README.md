# Detective Mystery

Game multiplayer bertema detektif yang dikembangkan menggunakan arsitektur *Client-Server* dengan komunikasi *TCP Socket Programming*. Pemain berperan sebagai detektif yang harus mengumpulkan petunjuk, berdiskusi dengan pemain lain melalui fitur chat, dan menentukan pelaku kejahatan.

## LINK Demo: https://youtu.be/zWTCeOakNB0*

## Anggota Kelompok

### Mahda Annisa (2408107010036)
*Job Desk:*
- Pengembangan Sistem CLI
- Implementasi Socket Programming
- Implementasi Client-Server
- Pengembangan Logika Permainan
- Pembuatan Laporan

### Niswatul 'Azimah (2408107010003)
*Job Desk:*
- Mengatur Implementasi Ide dan Mengarahkan Alur Program
- Pengembangan Sistem Web-Based
- Implementasi Flask
- Implementasi Flask-SocketIO
- Pengembangan Routing dan API
- Pengembangan Logika Permainan Dalam Web

### Raisa Nabila (2408107010037)
*Job Desk:*
- Desain User Interface (UI)
- Implementasi Tampilan Web
- Pengembangan Front-End
- Pengujian Antarmuka Pengguna
- Pembuatan PPT

## Teknologi yang Digunakan

- Python
- TCP/IP
- Socket Programming
- Multi-Threading
- Flask
- Flask-SocketIO
- HTML, CSS, JavaScript

## Fitur Utama

- Multiplayer Client-Server
- Investigasi Lokasi
- Sistem Petunjuk (Clues)
- Daftar Tersangka
- Chat Room Multi-User
- Sistem Tuduhan (Accuse)
- Versi CLI dan Web-Based

## Alur Sistem

1. Pemain login menggunakan nama detektif.
2. Client terhubung ke server melalui protokol TCP.
3. Pemain melakukan investigasi pada berbagai lokasi.
4. Server mengirim petunjuk sesuai lokasi yang dipilih.
5. Petunjuk disimpan pada notes pemain dan skor bertambah.
6. Pemain dapat berkomunikasi melalui fitur chat.
7. Pemain melihat daftar tersangka dan menganalisis petunjuk.
8. Pemain menggunakan perintah *accuse* untuk menentukan pelaku.
9. Server memverifikasi tuduhan dan menampilkan hasil permainan.
