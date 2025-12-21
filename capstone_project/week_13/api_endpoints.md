API Endpoints – Capstone Project

Authentication
POST /api/auth/register/ – Register a new user
POST /api/auth/login/ – Authenticate user and return token

Posts
POST /api/posts/ – Create a new post
GET /api/posts/ – Retrieve all posts
GET /api/posts/{id}/ – Retrieve a single post
PUT /api/posts/{id}/ – Update a post
DELETE /api/posts/{id}/ – Delete a post

Likes
POST /api/posts/{id}/like/ – Like a post
DELETE /api/posts/{id}/like/ – Unlike a post

Notifications
GET /api/notifications/ – Retrieve user notifications

