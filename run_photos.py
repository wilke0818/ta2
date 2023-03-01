import utils
import courses
import categories
import groups
import randomname
import spreadsheet
import sections
import users
import authentication

from PIL import Image
import requests
from io import BytesIO

def run_photos(course_id):
  sections_pics = {}
  student_pics = {} #partially redundant but allows us to limit API calls

  all_sections = sections.get_all_sections(course_id)
  ans = ''
  print(all_sections) 
  for section in all_sections:
    print(section)
    section_name = utils.get_useable_section_name(section['name'])
    if not section_name:
      print(section['name'], 'not in utils')
      continue 
    sections_pics[section_name] = {}
    enrollments = sections.get_section_enrollments(section['id'])
    for student in enrollments:
       if student['type'] != "StudentEnrollment":
         continue     
       student_name = student['user']['name']
       if student_name in student_pics.keys():
         sections_pics[section_name][student_name] = student_pics[student_name]
       else:
         profile = users.get_user_profile(student['user_id'])
         pic_response = requests.get(profile['avatar_url'], headers=authentication.header)
         if pic_response.status_code < 400:
           #TODO switch to other syntax to minimize memory issues
           #with Image.open(infile) as im:
           img = Image.open(BytesIO(pic_response.content))
           sections_pics[section_name][profile['name']] = img
         else:
           print("ERROR: no picture found")
           sections_pics[section_name][profile['name']] = None
         student_pics[profile['name']] = sections_pics[section_name][profile['name']]
#    print("Done with", section_name)
#    ans = input("show pictures? ")
#    if ans.lower() in ["y","yes"]:
#       for key, val in sections_pics[section['name']].items():
#         val.show()
  return sections_pics

#print(utils.course_id)
photos = run_photos(utils.course_id)
print(photos)
#for k,v in photos.items():
#  print(k + ':')
#  for name in v.keys():
#    print('\t', name)
