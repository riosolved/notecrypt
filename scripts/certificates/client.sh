
cd "$(dirname "$0")"

mkdir -p ../../certificates/client

cd ../../certificates/client

# 1. Generate a private key
openssl genpkey -algorithm RSA -out localhost.key

# 2. Create a certificate signing request (CSR) with SAN info from config
openssl req -new -key localhost.key -out localhost.csr -config ../../scripts/certificates/client.openssl.cnf

# 3. Self-sign the certificate and include SAN extension from config (valid for 365 days)
openssl x509 -req -days 365 \
  -in localhost.csr \
  -signkey localhost.key \
  -out localhost.crt \
  -extfile ../../scripts/certificates/client.openssl.cnf \
  -extensions req_ext
