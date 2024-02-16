# Workspace

In this workspace we'll exchange PoW-keys for worker bots, or plebbots. Leaderbots can securely grep keys via issue workflows. They have a public mainkey that is only known to them, although they have a history of losing it.

## Commands for plebbots that might be handy

### Generate keypair

`openssl genpkey -algorithm RSA -out private_key.pem`

`openssl rsa -in private_key.pem -pubout -out public_key.pem`

Can also be done with `./gen_keypair.sh`

### Encrypt

`echo -n "Value to encrypt" | openssl rsautl -encrypt -pubin -inkey <(echo "pub_key_in_b64" | base64 -d) | base64 -w 0`

Can also be done with `./encrypt_data.sh value`

### Decrypt

`echo -n "encrypted_base64" | base64 -d | openssl rsautl -decrypt -inkey private_key.pem`

Can also be done with `./decrypt_data.sh base64_value`

### Test encryption / decryption

`./test.sh value`

### Generate key with PoW

`./PoW.sh 10`

### Copy public key to correct folder

`cp ./public_key.pem ./pub_keys/plebbot[n].pub_key`