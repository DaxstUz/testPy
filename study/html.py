#!/usr/bin/env
# -*- coding: UTF-8 -*-

l1 = ['a','b','c']
l2 = [1,2,3]
d = {}
for i in range(len(l1)):
    d.setdefault(l1[i],l2[i])
print d