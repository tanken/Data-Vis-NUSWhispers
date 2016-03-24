import json
import operator
import re
import csv
import sys

if __name__ == "__main__":

	with open('nuswhispers-2103162330-dump.json') as data_file:
		confessions = json.load(data_file)

	length_all = len(confessions)

	count = {}		# dictionary
	time_day = {}
	date_day = {}

	for confession in confessions:
	#for confession in confessions[0:120]:
		date_time = confession["created_at"]
		postID = confession["confession_id"]
		
		"""content = confession["content"]		# Unique Words
		#print confession["confession_id"]

		#for w in content.split():
		for w in re.findall(r"[\w#@]+", content):
			#print w
			w = w.strip(';.:!,()')
			w = w.lower()
			if w in count:
				count[w] += 1
			else:
				count[w] = 1"""

		temp = date_time.split('T')
		boolly = False
		for w in temp:
			if (boolly):						# Unique Hour
				boolly = False
				full_time = w.rstrip('.000Z')
				temp2 = full_time.split(':')
				hour = temp2[0]
				if hour in time_day:
					time_day[hour] += 1
				else:
					time_day[hour] = 1				
			else:								# Unique Day
				boolly = True
				if w in date_day:
					date_day[w] += 1
				else:
					date_day[w] = 1

	sorted_date_day = sorted(date_day.items(), key=operator.itemgetter(0))

	#print sorted_date_day
	with open('date_counts.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerow(('Date', 'Times'))
		#a.writerows(sorted_count[0:10]) # top 10
		a.writerows(sorted_date_day)

	# ===================
	# === Unique Hour ===
	# ===================

	"""sorted_time_day = sorted(time_day.items(), key=operator.itemgetter(0))
	
	with open('hour_counts.csv', 'wb') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerow(('Hour', 'Times'))
		#a.writerows(sorted_count[0:10]) # top 10
		a.writerows(sorted_time_day)"""

	# ====================
	# === Unique Words ===
	# ====================

	"""# dictionary converted to a list
	sorted_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)

	#for word, times in sorted_count:
	#	print "%s - %d times" % (word, times)

	#print sorted_count[0:9]

	with open('unique_word_counts.csv', 'wb') as fp:
	    a = csv.writer(fp, delimiter=',')
	    a.writerow(('Word', 'Times'))
	    #a.writerows(sorted_count[0:10]) # top 10
	    a.writerows(sorted_count)"""