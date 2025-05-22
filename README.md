SETUP
---
> ./scripts/setup.sh

CERTIFICATES
---
Generate:
> ./scripts/certificates/client.sh
> ./scripts/certificates/api.sh

Trust:
- WSL
    > ADDING:
        > sudo cp ./api/localhost.crt /usr/local/share/ca-certificates/api.localhost.crt
            > curl https://api.localhost/api/register -H "Content-Type: application/json" -d '{"email":"h","password":"h"}'":"h"}'
            ```
            {
            "message": "User registered successfully."
            }
            ```
        > sudo cp ./client/localhost.crt /usr/local/share/ca-certificates/client.localhost.crt
            > curl https://client.localhost
            ```
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <script type="module" src="/@vite/client"></script>

                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <div id="application"></div>
                <script type="module" src="/index.js"></script>
            </body>
            </html>
            ```
        > ls /usr/local/share/ca-certificates
        > sudo update-ca-certificates
    > REMOVING:
        > sudo rm /usr/local/share/ca-certificates/api.localhost.crt
        > sudo rm /usr/local/share/ca-certificates/client.localhost.crt
        > sudo update-ca-certificates --fresh
- Windows:
    > Open `certmgr.msc`
    > Go to Trusted Root Certification Authorities -> Certificates
    > Import:
        > <WSL::PROJECT_ROOT>/certificates/api/localhost.crt
        > <WSL::PROJECT_ROOT>/certificates/client/localhost.crt

Debug:
- WSL:
    > openssl s_client -connect localhost:443 -servername client.localhost -showcerts
    > openssl s_client -connect localhost:443 -servername api.localhost -showcerts
    > openssl x509 -in /usr/local/share/ca-certificates/api.localhost.crt -noout -text | grep -A1 "Subject Alternative Name"
            ```
            X509v3 Subject Alternative Name:
                DNS:api.localhost, DNS:localhost
            ```
    > openssl x509 -in /usr/local/share/ca-certificates/client.localhost.crt -noout -text | grep -A1 "Subject Alternative Name"
            ```
            X509v3 Subject Alternative Name:
                DNS:client.localhost, DNS:localhost
            ```
RUN
---
> ./scripts/docker/start.sh
> ./scripts/docker/stop.sh

API
---
- Running locally:
```
NOTE:
In Windows, for WSL to connect to MariaDB, modify "bind-address" in [mysqld] to "0.0.0.0" in,
    - "C:\Program Files\MariaDB 11.4\data\my.ini"

Execute in windows MariaDB client,
GRANT ALL PRIVILEGES ON *.* TO 'root'@'host.docker.internal' IDENTIFIED BY 'secret';
FLUSH PRIVILEGES;

NOTE: 10.0.0.78 is from Windows' ipconfig > Ethernet adapter Ethernet > IPv4 Address

ENVIRONMENT="local" \
SESSION_SECRET_KEY=YKVw2xySAE704cjgFvYu7JqkO6Eglt0OdjqvFf4G6ww \
PERSISTENCE_USER="root" \
PERSISTENCE_PASSWORD="secret" \
PERSISTENCE_HOST="10.0.0.78" \
PERSISTENCE_PORT="3306" \
PERSISTENCE_DATABASE="api" \
./scripts/python/run.sh --file ./api/requirements.txt
```

- Endpoints:
> /register
    > curl -X POST http://127.0.0.1:5000/api/account/register -H "Content-Type: application/json" -d '{"email":"h","password":"h"}'
> /enter
    > curl -k https://127.0.0.1/api/enter -H "Content-Type: application/json" -d '{"email":"h","password":"h"}'
> /exit
    > ...

- DEBUG:
    > Inspecting traffic:
        > sudo tcpdump -i any -X port 5000

RESOURCES
---
- https://app.kontext.tech/project/tools/article/docker-with-wsl-2-ssl-proxy-and-ssl-certificate-problem
