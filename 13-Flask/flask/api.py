## put and delete -- HTTP verbs
## Working with API's-- json

from flask import Flask, jsonify, request   

app = Flask(__name__)

## initial data in my to do list 
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web', 
    }
]

@app.route('/')
def Home():
    return "Welcome to the to do list app"

## Get: Retrieve all the items 

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

## get: retireve aspecific item by id
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}),
    return jsonify(task)

## Post: add a new item to the list
@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Title is required'}), 400
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'description': request.json.get('description', "")
    }
    tasks.append(new_task)
    return jsonify(new_task)

## Put: update an existing item
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):   
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'})
    if not request.json:
        return jsonify({'error': 'Request body must be JSON'})
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    return jsonify(task)
## Delete: remove an item from the list
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'result': 'Task deleted'})


if __name__ == "__main__":
    app.run(debug=True)