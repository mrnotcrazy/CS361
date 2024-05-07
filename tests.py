import requests


API_URL = 'http://127.0.0.1:5000'


def test_new_village():
	print("Testing /new_village route...")
	response = requests.post(f'{API_URL}/new_village')
	village_data = response.json()
	print("Response:", village_data)


def test_new_villager():
	print("Testing /new_villager route")
	response = requests.post(f'{API_URL}/new_villager')
	villager_data = response.json()
	print("Response:", villager_data)
	return villager_data.get('villager_id')


def test_villager_mod(villager_id):
	print("Testing /villager_mod route for villager ID:", villager_id)
	data = {
		"villager_id": villager_id,
		"variable": "home_village",
		"value": "New Village"
	}
	response = requests.post(f'{API_URL}/villager_mod', json=data)
	print("Response:", response.json())


def test_add_event(villager_id):
	print("Testing /add_event route for villager ID:", villager_id)
	data = {
		"villager_id": villager_id,
		"event": "Moved to new house"
	}
	response = requests.post(f'{API_URL}/add_event', json=data)
	print("Response:", response.json())


def test_undo_event(villager_id):
	print("Testing /undo_event route for villager ID:", villager_id)
	data = {
		"villager_id": villager_id
	}
	response = requests.post(f'{API_URL}/undo_event', json=data)
	print("Response:", response.json())


def test_list_villagers():
	print("Testing /villagers route to list all villagers")
	response = requests.get(f'{API_URL}/villagers')
	print("Response:", response.json())


if __name__ == "__main__":
	test_new_village()  # Test creating a new village
	village_id = test_new_villager()
	test_villager_mod(village_id)  # Use the village ID for testing villager modification
	test_add_event(village_id)  # Use the village ID for testing adding events
	test_list_villagers()
	test_undo_event(village_id)  # Use the village ID for testing undoing events
	test_list_villagers()
