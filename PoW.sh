#!/bin/bash

difficulty=$1

while :
do
	./gen_keypair.sh 2>/dev/null
	bin_data=$(./encrypt_data.sh "Workspace PoW generator" 2>/dev/null | base64 -d)
	echo "Bin data:"
	echo $bin_data | xxd
	nulls=$(echo $bin_data | grep -a -o -P '\x20' | tr -d '\n' | wc -c)
	echo "Bits:"
	echo $nulls
	echo "Difficulty:"
	echo $difficulty

	if [[ $nulls -ge $difficulty ]]; then
		echo "Proof of work completed!"
	break
	else
		rm private_key.pem public_key.pem
	fi
done


