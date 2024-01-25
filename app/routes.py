from flask import Blueprint, request, jsonify, g
from app.models import Book, mongo, bcrypt

main = Blueprint('main', __name__)

def requires_auth(func):
    def auth_wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_credentials(auth.username, auth.password):
            return jsonify({'message': 'Invalid credentials'}), 401

        return func(*args, **kwargs)

    return auth_wrapper

def check_credentials(username, password):
    admin = mongo.db.admins.find_one({'username': username})

    if admin and bcrypt.check_password_hash(admin['password'], password):
        print("true")
        g.current_admin = admin
        return True

    return False

# Add a new book
@main.route('/books', methods=['POST'], endpoint='add_book')
@requires_auth
def add_book():
    try:
        data = request.get_json()
        new_book = Book(data['title'], data['author'], data['isbn'], data['price'], data['quantity'])
        
        # Use insert_one instead of insert
        result = mongo.db.books.insert_one({
            'title': new_book.title,
            'author': new_book.author,
            'isbn': new_book.isbn,
            'price': new_book.price,
            'quantity': new_book.quantity
        })

        if result.inserted_id:
            return jsonify({'message': 'Book added successfully'}), 200
        else:
            return jsonify({'message': 'Failed to add book'}), 500
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

# Retrieve all books
@main.route('/books', methods=['GET'], endpoint='get_all_books')
def get_all_books():
    books = mongo.db.books.find()
    book_list = []
    for book in books:
        book_list.append({
            'title': book['title'],
            'author': book['author'],
            'isbn': book['isbn'],
            'price': book['price'],
            'quantity': book['quantity']
        })
    return jsonify({'books': book_list})

# Retrieve a specific book by ISBN
@main.route('/books/<isbn>', methods=['GET'], endpoint='get_book')
def get_book_by_isbn(isbn):
    book = mongo.db.books.find_one({'isbn': isbn})
    if book:
        return jsonify({
            'title': book['title'],
            'author': book['author'],
            'isbn': book['isbn'],
            'price': book['price'],
            'quantity': book['quantity']
        })
    return jsonify({'message': 'Book not found'}), 404

@main.route('/books/<isbn>', methods=['PUT'], endpoint='update_book')
@requires_auth
def update_book(isbn):
    data = request.get_json()
    updated_book = {
        'title': data['title'],
        'author': data['author'],
        'isbn': data['isbn'],
        'price': data['price'],
        'quantity': data['quantity']
    }
    mongo.db.books.update_one({'isbn': isbn}, {'$set': updated_book})
    return jsonify({'message': 'Book updated successfully'})

@main.route('/books/<isbn>', methods=['DELETE'], endpoint='delete_book')
@requires_auth
def delete_book(isbn):
    mongo.db.books.delete_one({'isbn': isbn})
    return jsonify({'message': 'Book deleted successfully'})