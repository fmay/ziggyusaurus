--- 
title: Docker Compose
---

## Level 1
For a [Level 1 cluster](/user-guide/cluster/levels) a typical `docker-compose.yaml` is shown below. Note the (optional) use of Caddy for automatic Let's Encrypt certificates. 

```yaml
services:
  caddy:
    image: caddy:2.10-alpine
    restart: unless-stopped
    cap_add:
      - NET_ADMIN
    ports:
      - "80:80"
      - "443:443"
      - "443:443/udp"
    volumes:
      - $PWD/Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data
      - caddy_config:/config
    networks:
      - app-network

  db:
    image: postgres:16
    restart: unless-stopped
    # Remove ports to prevent all access
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: ziggy
      POSTGRES_PASSWORD: ziggy
      POSTGRES_DB: ziggy
    volumes:
      - ziggy_db:/var/lib/postgresql/data
      - ./db-init:/docker-entrypoint-initdb.d/
    networks:
      - app-network

  redis:
    image: redis:8.2-alpine
    restart: always
    # Remove ports to prevent all access
    ports:
      - "6379:6379"
    command: redis-server /etc/redis/redis.conf
    volumes:
      - ./redis.conf:/etc/redis/redis.conf:ro
    networks:
      - app-network

  api:
    image: ziggy-api-arm
    restart: unless-stopped
    depends_on:
      - redis
      - db
    env_file:
      - .env
    volumes:
      - /home/ubuntu/ziggy/files:/home/ubuntu/ziggy/files
    networks:
      - app-network

  client:
    image: ziggy-client-arm
    restart: unless-stopped
    depends_on:
      - api
    networks:
      - app-network

volumes:
  caddy_data:
  caddy_config:
  ziggy_files:
  ziggy_db:

networks:
  app-network:
    driver: bridge
```

## Level 2
For a [Level 2 cluster](/user-guide/cluster/levels) `docker-compose.yaml` should not contain `db` or `redis`.

You will then need to adjust the `.env` file to point to your clusters.

The following entries should be adjusted.

```dotenv
APP_DATABASE=postgresql://ziggy:ziggy@db:5432/ziggy
TENANT_DATABASE=postgresql://ziggy:ziggy@db:5432/ziggy_tenant
REDIS=redis://:ziggy@redis:6379
```