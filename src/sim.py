from __future__ import print_function
import argparse
import json
import logging
import logging.config
import pandas as pd
import os
from data_source import *
from datacenter import *
from latlng_util import *
from query import *


log = logging.getLogger()
logging.basicConfig(level=logging.INFO)

T = 10
CITIES_FILE		= "./data/test-cities.tsv"
SOURCES_FILE	= "./data/test-sources.tsv"
MASTERS_FILE	= "./data/test-masters.tsv"
SQ_METER_TO_SQ_MI = 1.0 / (1e6 * (LatLngUtil.KM_PER_MILE**2))


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-c', '--conf', default='./conf/conf.json', type=str)
	args = parser.parse_args()
	return args


def init_conf(args):
	if os.path.exists(args.conf):
		with open(args.conf, 'rt') as f:
			# args have priority over settings in conf
			conf = dict(json.load(f).items() + vars(args).items())
	else:
		conf = args
	return conf


def init(args):
	conf = init_conf(args)
	
	cities_df = pd.read_csv(CITIES_FILE, header=0, index_col=0, sep='\t')
	cities_df['radius_mi'] = cities_df.apply(lambda city : city.land_area * SQ_METER_TO_SQ_MI / math.pi, axis=1)
	
	dcs = {}
	clients = []
	population_per_machine = conf['machine']['population']['population_per_machine']

	master_ids = [3532]  # TODO: maybe decide this depend on population per state?
	masters = {}

	for city_id, city in cities_df.iterrows():
		# Datacenters
		dcs[city_id] = Datacenter(city.lat, city.lng, city.population / population_per_machine)

		# Master nodes
		if city_id in master_ids:
			masters[city_id] = MasterNode(dcs[city_id])

		# Query clients
		clients_per_city = 3	# TODO: update this with parameter
		for i in range(0, clients_per_city):
			lat, lng = LatLngUtil.get_rand_lat_lng(city.lat, city.lng, 360, city.radius_mi)
			clients.append(QueryClient(lat, lng, city_id, master_ids[0]))

	# Data sources
	sources = {}
	sources_df = pd.read_csv(SOURCES_FILE, header=0, index_col=0, sep='\t')
	for source_id, source in sources_df.iterrows():
		source_ = DataSource(source.lat, source.lng, source.data_mb)
		sources[source_id] = source_
		masters[source.master_id].sources.append(source_)
	
	return clients, sources, dcs, masters


def main(args):
	global clients, sources, dcs, masters	
	clients, sources, dcs, masters = init(args)
	
	# for t in range(0, T):
	# 	for qc in clients:
	# 		qc.generate_queries()
	# 		qc.send_queries()
			
	# 	if 0 < t:
	# 		qc.eval_queries()
			
	# 	for mn in masters:
	# 		mn.run_opt()
	# 		mn.request_data_tx()

	print('Done!')
	print('')
		
	
if __name__ == '__main__':
	args = parse_args()
	main(args)
