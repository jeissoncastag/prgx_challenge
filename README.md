# Take Home Interview Challenge
We have 2 basic tables: user and address. Use the FastAPI framework and create REST services to enable user management.

## REST API requirements:
1. create users with input parameters: user (id, first_name, last_name, email and password), and addresses (id, address_1, address_2, city, state, zip code, country).
2. Retrieve users by country.

For inter-service communication, REST or gRPC calls can be used to: Retrieve user information / Sample client test code.

## Project Configuration
Below is a basic guide to configure and run the project:

### Installation
1. Clone the repository.
`git clone https://github.com/tu-usuario/nombre-del-proyecto.git`

2. Go to the project directory.
`cd project-name`.

3. Install the dependencies.
`pip install -r requirements.txt`

### Execution
1. Start the FastAPI server.
`uvicorn main:app --reload`

### Usage
- To create a user, make a POST request to `/api/users` with the user data in the body of the request in JSON format. The following is an example:
- To retrieve users by country, make a GET request to `/api/users/{country}`.

```
{
    "id": 5,
    "first_name": "Lorena",
    "last_name": "Lopez",
    "mail": "lorelo@example.com",
    "password": "password123",
    "addresses": [
        {
            "id": 5,
            "address_1": "123 St 456",
            "address_2": "Apt 12",
            "city": "Tampa",
            "state": "Florida",
            "zip": "033101",
            "country": "USA"
        }
    ]
}
```

**Step 1: Run your FastAPI application**.
Before testing your application with Postman, make sure your FastAPI application is running. To run it, open a terminal, navigate to the root directory of your project and run the following command (make sure the dependencies are installed and the server is running):

````
bash
uvicorn main:app --reload
```

This will start your application at `http://127.0.0.1:8000`.

**Step 2: Open Postman
Open the Postman application on your system. If you do not already have Postman installed, you can download and install it from [https://www.postman.com/](https://www.postman.com/).

**Step 3: Create a new application in Postman**.
- In Postman, create a new request by clicking on "New" in the upper left corner and select "Request".

**Step 4: Configure the request
- Assign a descriptive name to the request in the "Request Name" field.
- Select the appropriate HTTP method (GET, POST) from the "HTTP Method" drop-down menu.
- In the URL bar, enter the full URL of the route you want to test in your FastAPI application. For example, if you want to test the `/users` path, enter `http://127.0.0.1:8000/users`.

**Step 5: Add parameters and data (if necessary)**.
- If your request requires parameters or data in the body of the request, you can configure them in the corresponding tabs at the bottom of the Postman window.

**Step 6: Send the request
- Click the "Send" button to send the request to your FastAPI application.

**Step 7: Observe the response**
- At the bottom of the Postman window, you will see the response from your FastAPI application. This will include the HTTP status code, JSON response, or other relevant data.

**Step 8: Analyze the response**.
- Examine the response to ensure that your API is working correctly and that the data is as expected.

## Contact:
- Jeisson Andres Castaño Aguirre
- Mail: jeacastanoag@unal.edu.co
- Estadístico de la Universidad Nacional de Colombia Sede Medellín
- MBA del Tecnológico de Monterrey
