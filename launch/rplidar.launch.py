import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node',
            parameters=[{
                'channel_type': 'serial',
                'serial_port': '/dev/ttyRPLidar', 
                'serial_baudrate': 460800,  # Critical: C1 specific baud rate
                'frame_id': 'laser',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Standard',    # C1 typically uses 'Standard' or 'Dense'
                # Add these if supported by your specific driver build:
                #'angle_start': 45.0,  # Start angle in degrees
                #'angle_end': 315.0,   # End angle in degrees
            }],
            output='screen'
        )
    ])
