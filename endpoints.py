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
	
