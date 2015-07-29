# 0comp
This program let you compress file without loss with an infinite compression rate.

```
$> dd if=/dev/zero of=original bs=1M count=1
$> du -h original 
1.0M  original
$>
$> ./0comp.py -c original 
The compressed file has been saved in the file: AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg==
$> du -h AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg==
0  AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg==
$>
$> ./0comp.py -d AEJaaDkxQVkmU1k4VxzlAAgIQADABAAIIAAwzAUppggGxCAeLuSKcKEgcK45yg== > decompressed
$> du -h decompressed
1.0M  decompressed
$> md5sum decompressed
b6d81b360a5672d80c27430f39153e2c  decompressed
$> md5sum original 
b6d81b360a5672d80c27430f39153e2c  original
```
