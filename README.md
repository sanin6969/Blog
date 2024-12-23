

# Blog Post List with Country-Based Filtering

This project is a simple Django-based application that displays blog posts and allows users to toggle between viewing all posts and posts filtered by the user's country. The filtering is achieved using a utility function that determines the user's country based on their request.


## Features

* Displays a grid of blog posts with hover effects.
* Allows users to toggle between:
  * Viewing all blog posts.
  * Viewing blog posts filtered by their country.
* Modern design with Tailwind CSS for styling.
* Interactive UI with JavaScript for toggling views.

## Technologies Used

* **Backend** : Django
* **Frontend** : HTML, Tailwind CSS, and JavaScript
* **Database** : SQLite (default for Django)
* **Utilities** : Custom utility function to determine the user's country

## Setup and Installation

### Prerequisites

* Python 3.x installed on your machine.
* A virtual environment tool such as `venv` or `virtualenv`.
* Django installed (`pip install django`).

  git clone https://github.com/your-repo/blog-post-list.git
  cd blog-post-list
* python -m venv venv
  source venv/bin/activate  # For Linux/Mac
  venv\Scripts\activate     # For Windows
* pip install -r requirements.txt
* python manage.py migrate
* python manage.py runserver
* http://127.0.0.1:8000/
