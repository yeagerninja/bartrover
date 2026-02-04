#import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():


    return LaunchDescription([

        Node(
            package='camera_ros',
            executable='camera_node',
            name='camera',
            parameters=[{
                'width': 640,
                'height': 480,
                'format': 'YUYV',   # Pixel format
                'role': 'video',    # video, view, or raw
                'camera': 0        # Index of the camera
            }]
        ),
        
        # # The republish node to create compressed images
        #Node(
        #    package='image_transport',
        #    executable='republish',
        #    name='republish_node',
        #   # Pass command line arguments before --ros-args
        #    arguments=['raw', 'compressed'], 
        #    remappings=[
        #        # Remapping the input raw image topic
        #        ('in', '/camera/image_raw'),
        #        # Remapping the output compressed image topic
        #        ('out/compressed', '/camera/image_compressed')
        #    ],
        #    parameters=[
        #        # Setting the transport type parameter
        #        {'image_transport': 'compressed'}
        #    ],
        #    output='screen'
        #)
    ])
