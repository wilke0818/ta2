import authentication
import requests

def process(r, process_callback, aggregate_callback):
	everything = []

	decoded_response = r.json()
	for item in decoded_response:
		callback_result = process_callback(item)
		if callback_result is not None:
			everything.append(callback_result)

	while r.links.get("next") is not None:
		next_endpoint = r.links["next"]["url"]
		r = requests.get(next_endpoint, headers=authentication.header)
		decoded_response = r.json()

		for item in decoded_response:
			callback_result = process_callback(item)
			if callback_result is not None:
				everything.append(callback_result)

	return aggregate_callback(everything)
	
