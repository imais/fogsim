
class Query(object):
	def __init__(self):
		pass


class QueryClient(object):
	def __init__(self, lat, lng, dc_id, master_id):
		self.lat = lat
		self.lng = lng
		self.dc_id = dc_id
		self.master_id = master_id

		
	def __str__(self):
		return '(' + str(self.lat) + ', ' + str(self.lng) + '), dc_id = ' + str(self.dc_id) + ', master_id = ' + str(self.master_id)


	def generate_queries(self):
		pass

	
	def send_queries(self):
		pass

	
	def eval_queries(self):
		pass
	
