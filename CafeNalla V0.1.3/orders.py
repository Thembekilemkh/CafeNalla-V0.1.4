import pickle
import os

class Orders():
	def __init__(self):
		self.orders = []
		try:
			# Open the menu pickle
			if os.path.getsize('orders.pickle')>0:
				with open('orders.pickle', 'rb') as pickle_in:
					self.orders = pickle.load(pickle_in)
					
		except Exception as e:
			pass

	def save_new_orders(self, orders):
		with open('orders.pickle', 'wb') as pickle_out:
			pickle.dump(orders, pickle_out)

