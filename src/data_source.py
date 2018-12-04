
class DataSource(object):

	def __init__(self, lat, lng, data_mb):
		self.lat = lat
		self.lng = lng
		self.data_mb = data_mb
		self.dest_dc_ids = []	# destination DCs
		
		
	def __str__(self):
		return '(' + str(self.lat) + ', ' + str(self.lng) + '), data_mb = ' + str(self.data_mb) + ', dest_dcs = ' + str(self.dest_dc_ids)
