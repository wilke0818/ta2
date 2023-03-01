
#TODO replace with new course_id each year (literally can grab it off canvas url)
#alternative, make it an empty string and use Jay's get_033_course_id
course_id = "19476"

section_mappings = {
  "Mohammad Alizadeh TR 11am-12pm ET": "Recitation 7",
  "Mohammad Alizadeh TR 12-1pm ET": "Recitation 8",
  "Adam Belay TR 10-11am ET": "Recitation 10",
  "Adam Belay TR 11am-12pm ET": "Recitation 13",
  "Mark Day TR 10-11am ET": "Recitation 9",
  "Mark Day TR 11am-12pm ET": "Recitation 12",
  "Sam DeLaughter TR 1-2pm ET": "Recitation 16",
  "Sam DeLaughter TR 2-3pm ET": "Recitation 4",
  "Manya Ghobadi TR 1-2pm ET": "Recitation 2",
  "Manya Ghobadi TR 2-3pm ET": "Recitation 5",
  "Sam Madden TR 1-2pm ET": "Recitation 3",
  "Sam Madden TR 2-3pm ET": "Recitation 6",
  "Larry Rudolph TR 12-1pm ET": "Recitation 14",
  "Larry Rudolph TR 1-2pm ET": "Recitation 15",
  "Karen Sollins TR 10-11am ET": "Recitation 1",
  "Karen Sollins TR 11am-12pm ET": "Recitation 11",
  "Dave Larson F 2-3pm ET": "Lab 16", 
  "Michael Maune F 1-2pm ET": "Lab 15",
  "Amy Carleton F 2-3pm ET": "Lab 6",
  "Amy Carleton F 1-2pm ET": "Lab 5",
  "Jessie Stickgold-Sarah F 2-3pm ET": "Lab 2",
  "Keith Clavin F 1-2pm ET": "Lab 1",
  "Kate Parsons F 2-3pm ET": "Lab 8",
  "Kate Parsons F 1-2pm ET": "Lab 7",
  "Laura McKee F 2-3pm ET": "Lab 10",
  "Laura McKee F 1-2pm ET": "Lab 9",
  "Sarah Bates F 2-3pm ET": "Lab 12",
  "Sarah Bates F 1-2pm ET": "Lab 11",
  "Thomas Pickering F 2-3pm ET": "Lab 14",
  "Thomas Pickering F 1-2pm ET": "Lab 13",
  "Michael Trice F 2-3pm ET": "Lab 4", 
  "Michael Trice F 1-2pm ET": "Lab 3"
}

def get_useable_section_name(canvas_section):
  inverse_section_mappings = {v:k for (k,v) in section_mappings.items()}
  for partial_section in inverse_section_mappings.keys():
    if partial_section in canvas_section and canvas_section[len(partial_section)] == ' ':
      return inverse_section_mappings[partial_section]

  return ""
