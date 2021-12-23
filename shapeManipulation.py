# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,6)))

print(a)
print(a.shape)
#shape bize oluşturulan matrisin boyutunu verir.
print(a.ravel())
a = a.ravel()
#ravel() oluşturulan matrisin tüm elemanlarını düz bir liste haline getirir.
print(a)
print(a.shape)

a = a.reshape(2,9)
#diziyi istediğimiz boyuta sokmaya yarar.
print(a)
print(a.T)
print(a.reshape(2,-1))

b = a.resize(6,3)
print(b)