import authentication
import endpoints
import pagination
import requests

def get_user_profile(user_id):
        r = requests.get(endpoints.get_user_profile(user_id),
                                headers=authentication.header)

        return r.json() 

def get_user_avatar(user_id):
        r = requests.get(endpoints.get_user_avatar(user_id),
                                headers=authentication.header)

        def process_response(avatar):
                return avatar

        def aggregate_responses(avatar):
                return avatar

        return pagination.process(r, process_response, aggregate_responses)
