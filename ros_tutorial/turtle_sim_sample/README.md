# turtlesimを動かす

## 1つのマシンで動かす

コンテナの立ち上げ

```
docker run -p 6080:80 --shm-size=512m --name ros_melodic_gui tiryoh/ros-desktop-vnc:melodic
```
ブラウザで以下のURLを開くことでブラウザでLinuxが使える．   
http://localhost:6080/


Terminalを開いてROSのマスターを立ち上げる
```
roscore
```
別のTerminalを開いて以下のコマンドでturtleの描画
```
rosrun turtlesim turtlesim_node
```
別のTerminalを開いて以下のコマンドでturtleの描画
```
rosrun turtlesim turtle_teleop_key
```
十字キーを操作すると画面上のカメが動き出す．

## 複数コンテナ間の通信で動かす