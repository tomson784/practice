FROM ros:melodic
# FROM osrf/ros:melodic-desktop-full
# http://lilaboc.work/archives/17311113.html

########## ROS setup ##########
RUN mkdir -p /home/catkin_ws/src && \
	cd /home/catkin_ws/src && \
	/bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_init_workspace" && \
	cd /home/catkin_ws && \
	/bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_make" && \
	echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc && \
	echo "source /home/catkin_ws/devel/setup.bash" >> ~/.bashrc && \
	echo "export ROS_PACKAGE_PATH=\${ROS_PACKAGE_PATH}:/home/catkin_ws" >> ~/.bashrc && \
	echo "export ROS_WORKSPACE=/home/catkin_ws" >> ~/.bashrc
######### initial position ##########
WORKDIR /home/catkin_ws