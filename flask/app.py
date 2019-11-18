from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

books = [
    {
        'name' : 'Green',
        'price' : 7.99,
        'isbn' : 65655
    }, 
    {
        'name' : 'The cat',
        'price' : 6.99,
        'isbn' : 56655
    }
]

def validBookObject(bookObject):
    if ("name" in bookObject 
            and "price" in bookObject 
                and "isbn" in bookObject):
        return True
    else:
        return False

@app.route('/books')
def get_books():
    return jsonify({'books' : books})

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if(validBookObject(request_data)):
        new_book = {
            "name" : request_data['name'], 
            "price" : request_data['price'], 
            "isbn" : request_data['isbn']
        }
        books.insert(0, new_book)
        response = Response("",201, mimetype='appliacation/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        errorMsg = {
            "error" : "Invalid book object passed in request", 
            "helpString" : "Data passed similr to this {'name':'book'...}"
        }
        response = Response(json.dumps(errorMsg), status=400, mimetype='appliacation/json')
        return response

@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name' : book["name"], 
                'price' : book["price"]
            }
    return jsonify(return_value)

@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book = {
        "name" : request_data['name'], 
        "price" : request_data['price'], 
        "isbn" : isbn
    }
    i = 0
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i += 1
    response = Response("", status=204)
    return response

app.run(port=5000)