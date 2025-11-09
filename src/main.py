import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.routers import expenses, users

app = FastAPI(
    title="Expenses App",
    description="A simple app for expenses app",
    version="1.0",
)


app.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
