SETUP
---

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

API
---
- Running locally,
> ./scripts/python/run.sh --file ./api/requirements.txt

/register
curl -k https://127.0.0.1/api/register -H "Content-Type: application/json" -d '{"email":"h","password":"h"}'

/enter
curl -k https://127.0.0.1/api/enter -H "Content-Type: application/json" -d '{"email":"h","password":"h"}'

/exit
...

- Inspecting traffic
> sudo tcpdump -i any -X port 5000
