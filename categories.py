import authentication
import endpoints
import pagination
import requests

class CategoryAlreadyCreatedError(Exception):
	pass

def create_group_category(for_course, name, capacity):
	parameters = {
			"name": name,
			"self_signup": "restricted",
			"auto_leader": "random",
			"create_group_count": capacity,
	}

	r = requests.post(endpoints.category_create(for_course), 
				headers=authentication.header,
				data=parameters)

	decoded_response = r.json()
	try: category_id = decoded_response["id"]	
	except KeyError: raise CategoryAlreadyCreatedError()

	r = requests.get(endpoints.groups_in_category(category_id),
				headers=authentication.header)

	def process_response(group):
		return group["id"]

	def aggregate_responses(responses):
		return responses

	return pagination.process(r, process_response, aggregate_responses)

def test_create_group_category():
	id_033 = 13713
	name = "TEST CATEGORY"
	capacity = 14

	groups = create_group_category(id_033, name, capacity)
	assert len(groups) == 14
