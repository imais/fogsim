

class Datacenter(object):
	def __init__(self, lat, lng, m):
		self.lat = lat
		self.lng = lng
		self.m = m


	def __str__(self):
		return '(' + str(self.lat) + ', ' + str(self.lng) + '), m = ' + str(self.m)


class MasterNode(Datacenter):
	def __init__(self, dc):
		super(MasterNode, self).__init__(dc.lat, dc.lng, dc.m)
		self.sources = []
		

	def __str__(self):
		return super(MasterNode, self).__str__() + ', #sources = ' + str(len(self.sources))

		
	def run_opt():
		pass

	
	def request_data_tx():
		pass

		
	
	
		
