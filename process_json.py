import json

if __name__ == "__main__":

	with open('nuswhispers-2103162330-dump.json') as data_file:
		confessions = json.load(data_file)

		length_all = len(confessions)

		#for confession in confessions:
		for confession in confessions[0:5]:
			content = confession["content"]
			#print confession["confession_id"]