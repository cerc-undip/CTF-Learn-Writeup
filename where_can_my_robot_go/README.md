# Where Can My Robot Go?
**Category:** miscellaneous
```
Hint: Where do robots find what pages are on a website?
Hint 2: What does disallow tell a robot? Hint 3: The flag is not 70r3hnanldfspufdsoifnlds
```
---

Di challenge ini diberikan clue yang cukup membantu untuk menyelesaikan. Robot yang dimaksud disini adalah file `robots.txt` yang ada di setiap halaman web.

File `robots.txt` dipasang di web untuk menentukan folder mana saja yang diizinkan atau tidak diizinkan untuk di-index oleh mesin pencari.

Kita coba akses file `robots.txt` website CTFLearn melalui browser
```
https://ctflearn.com/robots.txt
```

Di dalam file ini, _developer_ tidak memperbolehkan _search engine_ untuk mengakses file `/70r3hnanldfspufdsoifnlds.html`. Tapi, kita akses file ini dengan harapan bisa mendapatkan flag yang kita cari.
```
https://ctflearn.com/70r3hnanldfspufdsoifnlds.html
```

Ternyata kita menemukan flag di dalamnya.

> Untuk mempersingkat kita bisa menggunakan cURL untuk mendapatkan halaman yang kita akses
> cURL sangat berguna ketika menyelesaikan challenge dengan kategori **web**

```
curl https://ctflearn.com/70r3hnanldfspufdsoifnlds.html
```

flag : `abctf{r0b0ts_4r3_th3_futur3}`