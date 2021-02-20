FROM tiryoh/ros-desktop-vnc:melodic

SHELL ["/bin/bash", "-c"]

# RUN apt update -y && \
RUN mkdir -p ~/catkin_ws/src && \
    source /opt/ros/melodic/setup.bash && \
    cd ~/catkin_ws && catkin_make && \
    cd ~/catkin_ws/src && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git && \
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_gazebo_plugin.git && \
    cd ~/catkin_ws && catkin_make 

RUN echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && \
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
