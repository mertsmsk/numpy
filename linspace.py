# -*- coding: utf-8 -*-

import numpy as np

a = np.linspace(1,10,5)
#1 den 10 a kadar eşit aralıkta 5 sayı yazdır.
#sayı miktarı verilmezse default=50 sayı üretir.
print(a)

from numpy import pi
x = np.linspace(0,2*pi,100)
print(x)
print(np.sin(x))