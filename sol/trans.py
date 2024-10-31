from solathon import Client

# https://solathon.vercel.app/clients/client?ref=defiplot.com#send_transaction

client = Client("https://api.mainnet-beta.solana.com")

# sender = Keypair.from_private_key("your_private_key")
# receiver = PublicKey("receiver_public_key")
# amount = 100
#
# instruction = transfer(
#     from_public_key=sender.public_key,
#     to_public_key=receiver,
#     lamports=100
# )
#
# transaction = Transaction(instructions=[instruction], signers=[sender])
#
# result = client.send_transaction(transaction)
info = client.get_account_info("8q3PiifMQxnjs1NAETVXw8xMVN8q3Zfuoops9BSjpump")
print("Balance: ", info)
# print("Transaction response: ", result)
