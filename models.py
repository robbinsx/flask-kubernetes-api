import sqlite3

class DBSchemas:
    def __init__(self):
        self.conn = sqlite3.connect('menu.db')
        self.create_menu_table()


    def create_menu_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Menu" (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Description TEXT,
            Price INTEGER,
            is_deleted boolean DEFAULT 0
        );
        """

        self.conn.execute(query)


class MenuModel:
    TABLENAME = 'Menu'

    def __init__(self):
        self.conn = sqlite3.connect('menu.db')


    def __del__(self):
        self.conn.commit()
        self.conn.close()


    def get_by_id(self, id):
        where_clause = f' AND id={id}'
        return self.list_menu(where_clause=where_clause)


    def create(self, name, description, price):
        query = f'INSERT INTO {self.TABLENAME} ' \
                f'(Name, Description, Price)' \
                f'values ("{name}", "{description}", {int(price)})'

        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    
    def list_menu(self, where_clause=''):
        query = f'SELECT id, Name, Description, Price FROM {self.TABLENAME} WHERE is_deleted != 1{where_clause};'

        print(query)
        results = self.conn.execute(query).fetchall()
        print(results)
        result = [{'id': row[0], 'name':row[1], 'description':row[2], 'price':row[3]} for row in results]
        print(result)
        return result


    def list_all_menu(self):
        query = f'SELECT id, Name, Description, Price, is_deleted FROM {self.TABLENAME};'

        print(query)
        results = self.conn.execute(query).fetchall()
        print(results)
        result = [{'id': row[0], 'name':row[1], 'description':row[2], 'price':row[3], 'deleted': row[4]} for row in results]
        print(result)
        return result

    
    def update_item(self, id, params):
        set_clause = ', '.join([f'{col} = "{val}"' for col, val in params.items()])
        query = f'UPDATE {self.TABLENAME} SET {set_clause}WHERE id = {id};'
        self.conn.execute(query)
        return self.get_by_id(id)


    def delete_item(self, id): 
        query = f'UPDATE {self.TABLENAME} SET is_deleted = 1 WHERE id = {id};'
        self.conn.execute(query)
        return self.list_menu()
