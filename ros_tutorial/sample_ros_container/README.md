# 操作

## コンテナ間のネットワークが繋がっているかの確認

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

## docker-compose 操作

複数コンテナの立ち上げ．
```
docker-compose up -d
```

立ち上げたコンテナの削除
```
docker-compose down
```

コンテナ内のシェルの立ち上げ
```
docker-compose exec [container name] bash
```
