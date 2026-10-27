"""
Program: Flask REST API Application
Description: Exposes basic GET and POST endpoints for JSON data exchange.
Author: Teresa Brown
References: Sourced architectural endpoint structure rules from class video 
            series guidelines ("Install basic flask with GET and POST Endpoints").
            Code structure optimized with debugging assistance from Gemini AI.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Route 1: GET /hello - Accepts an optional query parameter "name"
@app.route('/hello', methods=['GET'])
def hello_endpoint():
    # Functions & Control Flow: Fall back to "World" if name parameter is missing
    name = request.args.get('name', 'World')
    
    # Data Structures: Return a JSON response dictionary
    return jsonify({"greeting": f"Hello, {name}!"})

# Route 2: POST /sum - Adds a list of numbers sent via JSON payload
@app.route('/sum', methods=['POST'])
def sum_endpoint():
    # Error Handling: Verify that the incoming payload is valid JSON data
    data = request.get_json(silent=True)
    if not data or 'numbers' not in data:
        return jsonify({"error": "Malformed request. Missing 'numbers' field."}), 400
        
    numbers_list = data['numbers']
    
    # Control Flow: Enforce that the structural payload is an actual list of items
    if not isinstance(numbers_list, list):
        return jsonify({"error": "'numbers' must be a JSON array/list."}), 400
        
    try:
        # Data types: Calculate total mathematical balance using built-in sum()
        total_sum = sum(float(n) for n in numbers_list)
        return jsonify({"sum": total_sum})
    except (ValueError, TypeError):
        # Gracefully handle data arrays that contain non-numeric entries (like text strings)
        return jsonify({"error": "All items inside the list must be valid numbers."}), 400

if __name__ == "__main__":
    # The application runs locally on port 5000 via a single execution rule
    app.run(port=5000, debug=True)