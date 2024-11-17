# Invoice Management API

This project is a Django REST Framework-based API for managing invoices and their details. It supports creating and updating invoices with nested invoice details in a single request. This API is containerized using Docker, making it easy to set up and run.
>[![django](https://img.shields.io/badge/Django-092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)](https://www.python.org/)
[![docker](https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://hub.docker.com/r/zeroxeli/readme-ai)
---

## Features

- **Create Invoice**: Add a new invoice with multiple line items.
- **Update Invoice**: Modify an existing invoice and its details.
- **Nested Serializer**: Handles validation for both invoices and their details.
- **Custom Response Messages**: Consistent API responses for success and error handling.
- **Dockerized**: Simplified deployment using Docker and Docker Compose.
- **Thunder Client Setup**: Pre-configured collection and environment for API testing.

---

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your system.
- Thunder Client extension installed in VS Code (optional but recommended).

---

### Clone Repository

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Dhanshree019/Invoice-Generation-API.git
   cd Invoice-Generation-API

---

## Running the Application With Docker Setup Or With Mannual Setup

### Docker Setup
1. **Build and Start the Container**:
   ```bash
   docker-compose up --build

2. **Access the API**:
   ```bash
   http://127.0.0.1:8000/

2. **Stop the Container**:
   ```bash
   docker-compose down

### Mannual Setup

1. **Create a virtual environment and activate it**:
   ```bash
   mkvirtualenv invoice

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Apply migrations to set up the database**:
   ```bash
   python manage.py migrate

4. **Start the development server**:
   ```bash
   python manage.py runserver
---

### Thunderclinet Setup
1. Import the provided Thunder Client Collection (thunder-collection_Invoice Generation.json) and Environment (thunder-environment_Invoice Environment.json) into Thunder Client.
2. Instructions:
Open Thunder Client in VS Code.
- Navigate to Collections → Import → Select the thunder-collection.json file.
- Navigate to Environments → Import → Select the thunder-environment.json file.

3. Test the API using Thunder Client:
- The collection includes POST and PUT requests for the API.
- Use the environment BASE_URL for a consistent API base URL.

---

## API Endpoints
### Create Invoice
- URL: /api/invoices/
- Method: POST

### Update Invoice
- URL: /api/invoices/<'id'>/
- Method: PUT