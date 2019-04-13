# C_e_er
**Category:** cryptography
> I got a message from a Roman General who liked the number 13 and he liked keys.
> This is the message:
> xwfsutyfxwsubvrohirbjvehojbrveoljrbvjrbivlojrbevhipojrbviuobvurosibjvrhsuoibjrvshiouljrbhsioujrbsiluorjsbihjrlosynt{PnrfneVfAbgFrpher}jbr;hsucjrvhucjrvhujrbvsiljrvbhujvbfqywyfxwiusc2vheucrhsucjvrhucjrvhtsbjrvltjrbevltjrheltjrheltjrbhltbjhrletsbhjrletjhrlestjrvhstrjvehsltjrehvljtvhltvhjlt
---

Pada challenge ini kita diminta untuk mendekripsi pesan yang disediakan dan menemukan flag-nya.

Ada beberapa clue untuk menyelesaikan challenge ini, yaitu:
* Dari judul "C_e_er"
* Kata "Roman"
* Kata "who liked the number 13"

Dari sini kita dapat simpulkan bahwa algoritma yang dipakai untuk mengenkripsi pesan ini adalah Caesar dengan rotasi sebanyak 13 kali. Jika belum paham apa itu **Caesar** dan **ROT 13** silahkan [baca disini](http://datagenetics.com/blog/july42015/index.html).

Simpan pesan rahasia kedalam file bernama `quest.txt` agar kita bisa dengan mudah untuk memprosesnya.

```bash
echo xwfsutyfxwsubvrohirbjvehojbrveoljrbvjrbivlojrbevhipojrbviuobvurosibjvrhsuoibjrvshiouljrbhsioujrbsiluorjsbihjrlosynt{PnrfneVfAbgFrpher}jbr;hsucjrvhucjrvhujrbvsiljrvbhujvbfqywyfxwiusc2vheucrhsucjvrhucjrvhtsbjrvltjrbevltjrheltjrheltjrbhltbjhrletsbhjrletjhrlestjrvhstrjvehsltjrehvljtvhltvhjlt > quest.txt
```

Selanjutnya mari kita dekripsi pesan tersebut dengan perintah `tr` untuk mentranslasikan setiap huruf.
```bash
cat quest.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

> Jika belum paham dengan _command_ diatas maka silahkan lihat writeup challenge [Basic ROT 13](https://github.com/cerc-undip/CTF-Learn-Writeup/tree/update/basic_rot_13_COMPLETE).

Setelah dieksekusi maka kita akan melihat kumpulan kata acak tanpa spasi. Namun di bagian tengah terdapat flag yang kita cari.

flag : `flag{CaesarIsNotSecure}`