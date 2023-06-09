# AI-Powered API

This FastAPI application provides a RESTful API for managing users, conducting language model-based conversations, and interacting with AI models.

## Endpoints

### LLM Chain

- **GET /llm_chain**: Retrieve the current prompt for the language model.
- **POST /llm_chain**: Create a new chain for the language model.
- **GET /llm_chain/new_template**: Retrieve a new template for the language model.
- **POST /llm_chain/new_template**: Update the template for the language model.

### Chat

- **GET /conversation**: Retrieve the current conversation.
- **POST /conversation**: Send a message to the AI and get its response.
- **GET /new_conversation**: Start a new conversation.
- **POST /new_conversation**: Set a new conversation.
- **POST /save_conversation**: Save the current conversation.
- **GET /load_conversations**: Load all available conversations.
- **GET /load_conversation_by_index/{index}**: Load a conversation by its index.
- **GET /load_conversation_by_id/{chat_id}**: Load a conversation by its ID.
- **GET /chat_models**: Get a list of available chat models.
- **GET /text_models**: Get a list of available text models.
- **GET /code_models**: Get a list of available code models.
- **GET /document_models**: Get a list of available document models.
- **GET /models**: Get a list of all available models.

# Authentication

These endpoints are used for user authentication and authorization. They handle user management, including user authentication, user information retrieval, and secure data access.

## Endpoints

### POST /token

Generate an access token for a user.

**Request:**

- `UserIn` (JSON) - An object containing `username` and `password` of the user to be authenticated.

**Response:**

- A JSON object containing the generated access token and token type (bearer).

### GET /users/me

Get the current user's information.

**Request:**

- `Authorization` (Header) - The access token generated by the `/token` endpoint.

**Response:**

- `UserOut` (JSON) - An object containing the current user's `username`.

### GET /secure_data

Access secure data (available only for authenticated users).

**Request:**

- `Authorization` (Header) - The access token generated by the `/token` endpoint.

**Response:**

- A JSON object containing the secure data.

### PUT /users/update/{username}

Update a user's information.

**Request:**

- `username` (Path) - The username of the user to be updated.
- `UserUpdate` (JSON) - An object containing the updated information of the user (e.g., new password).
- `Authorization` (Header) - The access token generated by the `/token` endpoint.

**Response:**

- `UserOut` (JSON) - An object containing the updated user's `username`.

## Models

### UserIn

An object containing user authentication details:

- `username` (string) - The username of the user.
- `password` (string) - The password of the user.

### UserOut

An object containing user information:

- `username` (string) - The username of the user.

### UserCreate

An object containing user creation details:

- `username` (string) - The username of the new user.
- `password` (string) - The password of the new user.

### UserRemove

An object containing user removal details:

- `username` (string) - The username of the user to be removed.

### UserUpdate

An object containing user update details:

- `password` (Optional[string]) - The new password of the user.




# Installation and Setup

1. Clone the repository.
2. Set up a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the API using a suitable ASGI server like `uvicorn`.

## Usage

To interact with the API, you can use tools like `curl`, [HTTPie](https://httpie.io/), or a REST client like [Postman](https://www.postman.com/). You can also create a frontend application that consumes the API endpoints.


## Run the application with main.py:

```
#bash

python -m main
The application should now be running on http://127.0.0.1:5000/.
```

## You can view the API documentation by visiting the following URLs:
- Interactive API documentation: **http://127.0.0.1:5000/docs**
- Alternative ReDoc API documentation: **http://127.0.0.1:5000/redoc**

### Tests

To run the tests, use files in the `tests` directory.


#TODO

### Error handling:
Improve error handling by creating custom exceptions and handling them centrally using FastAPI's exception handlers. This helps to provide more informative and consistent error messages to the client.

### Logging:
Implement a logging system to log important events and errors. This makes it easier to debug issues and monitor the API's performance.

### Rate limiting:
Implement rate limiting to prevent abuse and protect your API from excessive requests. You can use the slowapi library for this purpose, as it integrates well with FastAPI.

### API versioning:
Implement versioning for your API to maintain backward compatibility when introducing new features or changes.

### Authentication:
Consider using more robust authentication methods, such as OAuth2 or JWT, if you haven't already.

### Authorization:
Implement role-based access control (RBAC) to manage access to various API endpoints based on user roles and permissions.

### Database integration:
If your API requires a database, integrate it with a suitable database system, such as PostgreSQL or MongoDB, using an ORM like SQLAlchemy or Tortoise-ORM.

### Testing:
Write comprehensive test cases for all your API endpoints, covering various scenarios and edge cases. Use a testing library like pytest to automate the testing process.

### Deployment:
Deploy your API to a production environment using a platform like Heroku, AWS, or Google Cloud Platform. Set up continuous integration and continuous deployment (CI/CD) using tools like GitHub Actions or GitLab CI/CD.

### Monitoring:
Implement monitoring and alerting tools to track the performance, availability, and usage of your API. You can use tools like Prometheus and Grafana for this purpose.

### Documentation:
Write clear and comprehensive documentation for your API. Use tools like Swagger UI or ReDoc to generate interactive API documentation automatically from your code. Provide examples and explanations for using each endpoint.

