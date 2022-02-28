import authentication
import endpoints
import pagination
import requests

def get_group(group_id, get_users=False):
	r = requests.get(endpoints.get_group(group_id),
				headers=authentication.header)
	userless_response = r.json()

	if get_users:
		r = requests.get(endpoints.users_in_group(group_id),
					headers=authentication.header)

		def process_response(user):
			return user["id"]

		def aggregate_responses(users):
			return users

		return (userless_response,
		pagination.process(r, process_response, aggregate_responses))

	else: return userless_response

def get_all_small_groups(course_id):
	r = requests.get(endpoints.get_all_groups(course_id),
				headers=authentication.header)

	def process_response(group):
		if group["members_count"] > 4: return None
		elif "TEST" in group["name"]: return None
		return group["id"]

	def aggregate_responses(groups):
		return groups

	return pagination.process(r, process_response, aggregate_responses)

def rename_group(group_id, new_name, new_description):
	parameters = {"name": new_name, "description": new_description}
	r = requests.put(endpoints.edit_group(group_id),
				headers=authentication.header,
				data=parameters)

def set_group_membership(group_id, student_ids):
	parameters = {"members": student_ids}
	r = requests.put(endpoints.edit_group(group_id),
				headers=authentication.header,
				json=parameters)

def test_rename_group():
	import categories

	id_033 = 13713
	name = "TEST RENAMING"
	capacity = 1

	groups = categories.create_group_category(id_033, name, capacity)
	test_group = groups[0]

	rename_group(test_group, "TEST My favorite group", "Hi friend!")
	altered_group = get_group(test_group)
	assert altered_group["name"] == "TEST My favorite group"

def test_set_group_membership():
	import courses
	import categories

	id_033 = 13713
	name = "TEST ADD STUDENT"
	capacity = 1

	groups = categories.create_group_category(id_033, name, capacity)
	test_group = groups[0]

	emails_to_ids = courses.get_enrolled_emails_to_ids(id_033)
	group_members = [emails_to_ids["axie@MIT.EDU"]]
	group_members.append(emails_to_ids["quel@MIT.EDU"])

	set_group_membership(test_group, group_members)
	_group, membership = get_group(test_group, get_users=True)
	assert len(membership) == 2

def test_get_all_small_groups():
	import categories

	id_033 = 13713
	name = "TEST SMALL GROUPS"
	capacity = 1

	all_groups = categories.create_group_category(id_033, name, capacity)
	groups = get_all_small_groups(id_033)
	assert len(groups) == 0

	test_group = all_groups[0]
	rename_group(test_group, "not a test", "Hi friend!")

	groups = get_all_small_groups(id_033)
	assert len(groups) == 1
