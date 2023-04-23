from pydantic import BaseModel

class Process(BaseModel):
     name : str = "python process.py"
     # process should be presented as a python file