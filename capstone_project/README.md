# Capstone Project – ALX Program

This project was built **from scratch during the official Capstone phase of the ALX program**.

- This is **not a weekly project**
- This is **not a reused or previous project**
- This project exists **only** to satisfy the ALX capstone requirement

---

# Capstone Project: Social Media API
**Developer:** Godwin Obiomah

## Project Overview
This project is a backend **Social Media API** built with **Django** and **Django REST Framework**.

It allows users to create posts, like posts, and receive real-time notifications using **Django signals**.  
The system is secured with authentication and permissions to ensure only authorized access.

This project demonstrates clean backend architecture and production-ready API design.

## Features Implemented
- User authentication and authorization
- Create, retrieve, and manage posts
- Like and unlike posts
- Notification system
- Automatic notifications using Django signals
- Mark notifications as read
- Unread notification count
- Protected API endpoints

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** SQLite (development)
- **Tools:** Git, GitHub, Postman

## Setup Instructions

Run the project locally using the steps below:

```bash
# Clone the repository
git clone https://github.com/obiomahgodwin-101/Alx_DjangoLearnLab.git
cd capstone_project

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python3 manage.py migrate

# Run the server
python3 manage.py runserver

