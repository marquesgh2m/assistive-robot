#!/usr/bin/python

# bb_wander.py

# Example of how to write a controller with Python using the playerc
# bindings.
# Pablo Tarquino June 2013

# to run player server - "player bb.cfg" in one window
# to run controller - "python bb_wander_c.py" in another window

import sys,os,math
# this should be whereever "playerc.py" is.  
# On linux, you can find this out with "locate playerc.py"
sys.path.append('/usr/local/lib/python2.7/site-packages/')
from playerc import *


import math
def dtor (deg):
    return deg*math.pi/180.0;


# Create a client object
c = playerc_client(None, 'localhost', 6665)

# Connect it
if c.connect() != 0:
  raise playerc_error_str()

# Create a proxy for position2d:0
p = playerc_position2d(c,0)
if p.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise playerc_error_str()

# Retrieve the geometry
if p.get_geom() != 0:
  raise playerc_error_str()
print 'Robot size: (%.3f,%.3f)' % (p.size[0], p.size[1])

# Create a proxy for sonar ranger:0
s = playerc_ranger(c,0)
if s.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise ValueError(playerc_error_str())

# Retrieve the geometry
if s.get_geom() != 0:
  raise playerc_error_str()

print 'Sonar pose: (%.3f,%.3f,%.3f)' % (s.device_pose.px,s.device_pose.py,s.device_pose.pz)

# start going forward
p.set_cmd_vel(0.2, 0.0, 00.0 * math.pi / 180.0, 1)


# read once to get things going
if c.read() == None:
  raise playerc_error_str()

while (1):
  # read the sensors, etc.
    if c.read() == None:
        raise playerc_error_str()


  # always check scan_count before trying to access scan[*]
    if s.ranges_count < 4:
      continue;

    sonarstr = 'Sonar scan: '
    for j in range(s.ranges_count):
        sonarstr += '%.3f ' % s.ranges[j]
    print sonarstr

    # do simple collision avoidance
    short = 0.5;
    if s.ranges[0] < short or s.ranges[2]<short:
        turnrate = dtor(-20); # turn 20 degrees per second
    elif s.ranges[1] <short or s.ranges[3]<short:
        turnrate = dtor(20);
    else:
        turnrate = 0;

    if s.ranges[0] < short or s.ranges[1] < short:
        speed = 0;
    else:
        speed = 0.100;

# command the motors
    p.set_cmd_vel(speed,0.0,turnrate,1);
