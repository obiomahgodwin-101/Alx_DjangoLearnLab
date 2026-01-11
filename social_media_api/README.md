# Social Media API

A Django REST Framework–based Social Media API that allows users to create accounts, follow other users, create posts, like posts, receive notifications, and view a personalized feed.

This project was developed as part of the **ALX Django Learn Lab**.

---

## Features

### User Management
- User registration and authentication
- User profiles
- Follow and unfollow functionality

### Posts
- Create, retrieve, update, and delete posts
- View a feed of posts from followed users
- Posts ordered by most recent first

### Likes
- Like and unlike posts
- Prevent duplicate likes
- Track user interactions with posts

### Notifications
- Notifications for:
  - New followers
  - Likes on posts
  - Comments on posts
- Endpoint to fetch user notifications

---

## Project Structure

```text
social_media_api/
├── accounts/
├── posts/
├── notifications/
├── social_media_api/
├── manage.py
└── db.sqlite3

