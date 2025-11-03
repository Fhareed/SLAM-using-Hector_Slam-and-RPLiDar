
Overview

This project demonstrates a Simultaneous Localization and Mapping (SLAM) system built using Hector SLAM with an RPLiDAR sensor on a Raspberry Pi 4.
The goal is to enable real-time 2D mapping and localization for indoor navigation, without requiring odometry data from wheel encoders.

The project showcases an affordable and lightweight ROS-based mapping pipeline suitable for mobile robots, autonomous vehicles, and educational research in robotics.


 Features

	•	Real-time 2D map generation using RPLiDAR A1/A2 sensors.
	•	Implemented on ROS Noetic (Ubuntu 20.04).
	•	Uses Hector SLAM for mapping based on LIDAR scan matching.
	•	No need for wheel odometry — purely relies on scan data.
	•	Runs efficiently on Raspberry Pi 4 (4 GB).
	•	Integrated RViz visualization for live map monitoring.
	•	Modular ROS nodes for plug-and-play use with other sensors or robots.

  Installation

1. Clone the repository

cd ~/catkin_ws/src
git clone https://github.com/Fhareed/SLAM-using-Hector_Slam-and-RPLiDar.git
cd ~/catkin_ws
catkin_make

2. Install dependencies

sudo apt-get install ros-noetic-hector-slam
sudo apt-get install ros-noetic-rplidar-ros

3. Connect your RPLiDAR

ls /dev/ttyUSB*
sudo chmod 666 /dev/ttyUSB0

4. Launch the mapping nodes

roslaunch rplidar_ros rplidar.launch
roslaunch hector_slam_launch tutorial.launch

5. Visualize in RViz
rosrun rviz rviz

The commands used are:

roslaunch rplidar_ros rplidar_a3.launch
roslaunch rplidar_ros view_rplidar_a3.launch

roslaunch room_mapper run_all.launch

roslaunch hector_slam_launch tutorial.launch

Author

Farid Oladega
Master’s student in Sustainable and Autonomous Systems
University of Vaasa | University of Konstanz
oladegafarid@outlook.com￼
