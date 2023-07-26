from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)  # This enables CORS for all routes.

# Your route and other code here...
@app.route('/store', methods=['POST'])
def store_data():
    data = request.get_json()
    email = data['email']
    # Here, you can store the email in a file or database.
    # For simplicity, we'll just print the email for now.
    print('Received email:', email)
    return jsonify(message='Email stored successfully.')
if __name__ == '__main__':
    app.run(debug=True)
