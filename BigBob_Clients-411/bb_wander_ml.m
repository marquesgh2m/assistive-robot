% bb_wander_ml.m

% Example of how to write a controller with MATLAB using the playerm
% mex interface.

% First, you have to have the MEX working - see matlab's help on this at 
% http://www.mathworks.com/help/matlab/create-mex-files.html
%
% Then, just go to $(PLAYER)/client_libs/libplayerm/src and type "make"

% Kevin Nickels July 2013

% to run player server - "player bb.cfg" in one window
% to run controller - "bb_wander_ml" in a matlab window

addpath('../libplayerm/mex'); % or wherever your mex files are

c = player_client_connect('localhost',6665);
fprintf(1,'Connected, c=%x\n',c);

pos2d = player_pos2d_connect(c,0);
sonar = player_ranger_connect(c,0);

player_pos2d_speed( pos2d, 0.0, 0.0); % pos2d,fwdSpeed,yawSpeed
player_client_read(c);

while(true)
    % update robot position/etc
    player_client_read(c);

    % get odometry information
    pose = player_pos2d(pos2d);
    fprintf('pos2d --> X=%.1f, Y=%.1f, A=%.2f\n',pose(1),pose(2),pose(3));

    % get range information (in bearing,distance, in robots CS)
    rangedata = player_ranger_range(sonar);
    
    if (length(rangedata) >3)
        fprintf('Sonar scan: ')
        for i=1:length(rangedata)
            fprintf('%.1f ',rangedata(i))
        end;
        fprintf('\n');
    end;
    
    % do simple collision avoidance
    short = 0.5;
    if (rangedata(1) < short || rangedata(3) < short)
      turnrate = -20*pi/180; % turn 20 degrees per second
    elseif (rangedata(2) <short || rangedata(4)<short)
      turnrate = +20*pi/180;
    else
      turnrate = 0;
    end;

    if (rangedata(1)<short || rangedata(2)<short)
      speed = 0;
    else
      speed = 0.200;
    end;

    % command the motors
    player_pos2d_speed( pos2d, speed, turnrate); % pos2d,fwdSpeed,yawSpeed   
end;
