# Portfolio Project 3 — CI/CD Demo Application

A production-style Python Flask application demonstrating automated testing,
Docker containerization, and continuous integration using GitHub Actions.

## 🚀 Project Overview

This project demonstrates a basic DevOps CI pipeline where every push to the
main branch automatically:

1. Checks out the source code
2. Sets up Python 3.12
3. Installs application dependencies
4. Runs automated pytest tests
5. Builds the Docker image

## 🛠️ Technologies

- Python 3.12
- Flask
- Pytest
- Gunicorn
- Docker
- Git
- GitHub
- GitHub Actions

## 📁 Project Structure

```text
portfolio-project-3/
├── app/
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .dockerignore
├── Dockerfile
└── README.md
