<h1 align="center">API for customer registration</h1>

<img align="center" src="https://i.imgur.com/aII6Tvc.png" width="100%">

---
# :robot: Tecnologias Utilizadas

- Python
- FastAPI
- PostgresSQL
- SQLAlchemy
- Pytest
- Logging

# :rocket: How to Use

### 1. Clone the Repository

### 2. Run the Application Using Docker

```bash
docker-compose up -d
```

This command will launch the application in the background. Make sure you have Docker installed on your system.

### 3. Access the API

After the Docker container is up and running, you can access the API at: `http://localhost:8002/`
 
**You can also explore the interactive API documentation by navigating to: `http://localhost:8002/docs`**

### 4. Running Tests

To run tests, execute the following command in the root of the project:

```bash
pytest tests/
```

# :gear: Endpoints

#### 1. Create Customer

- **Method:** POST
- **Route:** `/customers/`
- **Summary:** Create a customer
- **Request Body:**
  - Required: Yes
  - Content:
  ```json
  {
    "name": "Example",
    "cpf": "123.456.789-09",
    "birthdate": "2024-01-08"
  }
  ```

#### 2. List All Customers

- **Method:** GET
- **Route:** `/customers/`
- **Summary:** List all customers
- **Query Parameters:**
  - `page` (Optional, Default: 1): Page of the list
  - `size` (Optional, Default: 10): Page size

#### 3. List by CPF

- **Method:** GET
- **Route:** `/customers/{cpf}/`
- **Summary:** List customer by CPF
- **Path Parameters:**
  - `cpf` (Required): Customer's CPF


