# exHplToiMtiLng
**Category:** miscellaneous
> What is li123456789fe?
> 
> Ignore that nonsense ^
> 
> https://mega.nz/#!9ZsDFbYL!y8agy4iFlDq-MX5CCDf5fuUcwyFUOSy3A3aSLFzqXnk
---

Oke, no intro langsung saja download file-nya dan coba buka file tersebut.
```bash
eog 1234568-doesn\'t-that-bother-you.jpg
```

Saat membuka gambar kita akan mendapatkan error. Kemungkinan jenis file ini berbeda dari yang terlihat atau bahkan telah dilakukan teknik _steganografi_.

Saat kita melihat jenis file tersebut dengan perintah `file` kita tahu bahwa itu bukanlah file gambar, melainkan adalah dokumen HTML.

Selanjutnya kita ubah file tersebut menjadi `quest.html`.
```
$ file 1234568-doesn\'t-that-bother-you.jpg
1234568-doesn't-that-bother-you.jpg: HTML document, UTF-8 Unicode text, with very long lines
$ mv 1234568-doesn't-that-bother-you.jpg quest.html
```

Buka `quest.html` dengan text editor. Perhatikan disana ada flag yang kita cari. Bisa dicari dengan Ctrl+F atau jika menggunakan terminal gunakan perintah:
```bash
cat quest.html | grep -i ctf{
```

flag : `CTF{HTML=fun}`