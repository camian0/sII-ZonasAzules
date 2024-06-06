from typing import  TypeVar

T = TypeVar("T") 

class ResponseDto():
    status: int
    message: str
    data: T = None


    def toString(self)->dict:
        return {
            "status":self.status,
            "message":self.message,
            "data":self.data,
        }
