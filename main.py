from fastapi import FastAPI
from routers import task as task_route, health as health_route


app = FastAPI()
app.include_router(task_route.router, tags=["tasks"])
app.include_router(health_route.router, tags=["health"])


def main():
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
