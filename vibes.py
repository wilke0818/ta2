import courses
import categories
import groups
import randomname
import spreadsheet

class StudentNotEnrolledError(Exception):
	pass

def log_start(msg):
	print(f"[+] {msg}", end="", flush=True)

def log_fail(why):
	print(f"...ERROR: {why}")

def log_ok(msg=""):
	print(f"   ---   {msg}...OK")

def vibes():
	log_start(f"reading teams from {spreadsheet.fname}")
	teams_dict = spreadsheet.mk_teams_dictionary()
	log_ok(f"imported {len(teams_dict)} tutorials")

	log_start(f"finding 6.033 on canvas")
	course_id = courses.find_6033()
	log_ok(f"course id {course_id}")

	log_start(f"getting course enrollment")
	emails_to_ids = courses.get_enrolled_emails_to_ids(course_id)
	log_ok(f"imported {len(emails_to_ids)} students")

	group_id_to_team = {}
	team_first_ent_to_tutorial = {}

	for tutorial, teams_list in teams_dict.items():
		category_name = tutorial
		category_cap = len(teams_list)

		log_start(f"creating category {category_name}")
		group_ids = categories.create_group_category(course_id,
								category_name,
								category_cap)

		log_ok(f"allocated {len(group_ids)} groups")

		for i in range(category_cap):
			group_id_to_team[group_ids[i]] = teams_list[i]
			team_first_ent_to_tutorial[teams_list[i][0]] = tutorial

	messed_up_teams = set()

	for group_id, team in group_id_to_team.items():
		tutorial = team_first_ent_to_tutorial[team[0]]
		group_name = randomname.get_name()
		group_description = f"{team} (tutorial {tutorial})"

		log_start(f"christening {group_description} \"{group_name}\"")
		groups.rename_group(group_id, group_name, group_description)
		log_ok()

		teammate_ids = []
		for teammate in team:
			log_start(f"getting user id for {teammate}")
			try: user_id = emails_to_ids[teammate]
			except KeyError:
				log_fail(f"{teammate} not enrolled!")	
				messed_up_teams.add(group_id)
				continue

			log_ok(f"{teammate} -> {user_id}")
			teammate_ids.append(user_id)

		log_start(f"adding teammates to {group_name}")
		groups.set_group_membership(group_id, teammate_ids)
		log_ok()

	print("DONE")
	print("Messed up teams:")

	for messed_up_team in messed_up_teams:
		group_name = groups.get_group(messed_up_team)["name"]
		print(f"Team {group_name}")

