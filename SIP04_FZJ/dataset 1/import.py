#!/usr/bin/env python3
import scipy.io

mat = scipy.io.loadmat('sip_data.mat', squeeze_me=True)

mat
mat.keys()
mat['Temp']
mat['Zg']
mat['Zg'].shape
mat['fm']
mat['fm'].shape
mat.keys()
mat['Ug']
mat.keys()
mat['Us']
mat.keys()


import IPython
IPython.embed()

