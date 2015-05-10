#!/usr/bin/python

# bb_wander_cpp.py

# Example of how to write a controller with Python using the playercpp
# (C++) bindings.
# Note: The CPP bindings are NOT made by default in player.  You need
#       to do a "cd build; ccmake ." and change the
#       BUILD_PYTHONCPP_BINDINGS property to ON, then "cmake .; make ; make
#       install".  To see if this is done, search for the directory
#       containing playerc.py and see if it's also got playercpp.py in it.

# Kevin Nickels July 2013

# to run player server - "player bb.cfg" in one window
# to run controller - "python bb_wander_cpp.py" in another window

import math

def dtor (deg):
    return deg*math.pi/180.0;
    
import sys, os
# this should be whereever "playercpp.py" is.  
# On linux, you can find this out with "locate playercpp.py"
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from playercpp import *

# Make proxies for Client, Sonar, Position2d
robot = PlayerClient("localhost");
sp = RangerProxy(robot,0);
pp = Position2dProxy(robot,0);

#robot.RequestGeometry();
sp.RequestConfigure(); # fills up angle structures

while(1):
    # read from the proxies
    robot.Read()

    # sometimes you miss a scan, just start over
    if sp.GetRangeCount() < 4:
        continue;

    # print out sonars, for fun
    sonarstr="Sonar scan: "
    for i in range(sp.GetRangeCount()):
        sonarstr += '%.3f ' % sp.GetRange(i)
    print sonarstr

    # print out bearings


     # do simple collision avoidance
    short = 0.5;
    if sp.GetRange(0) < short or sp.GetRange(2)<short:
      turnrate = dtor(-20); # turn 20 degrees per second
    elif sp.GetRange(1) <short or sp.GetRange(3)<short:
      turnrate = dtor(20);
    else:
      turnrate = 0;

    if sp.GetRange(0) < short or sp.GetRange(1) < short:
      speed = 0;
    else:
      speed = 0.100;

    # command the motors
    pp.SetSpeed(speed, turnrate);

