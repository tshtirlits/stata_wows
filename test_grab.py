#!/usr/bin/python
from grab import Grab

g = Grab()
resp = g.go('http://ya.ru')
print(resp.body)

