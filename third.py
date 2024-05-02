from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - dictionary to store user information
users = {
    1: {'name': 'Alice', 'age': 25},
    2: {'name': 'Bob', 'age': 30},
    3: {'name': 'Charlie', 'age': 35}
}

# Route to get user information by ID
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({'error': 'User not found'}), 404

# Route to update user information by ID
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id] = data
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
