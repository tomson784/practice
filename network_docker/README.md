# Memo

`docker-compose.yml`にて，サーバーごとにIPを割り振った．  
`nginx.conf`の`proxy_pass`にも割り振ったIPを設定．  
各URLにアクセスすることができた．  
http://localhost/server_1  
http://localhost/server_2


`ping`が通ることも確認（ただし，同じネットワーク内のサーバーである必要がある）．
```
ping 172.30.0.2
ping 172.30.0.3
```