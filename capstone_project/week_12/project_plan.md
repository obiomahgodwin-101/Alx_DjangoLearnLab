Capstone Project – ALX Program

Author: Godwin Obiomah

Project Overview

This capstone project is a Social Media Backend API built using Django and Django REST Framework (DRF). The project demonstrates backend engineering skills including API design, database modeling, authentication, permissions, notifications, and deployment readiness.

The application provides core social media functionality such as user authentication, post creation, liking and unliking posts, and real-time-style notifications through backend logic.

Project Idea

The project is a Social Media API that allows users to interact with posts by creating content, liking and unliking posts, and receiving notifications when interactions occur. The system is designed to be scalable, modular, and suitable for integration with a frontend or mobile application.

Main Features

User authentication and authorization

Create, retrieve, update, and delete posts

Like and unlike posts

Automatic notification generation on user interactions

Token-based authentication using Django REST Framework

RESTful API endpoints following best practices

Production-ready configuration

Django Apps Structure

The project is organized into modular Django apps with clear responsibilities:

accounts  
Handles user authentication and authorization

posts  
Manages post creation and user interactions (likes/unlikes)

notifications  
Handles notification creation and retrieval

social_media_api  
Main project configuration and global settings

Database Models Overview

User  
Represents registered users in the system

Post  
Stores user-generated content

Like  
Tracks which users liked which posts

Notification  
Stores notifications generated from user interactions

Relationships are structured to support efficient querying and data integrity using Django ORM best practices.

API Endpoints Overview

The API exposes endpoints for:

User registration and authentication

Creating and retrieving posts

Liking and unliking posts

Fetching user notifications

Endpoints follow REST principles and use appropriate HTTP methods such as GET, POST, and DELETE.

