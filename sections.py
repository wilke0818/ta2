import authentication
import endpoints
import pagination
import requests

def get_all_sections(course_id):
	r = requests.get(endpoints.get_all_sections(course_id),
				headers=authentication.header)

	def process_response(section):
		return section

	def aggregate_responses(sections):
		return sections

	return pagination.process(r, process_response, aggregate_responses)


def get_section_enrollments(section_id):
        r = requests.get(endpoints.get_section_enrollments(section_id),
                                headers=authentication.header)

        def process_response(enrollment):
                return enrollment

        def aggregate_responses(enrollment):
                return enrollment

        return pagination.process(r, process_response, aggregate_responses)
