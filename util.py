#!/usr/bin/python
#-*- coding: iso-8859-15 -*-
#NACHO MAS

def group(lst, n):
  for i in range(0, len(lst), n):
    val = lst[i:i+n]
    if len(val) == n:
      yield tuple(val)
