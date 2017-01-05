#!/usr/bin/env python
# -*- coding: UTF-8 -*-

while True:
    reply = raw_input('Enter text:')
    if reply == 'stop':break
    if(reply.isdigit()):
        print int(reply)**10
    else:
        print reply.upper()
print 'bye'
