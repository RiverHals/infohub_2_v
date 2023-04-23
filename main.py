from fastapi import FastAPI
from routers import docs, process_control, process_status, process_result

app = FastAPI()

@app.get("/")
async def read_root():
    return "Server is running"

app.include_router(docs.router)
app.include_router(process_control.router)
app.include_router(process_status.router)
app.include_router(process_result.router)
