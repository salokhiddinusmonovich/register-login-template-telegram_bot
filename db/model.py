from db.connect import DB

class Users(DB):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
