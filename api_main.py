from flask import Flask, request, jsonify
import random
app = Flask(__name__)

# Out team has yet to implement the following services, so we will set them to false but in the future I would
# still like the option to enable and disable thing as part of my commitment to configurability.
enable_rng = False
enable_rnamegen = False


# Dictionary to store villagers, this may someday be replaced by a database
villagers = {}

@app.route('/new_village', methods=['POST'])
def create_new_village():
    # Generate random village data
    village_name = "Village " + str(random.randint(1, 100))
    inhabitants = random.randint(50, 200)
    buildings = random.randint(20, 50)
    village_id = random.randint(1000, 9999)

    # Construct village object
    village_data = {
        "village_id": village_id,
        "name": village_name,
        "inhabitants": inhabitants,
        "buildings": buildings
    }

    # Print and return the generated village data
    print("Generated Village Data:", village_data)
    return jsonify(village_data)

@app.route('/new_villager', methods=['POST'])
def create_new_villager():

    #some of these commented out lines are staged for later use, currently they are not useful
    #data = request.json
    # Generate random villager data
    #villager_id = random.randint(10000, 99999)
    #villager_name = data.get('name', f"Villager {villager_id}")
    #home_village = data.get('home_village', None)
    events = []

    # Construct villager object
    villager_data = {
        "villager_id": random.randint(1000, 9999),
        "name": "Villager " + str(random.randint(1, 100)),
        "home_village": "Village " + str(random.randint(1, 100)),
        "events": events
    }

    # Add villager to the dictionary
    villagers[villager_data["villager_id"]] = villager_data
    print(villagers)
    # Print and return the created villager data
    print("Created Villager Data:", villager_data)
    return jsonify(villager_data)

@app.route('/villagers', methods=['GET'])
def list_villagers():
    # Return all villagers in JSON format
    return jsonify(villagers)

@app.route('/villager_mod', methods=['POST'])
def modify_villager():
    data = request.json
    villager_id = data.get('villager_id')
    variable_to_change = data.get('variable')
    value = data.get('value')

    if villager_id in villagers:
        # Modify the specified variable of the villager
        villagers[villager_id][variable_to_change] = value
        return jsonify({"status": "Villager modified successfully"})
    else:
        return jsonify({"status": "Villager not found"}), 404

@app.route('/add_event', methods=['POST'])
def add_event_to_villager():
    data = request.json
    villager_id = data.get('villager_id')
    event = data.get('event')

    if villager_id in villagers:
        # Append event to the villager's events list
        villagers[villager_id]['events'].append(event)
        return jsonify({"status": "Event added successfully"})
    else:
        return jsonify({"status": "Villager not found"}), 404

@app.route('/undo_event', methods=['POST'])
def undo_last_event():
    data = request.json
    villager_id = data.get('villager_id')

    if villager_id in villagers:
        # Undo the last event by removing the last item from the events list
        if villagers[villager_id]['events']:
            last_event = villagers[villager_id]['events'].pop()
            return jsonify({"status": f"Event '{last_event}' undone successfully"})
        else:
            return jsonify({"status": "No events to undo"}), 400
    else:
        return jsonify({"status": "Villager not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

