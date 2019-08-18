#!/bin/bash
echo Enter Domain Name!
read domain
echo Creating for $domain!
mkdir $domain
cd $domain
openssl genrsa -out ${domain}.key 2048
openssl req -new -key ${domain}.key -out ${domain}.csr
echo "authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = ${domain}" > ${domain}.ext
cd ..
openssl x509 -req -in ${domain}/${domain}.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out ${domain}/${domain}.crt -days 1825 -sha256 -extfile ${domain}/${domain}.ext
