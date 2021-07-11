import pickle
import os

class Sent():
	def __init__(self):
		self.sent = []
		try:
			# Open the menu pickle
			if os.path.getsize('sentorders.pickle')>0:
				with open('sentorders.pickle', 'rb') as pickle_in:
					self.sent = pickle.load(pickle_in)
					
		except Exception as e:
			pass

	def save_sent_orders(self, sent):
		with open('sentorders.pickle', 'wb') as pickle_out:
			pickle.dump(sent, pickle_out)
