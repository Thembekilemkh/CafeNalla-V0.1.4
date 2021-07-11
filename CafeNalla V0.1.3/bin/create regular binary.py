import pickle
import datetime
import os

regular = []
  
# Instance the Fernet class with the key
with open("regular.pickle", "wb") as pickle_out:
	pickle.dump(regular, pickle_out)
	print('Done')
'''  
# Open user pickle
if os.path.getsize("regular.pickle") > 0:
	with open("regular.pickle", "rb") as pickle_in:
		regular = pickle.load(pickle_in)
		print(regular)
else:
	print("The file is empty")'''