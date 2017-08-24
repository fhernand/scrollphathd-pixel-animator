#!/usr/bin/env python

import time
import math
import ast

import scrollphathd

fh = open( "candle_example.js", "r" )

x = fh.read()
fh.close()

y = ast.literal_eval(x)

list = []
for s in y:
	list.append(s.splitlines())

def candle(i , j, step):
    r = float(list[step][i][j*3:j*3+3])
    return r

scrollphathd.set_brightness(0.5)
timestep = 0
while True:
    if timestep == 332:
      timestep = 0
 
    timestep = timestep + 1

    for x in range(0, scrollphathd.DISPLAY_WIDTH):
        for y in range(0, scrollphathd.DISPLAY_HEIGHT):
            v = candle(x, y, timestep)
            scrollphathd.pixel(x, y, max(0,v/255))

    time.sleep(0.001)
    scrollphathd.show()

