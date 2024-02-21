# Import necessary modules
from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication  # Import functions from mathematics module

# Create Flask app instance
app = Flask("Mathematics Problem Solver")

# Route for addition
@app.route("/sum")
def sum_route():
    # Get 'num1' and 'num2' from query parameters
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Call the 'summation' function and return result
    result = summation(num1, num2)
    return str(result)  # Convert result to string and return

# Route for subtraction
@app.route("/sub")
def sub_route():
    # Get 'num1' and 'num2' from query parameters
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Call the 'subtraction' function and return result
    result = subtraction(num1, num2)
    return str(result)  # Convert result to string and return

# Route for multiplication
@app.route("/mul")
def mul_route():
    # Get 'num1' and 'num2' from query parameters
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Call the 'multiplication' function and return result
    result = multiplication(num1, num2)
    return str(result)  # Convert result to string and return

# Route for the main page
@app.route("/")
def render_index_page():
    return render_template('index.html')  # Render the HTML template for the main page

# Run the app if this script is executed
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Run the app on host 0.0.0.0 (accessible from outside) and port 8080
