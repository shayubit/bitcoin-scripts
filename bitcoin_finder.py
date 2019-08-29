from bitcoin import *

def main():
	my_private_key = random_key()
	my_public_key = privtopub(my_private_key)
	my_bitcoin_address = pubtoaddr(my_public_key)

	my_history = history(my_bitcoin_address)

	if not my_history:
		return "..."
	else:
		print "You found a treasure:"
		print "Public key: " + my_public_key
		print "Private key: " + my_private_key
		print "Address: " + my_bitcoin_address

                file = open("./bitcoin.txt","w")
                file.write("Public key: " + my_public_key  + "\n")
                file.write("Private key: " + my_private_key  + "\n" )
                file.write("Address: " + my_bitcoin_address  + "\n" )
                file.close()

		return "@@@@@@@@@@ You found a treasure @@@@@@@@@@@ "


if __name__ == "__main__":

	i = 0
	treasure = main()

	while treasure == "...":
		main()
		i = i + 1
		if i == 9:
			i = 0
			print "10 tries failed"


#
# PENDING IMPROVEMENTS:
#
# - Handling errors
# - Check the correct format of a bitcoin account key after generating keys before doing more steps
#
