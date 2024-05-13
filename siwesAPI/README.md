<picture> <source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/HYdh2YO.png"> <source media="(prefers-color-scheme: light)" srcset="https://i.imgur.com/HYdh2YO.png"> <img alt="README image" src="https://i.imgur.com/HYdh2YO.png"> </picture>

# SIWES LOGBOOK API
The SIWES (Students Industrial Work Experience Scheme) API provides a platform for managing logbook entries for students undergoing their industrial training. It supports operations for creating, retrieving, updating, and deleting log entries associated with students, schools, departments, companies, and supervisors. This API is ideal for educational institutions, students, and companies participating in SIWES programs.

### Features
* **Student Management**: Add, update, retrieve, and delete student records.
* **School Management**: Manage school details.
* **Department Management**: Handle departmental information within schools.
* **Company Management**: Manage company profiles linked to student internships.
* **Logbook Management**: Students can create, retrieve, update, and delete entries in their logbooks based on their daily activities.
* **Date Restrictions**: Students can only fill the logbook for today and future dates.
* **Overwrite Existing Entries**: If a student fills the logbook for a date already filled, the API overwrites the existing entry with the new data.
* **Search/Filter Functionality**: Search for logs by based on date range and/or work status

### Technology Stack
* **FastAPI**: As the web framework for building APIs.
* **SQLAlchemy**: For ORM.
* **SQLite**: As the database for local development.
* **Pydantic**: For data validation.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
- Clone the repository
```
git clone https://github.com/Hordunlarmy/APIs
cd APIs/siwesAPI
```
- Set up a virtual environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```
### Install dependencies
`pip install -r requirements.txt`

### Environment Setup
Create a file named .env in the root directory and add environment-specific variables:
```
database = sqlite:///./blog.db
```
### Running the Application
Start the server with:
`python3 main.py`
This command starts the application with live reloading enabled, which is useful during development.

### Program Logic
The application is structured around MVC architecture, where:

* **Models** are defined using SQLAlchemy ORM. These models represent User, Post, and Comment.
* **Controllers** (or routes) are defined in FastAPI. Each route handles specific logic for processing requests and returning responses.
* **Views** are represented by Pydantic models which validate and serialize request and response data.

### Documentation
For full documentation, visit http://localhost:8000/docs after starting the server. This will provide access to an interactive Swagger UI where you can test all API endpoints.

## Running with Docker
To run this project using Docker, run `docker-compose up --build`
