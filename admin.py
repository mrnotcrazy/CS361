import argparse
import requests

API_URL = "http://127.0.0.1:5000"


def create_new_village():
	response = requests.post(f"{API_URL}/new_village")
	print(response.json())


def create_new_villager():
	response = requests.post(f"{API_URL}/new_villager")
	print(response.json())


def modify_villager(villager_id, variable, value):
	data = {"villager_id": villager_id, "variable": variable, "value": value}
	response = requests.post(f"{API_URL}/villager_mod", json=data)
	print(response.json())


def add_event_to_villager(villager_id, event):
	data = {"villager_id": villager_id, "event": event}
	response = requests.post(f"{API_URL}/add_event", json=data)
	print(response.json())


def undo_last_event(villager_id):
	data = {"villager_id": villager_id}
	response = requests.post(f"{API_URL}/undo_event", json=data)
	print(response.json())


def list_villagers():

	response = requests.get(f'{API_URL}/villagers')
	print(response.json())


def main():
	parser = argparse.ArgumentParser(description="Admin interface for the village API")
	subparsers = parser.add_subparsers(dest='command')

	parser_new_village = subparsers.add_parser('new_village')
	parser_new_villager = subparsers.add_parser('new_villager')

	parser_mod_villager = subparsers.add_parser('mod_villager')
	parser_mod_villager.add_argument('-id', required=True, type=int, help="Villager ID")
	parser_mod_villager.add_argument('-var', required=True, type=str, help="Variable to modify")
	parser_mod_villager.add_argument('-value', required=True, type=str, help="New value for variable")

	parser_add_event = subparsers.add_parser('add_event')
	parser_add_event.add_argument('-id', required=True, type=int, help="Villager ID")
	parser_add_event.add_argument('-event', required=True, type=str, help="Event to add")

	parser_undo_event = subparsers.add_parser('undo_event')
	parser_undo_event.add_argument('-id', required=True, type=int, help="Villager ID")

	parser_list_villagers = subparsers.add_parser('list_villagers')

	args = parser.parse_args()

	if args.command == 'new_village':
		create_new_village()
	elif args.command == 'new_villager':
		create_new_villager()
	elif args.command == 'mod_villager':
		modify_villager(args.id, args.var, args.value)
	elif args.command == 'add_event':
		add_event_to_villager(args.id, args.event)
	elif args.command == 'undo_event':
		undo_last_event(args.id)
	elif args.command == 'list_villagers':
		list_villagers()


if __name__ == "__main__":
	main()
