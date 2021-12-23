# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)
print(a)

b = a #bu işlem koplayama yapmaz. bellekte aynı yere işaret ederler!
print(b)
print(a[2])
print(b[2])

b[0]=100
print(a)
print(b)

#dizilerde kopyalama yapmak için copy fonksiyonu kullanılır!
c = a.copy()
print(c)
c[0]=1000
print(a)
print(c)

d = a.view() #işlem yapıldığı zaman iki dizi de etkilenir ancak yinede bellekteki yerleri farklıdır.
print("****")
print(a)
print(d)
d[0]=250
print(a)
print(d)
d.shape = 2,5
print(a)
print(d)
a[0]=123
print(a)
print(d)








