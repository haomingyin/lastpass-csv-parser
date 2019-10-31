import csv

groups = {}
with open('lastpass.csv') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		groups[row[5]] = groups.get(row[5], []) + [row]

for group, rows in groups.items():
	_group = group if group else 'default'
	with open(f'{group}.csv', 'w') as csvfile:
		csvfile.write('url,username,password,extra,name,grouping,fav\n')
		csv.writer(csvfile).writerows(rows)
