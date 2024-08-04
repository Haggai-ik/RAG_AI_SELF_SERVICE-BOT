from pydantic import BaseModel



class question(BaseModel):
     question : str

class answer(BaseModel):
     answer : str
