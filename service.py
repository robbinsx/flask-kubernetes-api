from models import MenuModel

class MenuService:
    def __init__(self):
        self.model = MenuModel()

    def create(self, params):
        return self.model.create(params['Name'], params['Description'], params['Price'])

    def list_items(self):
        return self.model.list_menu()

    def list_all_items(self):
        return self.model.list_all_menu()

    def get_by_id(self, id):
        return self.model.get_by_id(id)

    def update(self, id, params):
        return self.model.update_item(id, params)

    def delete(self, id):
        return self.model.delete_item(id)