def courses():
	return "https://canvas.mit.edu/api/v1/courses"

def category_create(course_id):
	root = "https://canvas.mit.edu/api/v1/courses/"
	suffix = "/group_categories"
	return f"{root}{course_id}{suffix}"

def groups_in_category(category_id):
	root = "https://canvas.mit.edu/api/v1/group_categories/"
	suffix = "/groups"
	return f"{root}{category_id}{suffix}"

def edit_group(group_id):
	root = "https://canvas.mit.edu/api/v1/groups/"
	return f"{root}{group_id}"

def get_group(group_id):
	return edit_group(group_id)

def get_all_groups(course_id):
	root = "https://canvas.mit.edu/api/v1/courses/"
	suffix = "/groups"
	return f"{root}{course_id}{suffix}"

def enrollment(course_id):
	root = "https://canvas.mit.edu/api/v1/courses/"
	suffix = "/users"
	return f"{root}{course_id}{suffix}"

def users_in_group(group_id):
	root = "https://canvas.mit.edu/api/v1/groups/"
	suffix = "/users"
	return f"{root}{group_id}{suffix}"


def get_all_sections(course_id):
	root = "https://canvas.mit.edu/api/v1/courses/"
	suffix = "/sections"
	return f"{root}{course_id}{suffix}"


def get_section_enrollments(section_id):
        root = "https://canvas.mit.edu/api/v1/sections/"
        suffix = "/enrollments"
        return f"{root}{section_id}{suffix}"


def get_user_profile(user_id):
        root = "https://canvas.mit.edu/api/v1/users/"
        suffix = "/profile"
        return f"{root}{user_id}{suffix}"

def get_user_avatar(user_id):
        root = "https://canvas.mit.edu/api/v1/users/"
        suffix = "/avatars.json"
        return f"{root}{user_id}{suffix}"
