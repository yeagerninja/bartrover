# BartRover
BartRover is a 6WD differential drive controlled bot built in ROS2

Build and code is based heavily on the tutorials of Articulated Robotics: https://articulatedrobotics.xyz/
(Shout-out, one of the best ROS2 tutorials out there)!

Build 001
ROS2 version: Humble
Capabilities: remote control, camera only.  Future builds to add lidar, self navigation, etc.

Concurrent requirements (packages in src directory):
	diffdrive_arduino: https://github.com/RedstoneGithub/diffdrive_arduino
	serial: https://github.com/joshnewans/serial

Simulation:

My launch codes (commands):
	sudo xboxdrv --silent
	ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox'
	ros2 launch bartrover launch_sim.launch.py world:=./src/bartrover/worlds/neighborhood.world
