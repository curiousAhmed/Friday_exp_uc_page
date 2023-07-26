from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ucpage.html')

@app.route('/store', methods=['POST'])
def store_email():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        if email:
            # Do something with the email data (e.g., store it in a database)
            # For demonstration, we'll just return the email back to the client
            return jsonify({'message': f'Received email: {email}'}), 200
        else:
            return jsonify({'message': 'Email not provided'}), 400
    else:
        return jsonify({'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
