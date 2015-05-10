import cmd, sys
from turtle import *

from time import *

import math
from playercpp import *

import subprocess


c = PlayerClient('localhost', 6666)

p = Position2dProxy(c,0)

#r = RangerProxy(c,0)

#b = BlobfinderProxy(c,0)

while(True):
	
	c.Read()
	p.SetSpeed(1,0)
	sleep(1)
	p.SetSpeed(0,1)
	sleep(1)
	
