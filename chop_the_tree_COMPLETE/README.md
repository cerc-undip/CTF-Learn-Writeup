# Chop the Three
**Category:** cryptography
> i'm a lumberjack. i just need to swing my axe to make the three fall. can you do it too?
> d2FvLCBhbG1vc3QgdGhlcmUNClpHOXVKM1FnZDI5eWNua3NJSE52YjI0TkNscHRlR2hhTTNSd1pFWTVjR014T1hwaU1UbHNXVmhPTldaUlBUMD0=
---

Pada challenge ini kita diminta untuk melakukan decoding terhadap pesan dalam bentuk Base64. Bentuk Base64 dapat dengan mudah dikenali dengan tanda "sama dengan" (`=`) di akhir. ([Baca disini](https://en.wikipedia.org/wiki/Base64))

Langsung saja kita _decode_ pesan tersebut menggunakan bash.
```bash
echo d2FvLCBhbG1vc3QgdGhlcmUNClpHOXVKM1FnZDI5eWNua3NJSE52YjI0TkNscHRlR2hhTTNSd1pFWTVjR014T1hwaU1UbHNXVmhPTldaUlBUMD0= | base64 -d
```

> wao, almost there
> ZG9uJ3Qgd29ycnksIHNvb24NClpteGhaM3RwZEY5cGMxOXpiMTlsWVhONWZRPT0=

Setelah di-_decode_ ternyata pesan ini masih memiliki pesan dalam bentuk Base64 dan terdapat pesan lain sebelumnya.

Dari kata "Three" di judul kita bisa mengetahui bahwa kemungkinan pesan rahasia ini di-_encode_ sebanyak 3 kali. Jadi, kita tidak perlu membuat script panjang seperti pada challenge [So many 64s](https://github.com/cerc-undip/CTF-Learn-Writeup/tree/master/so_many_64_COMPLETE).

Paste hasil _decoding_ sebelumnya dan _decode_ lagi sampai flag-nya ketemu.
```bash
echo ZG9uJ3Qgd29ycnksIHNvb24NClpteGhaM3RwZEY5cGMxOXpiMTlsWVhONWZRPT0= | base64 -d
echo ZmxhZ3tpdF9pc19zb19lYXN5fQ== | base64 -d
```

Setelah dilakukan _decoding_ sebanyak 3 kali maka kita dapatkan flag yang kita cari. Yoyoy.

flag : `flag{it_is_so_easy}`