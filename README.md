# FastAPI Blogging Platform API

## Introduction

This repository contains the source code for a simple blogging platform API built with FastAPI and MongoDB. It allows users to create, read, update, and delete blog posts, as well as comment on posts and like/dislike them.

## Prerequisites

- Python 3.9 or newer
- MongoDB instance running (local or MongoDB Atlas)
- Basic knowledge of FastAPI and Pydantic

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash git clone https://github.com/HarshRajGithub/FastAPI-Blogging-Platform.git cd fastapi-blog-api```


### Step 2: Create a Virtual Environment

Create a virtual environment to manage dependencies:

```bash python3 -m venv.venv```


Activate the virtual environment:

- On Windows:

```bash .venv\Scripts\activate```

- On macOS/Linux:

```bash source.venv/bin/activate```


### Step 3: Install Dependencies

Install the required Python packages:

```bash pip install -r requirements.txt```


### Step 4: Configure MongoDB Connection

Create a `.env` file in the root of your project and add your MongoDB connection URI:

```MONGO_URL=mongodb://user:password@host:port/database?options```

Replace `user`, `password`, `host`, `port`, and `database` with your actual MongoDB credentials and details.

### Step 5: Run the API

Start the FastAPI server using Uvicorn:

```bash uvicorn main:app --reload```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation. Access it by navigating to `http://127.0.0.1:8000/docs` in your web browser.

## Data Models

The API uses Pydantic models for data validation and serialization. The `BlogPost` and `Comment` models are defined in `main.py`.

## Additional Notes

- Ensure your MongoDB server is running and accessible at the URI specified in your `.env` file.
- This setup uses in-memory storage for simplicity. For production, consider using a persistent MongoDB deployment.
- Expand the models and endpoints as needed to support likes/dislikes functionality and other features.

