from flask import Flask, request, jsonify
from models import DBSchemas
from service import MenuService

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello!'

@app.route("/<name>", methods=['GET'])
def hello_name(name):
    return f'Hello {name}!'

@app.route("/menu", methods=['GET'])
def list_menu_items():
    '''
    Lists the current menu items
    '''
    result = MenuService().list_items()
    return jsonify(result)

@app.route("/menu/all", methods=['GET'])
def list_all_menu_items():
    '''
    Lists all menu items even deleted ones 
    '''
    result = MenuService().list_all_items()
    return jsonify(result)

@app.route("/menu/<item_id>", methods=['GET'])
def show_item(item_id):
    result = MenuService().get_by_id(item_id)
    return jsonify(result)

@app.route("/menu", methods=['POST'])
def create_menu_item():
    '''
    Creates a menu item using the MenuService from the service.py file when a user navigates to the menu endpoint
    '''
    result = MenuService().create(request.get_json())
    return jsonify(result)

@app.route("/menu/<item_id>", methods=['PUT'])
def update_menu_item(item_id): 
    result = MenuService().update(item_id, request.get_json())
    return jsonify(result)

@app.route("/menu/<item_id>", methods=['DELETE'])
def delete_menu_item(item_id):
    result = MenuService().delete(item_id)
    return jsonify(result)

if __name__ == '__main__':
    DBSchemas()
    app.run(host='0.0.0.0')