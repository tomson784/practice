# 操作

masterとfollowerを立ち上げる

```
docker-compose up -d
```

コンテナにアタッチして，`source /opt/ros/melodic/setup.bash`により，ROS関連の環境変数やPathが通る．

```
env | grep ROS
```

master側で`roscore`，follower側で`rostopic list`．
ネットが繋がっていることがわかる．