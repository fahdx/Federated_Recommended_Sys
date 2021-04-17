import socket
import pickle

import pandas as pd
from surprise import Dataset
from surprise import Reader


from load_data import data , movielens
from recommender import algo

data3=data.build_full_trainset()
algo.fit(data3)
#
prediction = algo.predict('E', 2)
# print(prediction)
# #print(prediction.est)
#
# prediction = algo.test(data_t)
#
# print(prediction)



soc = socket.socket()
print("Socket is created.")

soc.connect(("localhost", 10000))
print("Connected to the server.")

msg = "A message from the client"
msg = pickle.dumps(msg)
soc.sendall(msg)
print("Client sent a message to the server.")

received_data = b''
while str(received_data)[-2] != '.':
    data = soc.recv(8)
    received_data += data
print(received_data)
algo2 = pickle.loads(received_data)

print(algo2)
print("Received data from the client: {received_data}".format(received_data=algo2))

algo2.fit(data3)
#
prediction = algo2.predict('E', 2)
print(prediction)


msg =algo2
msg = pickle.dumps(msg)
print(msg)
soc.sendall(msg)
print("Client sent a message to the server.")
soc.close()
print("Socket is closed.")