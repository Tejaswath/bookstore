# Bookstore Microservices Application

## Overview

Welcome to the **Bookstore Microservices Application**! This project is a simple, scalable web application built using a microservices architecture and deployed on Google Kubernetes Engine (GKE). It allows users to manage books and orders through a user-friendly web interface.

Live URL for the application: http://34.160.6.21.nip.io/

## Architecture

The application is composed of three main services:

1. **Book Service**
   - **Purpose:** Manages the collection of books.
   - **Functionality:** Allows adding new books and retrieving the list of available books.
   
2. **Order Service**
   - **Purpose:** Handles customer orders.
   - **Functionality:** Enables placing new orders and viewing existing orders.
   
3. **Streamlit UI**
   - **Purpose:** Provides the front-end interface for users.
   - **Functionality:** Lets users interact with the Book and Order services through a web browser.

All services communicate with each other and share a SQLite database to store persistent data.

## Technologies Used

- **Kubernetes (GKE):** Orchestrates the deployment, scaling, and management of the microservices.
- **Docker:** Containers each microservice for consistent deployment.
- **Streamlit:** Builds the web-based user interface.
- **SQLite:** Serves as the lightweight database for storing book and order information.

- **book-service/**: Contains the code and Dockerfile for the Book Service.
- **order-service/**: Contains the code and Dockerfile for the Order Service.
- **streamlit-ui/**: Contains the code and Dockerfile for the Streamlit User Interface.
- **pvc.yaml**: Defines the Persistent Volume Claim for database storage.
- **book-service.yaml**, **order-service.yaml**, **streamlit-ui.yaml**: Kubernetes deployment and service configurations for each microservice.
- **ingress.yaml**: Kubernetes Ingress configuration to expose the UI to the internet.

