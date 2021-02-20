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

複数コンテナがそれぞれノードを立ち上げ，通信して命令しあう．
|  コンテナ名  |  役割  |
| ---- | ---- |
|  ros-master  |  roscore用  |
|  ros-client  |  turtleに命令  |
|  ros-gui  |  turtlesimの描画  |

3つのコンテナを立ち上げる
```
docker-compose up -d
```
### ros-master
以下のコマンドでros-masterコンテナのシェルを立ち上げる
```
docker-compose exec ros-master bash
```
立ち上げたシェルで以下のコマンド
```
roscore
```

### ros-gui

以下のURLをブラウザで開く  
http://localhost:6080/

Terminalを開いて`rostopic list`などのコマンドでコンテナ間が通信できているか確認．  
確認出来たら，以下のコマンドにより，urtlesimの起動．
```
rosrun turtlesim turtlesim_node
```

### ros-client
以下のコマンドでros-clientコンテナのシェルを立ち上げる
```
docker-compose exec ros-client bash
```
立ち上げたシェルで以下のコマンド
```
rosrun turtlesim turtle_teleop_key
```
十字キーを操作するとros-guiで描画されているのカメが動き出す．

以下のコマンドでノード間の通信ができていることが確認できる．
```
rosrun rqt_graph rqt_graph
(rqt_graphだけでも可)
```