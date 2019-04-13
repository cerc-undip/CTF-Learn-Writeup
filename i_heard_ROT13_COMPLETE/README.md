# I Heard You Can't ROT13 Numbers
**Category:** cryptography
> I saw this in a file but I can't figure out what it meant: MzkuM3gaMKE0nJ5aK3A0LKW0MJE9
> 
> Can you help?
---

Dari judul kita sudah bisa menebak apa algoritma yang digunakan untuk menyembunyikan pesan rahasianya, yaitu ROT13. Logika dari algoritma enkripsi ini adalah dengan memutar huruf abjad dari A sampai dengan Z sebanyak 13 kali. ([Baca disini](http://datagenetics.com/blog/july42015/index.html))

![ROT 13](http://datagenetics.com/blog/july42015/big.png "sumber: datagenetics.com")

Oke, kita langsung saja perintahkan terminal untuk menyelesaikannya.
```bash
echo MzkuM3gaMKE0nJ5aK3A0LKW0MJE9 | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

> Jika belum paham arti perintah `tr` silahkan baca writeup challenge [Basic ROT 13](https://github.com/cerc-undip/CTF-Learn-Writeup/tree/update/basic_rot_13_COMPLETE).

Setelah kita eksekusi perintahnya, kita menemukan bahwa pesan ini masih dirahasiakan lagi. Namun pesan ini merupakan besan berbentuk Base64 ([Baca disini](https://en.wikipedia.org/wiki/Base64)), maka dari itu kita perlu men-_decode_ pesan ini
```bash
echo MzkuM3gaMKE0nJ5aK3A0LKW0MJE9 | tr 'A-Za-z' 'N-ZA-Mn-za-m' | base64 -d
```

Terakhir, kita akan mendapatkan flag yang kita cari.

flag : `flag{getting_started}`