import pickle
import os

class Incoming():
	def __init__(self):
		self.incoming = []
		try:
			# Open the menu pickle
			if os.path.getsize('incomingorders.pickle')>0:
				with open('incomingorders.pickle', 'rb') as pickle_in:
					self.incoming = pickle.load(pickle_in)
					
		except Exception as e:
			pass

	def save_incoming_orders(self, incoming):
		with open('incomingorders.pickle', 'wb') as pickle_out:
			pickle.dump(incoming, pickle_out)
