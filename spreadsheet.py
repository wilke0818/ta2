import csv

fname = "resources/team_assignments.csv"

def mk_teams_dictionary():
	global fname

	def process_entry(tutorials_to_teams, team_row):
		metagroup_name = "DP Teams: Tutorial " + team_row[0]

		team_members = []
		for teammate in team_row[1:]:
			if teammate != '': team_members.append(teammate)

		try: tutorials_to_teams[metagroup_name].append(team_members)
		except KeyError:
			tutorials_to_teams[metagroup_name] = [team_members]

	tutorials_to_teams = {}

	with open(fname, newline='') as csvf:
		teams_reader = csv.reader(csvf)
		for team_row in teams_reader:
			process_entry(tutorials_to_teams, team_row)

	return tutorials_to_teams

def test_teams_dictionary():
	teams_dictionary = mk_teams_dictionary() 	
	
	test_row = teams_dictionary["DP Teams: Tutorial 2"]
	assert len(test_row) == 9
	assert len(test_row[0]) == 3

