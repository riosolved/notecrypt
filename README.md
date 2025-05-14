SETUP
---
> ./scripts/certificates/client.sh
> ./scripts/certificates/api.sh

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
