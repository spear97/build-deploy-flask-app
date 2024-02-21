# Building and Deploying a Web App using Flask

This is a simple Flask application that provides endpoints for basic mathematical operations: addition, subtraction, and multiplication. The application allows users to input two numbers and get the result of the specified operation.

## Installation

To run this application, follow these steps:

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2. Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Starting the Server
Run the Flask application with the following command:
```bash
python app.py
```
The server will start on http://0.0.0.0:8080/.

### Endpoints
-`/sum`: Endpoint for addition. Pass num1 and num2 as query parameters to get the sum.
Example: http://0.0.0.0:8080/sum?num1=5&num2=3 will return 8.
-`/sub`: Endpoint for subtraction. Pass num1 and num2 as query parameters to get the subtraction.
Example: http://0.0.0.0:8080/sub?num1=10&num2=4 will return 6.
-`/mul`: Endpoint for multiplication. Pass num1 and num2 as query parameters to get the multiplication.
-`/`: Main page to interact with the application. This page provides a simple UI to input numbers and perform operations.

### Structure
- `app.py`: Contains the Flask application code with the defined routes.
- `Maths/mathematics.py`: Module with functions for `summation`, `subtraction`, and `multiplication`.
- `templates/index.html`: HTML template for the main page with input fields and buttons.
- `static/mywebscript.js`: JavaScript file with functions to handle operations and display results dynamically.
  
### Dependencies
- Flask: A lightweight WSGI web application framework.
- Bootstrap (CDN): Used for styling the HTML template.
