# Final_Build
This repo acts as a the base catkin directory for the sub's ROS packages.

Our project uses [ROS](http://wiki.ros.org/)

[CU Robosub Site](http://curobotics.org/robosub-2017)
## Requirements
### System
* Ubuntu 16.04
* ROS Kinetic - [Installation Instructions](http://wiki.ros.org/kinetic/Installation/Ubuntu)
### Hardware
* You are going to need a sub
## Set up
To get the submodules to work run these commands:
* ```git submodule init```
* ```git submodule update```
* ```./scripts/init.sh``` (Under testing still - results may vary)
* ```catkin_make```
* ```source devel/setup.bash```
## Execution
* $ roslaunch launch/main.launch

--OR--

* You may launch any sub launch file or run any script on its own. For direction see [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
## Contents
* ### launch/main.launch [Launch File Info](http://wiki.ros.org/roslaunch)
  * All other launch files are linked to this one. This means one launch file as to be started to start the sub.
  * This file also starts a bag file to record each run. [ROS bag Info](http://wiki.ros.org/Bags)
* ### scripts - Scripts to make common operations easier
  * git_add.sh - adds all changes made to the sub during a test run
  * git_pull.sh - pulls the lastest changes from all of the submodules
  * init.sh - Installs required packages
* ### src - This is where all the packages and submodules live
  * [Computer_Vision](https://github.com/CU-Robosub/Computer_Vision)
  * [Debugging-Console](https://github.com/CU-Robosub/Debugging-Console)
  * [Global_Control](https://github.com/CU-Robosub/Global_Control)
  * [Local_Control](https://github.com/CU-Robosub/Local_Control)
  * [Polou_Motor](https://github.com/CU-Robosub/Pololu_Motor)
  * [Sensor_Intergration](https://github.com/CU-Robosub/Sensor_Intergration)
  
