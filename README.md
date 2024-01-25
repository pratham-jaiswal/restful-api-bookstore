# RESTful API for a Bookstore Management System - Documentation

## Table of Contents
1. Adding a new book
2. Retrieving all books
3. Retrieving a specific book by ISBN
4. Updating book details
5. Deleting a book

## Adding a new book
**Endpoint:** /books

**Method:** POST

**Request:** Body should contain JSON data with book details
```.json
{
  "title": "The Life of John Doe",
  "author": "John Doe",
  "isbn": "123-4567890123",
  "price": "Rs. 123",
  "quantity": 10
}
```

**Authorization:** Basic [base64-encoded-username:password]

**Response:** Successful response (HTTP status code 200)
```.json
{
  "message": "Book added successfully"
}
```
Error response (HTTP status code 500)
```.json
{
  "message": "Failed to add book"
}
```
*or*
```.json
{
  "message": "Error ‘{parameter}’"
}
```

## Retrieving all books
**Endpoint:** /books

**Method:** GET

**Response:** Successful response (HTTP status code 200)
```.json
{
  "books": [
  {
    "title": "The Life of John Doe",
    "author": "John Doe",
    "isbn": "123-4567890123",
    "price": "Rs. 123",
    "quantity": 10
  },
  // ... other books
  ]
}
```

## Retrieving a specific book by ISBN
**Endpoint:** /books/{isbn}

**Method:** GET

**Path Parameters:**
- *isbn:* ISBN number of the book.

**Response:** Successful response (HTTP status code 200)
```.json
{
  "title": "The Life of John Doe",
  "author": "John Doe",
  "isbn": "123-4567890123",
  "price": "Rs. 123",
  "quantity": 10
}
```
Error response (HTTP status code 404)
```.json
{
  "message": "Book not found"
}
```

## Updating book details
**Endpoint:** /books/{isbn}

**Method:** PUT

**Path Parameters:**
- *isbn:* ISBN number of the book.

**Request:** Body should contain JSON data with updated book details.
```.json
{
  "title": "The Life of John Doe",
  "author": "John Doe",
  "isbn": "123-4567890123",
  "price": "Rs. 123",
  "quantity": 5
}
```
**Authorization:** Basic [base64-encoded-username:password]

**Response:** Successful response (HTTP status code 200)
```.json
{
  "message": "Book updated successfully"
}
```

## Deleting a book
**Endpoint:** /books/{isbn}

**Method:** DELETE

**Path Parameters:**
- *isbn:* ISBN number of the book.

**Authorization:** Basic [base64-encoded-username:password]

**Response:** Successful response (HTTP status code 200)
```.json
{
  "message": "Book deleted successfully"
}
```