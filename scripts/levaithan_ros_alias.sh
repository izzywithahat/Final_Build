#!/bin/bash
cd ..
(echo -n "alias leviathan='source " ;echo -n $PWD; echo -n "/devel/setup.bash";
echo "; ROS_MASTER_URI=http://10.0.0.10:11311'";) >> ~/.bash_aliases

source ~/.bashrc
