# BartRover
BartRover is a 6WD differential drive controlled bot built in ROS2

Build and code is based heavily on the tutorials of Articulated Robotics: https://articulatedrobotics.xyz/  (Shout-out, one of the best ROS2 tutorials out there)!

Build 002
ROS2 version: Humble

Capabilities: remote control via ros2_control, camera only sensor.  Future builds (plans) to add lidar, self navigation, etc.
Launch files for both simulation and real bot also concurrently launch foxglove_bridge.
Joystick and or keyboard launch commands optional depending on foxglove setup.

Concurrent requirements (place packages in src directory):

	diffdrive_arduino: -b humble https://github.com/joshnewans/diffdrive_arduino
 
	serial: https://github.com/joshnewans/serial

Simulation:

My launch codes (commands):
	
 	ros2 launch bartrover launch_sim.launch.py world:=./src/bartrover/worlds/neighborhood.world
 
 	[optional] sudo xboxdrv --silent
 
	[optional] ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox'
  

Real Robot:

My launch codes (commands):

	ros2 launch bartrover launch_robot.launch.py
 
	[optional] ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped
