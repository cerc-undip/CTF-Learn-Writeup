# Name
**Category:** miscellaneous
> I don't understand, I only see hello at the end
> 
> Flag={reDnAxElA si e*an ym ,u0y llet lli2 I nois*cco laic*ps a si ti sa tub tErces sI emAn ym dn*irf olleH}
> 
> Help me please!!!
---

Pada challenge **Name** kita diminta untuk mencari nama yang ada di dalam pesan "rahasia" yang disediakan.

Untuk menyelesaikan ini kita bisa menggunakan **bash script** maupun bahasa pemrograman **Python**. Namun pada writeup ini akan dijelaskan menggunakan **bash script**. Script **Python** tetap akan disediakan untuk pembelajaran.

Pesan rahasia ini dapat dengan mudah ditebak karena pesan ini hanya dibalik saja. Maka kita akan gunakan _command_ `rev` pada bash.

```bash
echo reDnAxElA si e*an ym ,u0y llet lli2 I nois*cco laic*ps a si ti sa tub tErces sI emAn ym dn*irf olleH | rev
```

Dengan perintah ini kita bisa melihat pesan aslinya, dan pada akhir kalimat kita melihat nama yang dicari (flag).

Perintah ini bisa diubah agar hanya menampilkan namanya saja dengan memotong string.
```bash
echo reDnAxElA si e*an ym ,u0y llet lli2 I nois*cco laic*ps a si ti sa tub tErces sI emAn ym dn*irf olleH | cut -d ' ' -f 1 | rev
```

flag : `AlExAnDer`