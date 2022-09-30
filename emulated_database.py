from typing import Dict
from itertools import count

class DB:
    db = []
    count = count(start = 1)
    
    def insert(self, v1):
        v1['id'] = next(self.count)
        self.db.append(v1)
        
    def user_query(self, user: str):
        query = [user_register for user_register in self.db if user_register['name'] == user]
        return query if query else []
    
    def clean_db(self):
        self.db = []
        
db = DB()

def validate(user: Dict[str, str]):
    return user.get('nome', None)

def user_Register(user: Dict):
    if validate(user):
        db.insert(user)
        return True
    else:
        return False
    
