from datetime import datetime
class BaseModel():
    def __init__(self, created_at= None, updated_at=None, is_deleted=False, **kwargs):
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.is_deleted = is_deleted 
    
    @property
    def created_at(self):
        return self._created_at
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at
    
    @property
    def is_deleted(self):
        return self._is_deleted
    @is_deleted.setter
    def is_deleted(self, is_deleted):
        self._is_deleted = is_deleted
    
    def __str__(self):
        return f"{self.created_at} {self.updated_at} {self.is_deleted}"

bm = BaseModel()
print(bm)
        