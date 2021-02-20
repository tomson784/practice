# turtlebot3 simulation

turtlebot3をブラウザ上で動かす
```
docker build -t ros-gui .
docker run -p 6080:80 --shm-size=512m --name ros_melodic_gui ros-gui
```
ブラウザで以下のURLを開くことでブラウザでLinuxが使える．   
http://localhost:6080/

## 参考サイト
https://demura.net/education/16279.html  
https://qiita.com/protocol1964/items/1e63aebddd7d5bfd0d1b  