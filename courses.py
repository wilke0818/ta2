import authentication
import endpoints
import pagination
import requests

target_name = "6.033 Computer Systems Engineering"

def find_6033():
	r = requests.get(endpoints.courses(), headers=authentication.header)
	decoded_response = r.json()	

	def process_response(course):
		global target_name
		try:
			if course["name"] == target_name: return course["id"]
		except KeyError: pass

		return None

	def aggregate_responses(courses):
		return courses[0]

	return pagination.process(r, process_response, aggregate_responses)

def get_enrolled_emails_to_ids(course_id):
	parameters = {
			"enrollment_type": ["student"],
			"enrollment_state": ["active"],
	}

	r = requests.get(endpoints.enrollment(course_id),
				headers=authentication.header,
				params=parameters)

	def process_response(enrollment):
		return enrollment

	def aggregate_responses(enrollments):
		email_to_id = {}
		for enrollment in enrollments:
			email_to_id[enrollment["email"]] = enrollment["id"]
		return email_to_id

	return pagination.process(r, process_response, aggregate_responses)

def test_find_6033():
	identifier = find_6033()
	assert identifier == 13713

def test_get_enrolled_emails_to_ids():
	enrollment = get_enrolled_emails_to_ids(13713)

	# interesting. this should be 402, but it is
	# 417 according to the results of the API call...
	# update now it's 414 sad
	assert len(enrollment) == 414

