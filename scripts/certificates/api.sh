
cd "$(dirname "$0")"

mkdir -p ../../certificates/api

cd ../../certificates/api

# 1. Generate a private key
openssl genpkey -algorithm RSA -out localhost.key

# 2. Create a certificate signing request (CSR) with 'localhost' as Common Name (CN)
# openssl req -new -key localhost.key -out localhost.csr -subj "/CN=localhost"
openssl req -new -key localhost.key -out localhost.csr -config ../../scripts/certificates/api.openssl.cnf

# 3. Self-sign the certificate (valid for 365 days)
openssl x509 -req -days 365 -in localhost.csr -signkey localhost.key -out localhost.crt
