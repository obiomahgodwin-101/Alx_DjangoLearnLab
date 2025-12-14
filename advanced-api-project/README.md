## Book API Views

This project uses Django REST Framework generic views to manage Book resources.

### Available Endpoints

- GET /api/books/  
  Returns a list of all books (public access)

- GET /api/books/<id>/  
  Returns details of a single book (public access)

- POST /api/books/create/  
  Creates a new book (authenticated users only)

- PUT /api/books/<id>/update/  
  Updates an existing book (authenticated users only)

- DELETE /api/books/<id>/delete/  
  Deletes a book (authenticated users only)

### Permissions

Read operations are open to all users.  
Write operations require authentication using DRF permission classes.

