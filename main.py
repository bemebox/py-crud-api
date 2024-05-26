from fastapi import FastAPI, Depends, HTTPException, status
from schemas import task as task_schema
from typing import List
from uuid import UUID, uuid4

app = FastAPI()

tasks = []


@app.post(
    "/tasks/", response_model=task_schema.Task, status_code=status.HTTP_201_CREATED
)
def create_task(_task: task_schema.Task):
    _task.id = uuid4()
    tasks.append(_task)
    return _task


@app.get("/tasks/{task_id}", response_model=task_schema.Task)
def read_task(task_id: UUID):
    for _task in tasks:
        if _task.id == task_id:
            return _task

    raise HTTPException(status_code=404, detail="Task not found!")


@app.get("/tasks/", response_model=List[task_schema.Task])
def read_tasks():
    return tasks


@app.put("/tasks/{task_id}", response_model=task_schema.Task)
def update_task(task_id: UUID, task_update: task_schema.Task):
    for index, _task in enumerate(tasks):
        if _task.id == task_id:
            update_task = _task.copy(update=task_update.dict(exclude_unset=True))
            update_task.id = _task.id #id cannot be updated
            tasks[index] = update_task
            return update_task

    raise HTTPException(status_code=404, detail="Task not found!")


@app.delete("/tasks/{task_id}", response_model=task_schema.Task)
def delete_task(task_id: UUID):
    for index, _task in enumerate(tasks):
        if _task.id == task_id:
            return tasks.pop(index)

    raise HTTPException(status_code=404, detail="Task not found!")


def main():
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
