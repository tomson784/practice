# Memo

## docker command for nginx container

start up command nginx container

```bash
docker run --name my_nginx -p 8080:80 -d nginx
```

access a `http://localhost:8080/`

start shell in the container

```bash
docker exec -it my_nginx bash
```
