from fastapi import FastAPI
from app.routers import expenses  # наш модуль с маршрутами
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="Expense Tracker API",
    description="API для отслеживания расходов",
    version="1.0.0"
)

# Подключаем маршруты
app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])


@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
