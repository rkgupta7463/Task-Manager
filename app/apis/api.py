from ninja import Router,Schema
from app.auth import JWTAuth
from app.models import *

api = Router(tags=["Tasks"])

@api.get('tasks/',auth=JWTAuth())
def task_list(request,offset:int=0,limit:int=10):
    user=request.auth
    tasks=Task.objects.filter(created_by=user)
    tasks=tasks[offset:offset + limit]
    data=[task.serializer() for task in tasks]
    return {"status": True, "message": "List of all tasks fetched!", "data": data}


@api.get('tasks/{task_id}/')
def task_detail(request, task_id: int):
    try:
        task=Task.objects.get(id=task_id)
        return {"status": True, "message": f"Details of task {task_id} fetched!", "data": task.serializer()}
    except Exception as e:
        return {"status": False, "message": f"Task {task_id} not found!", "data": ""}


class TaskSchema(Schema):
    title:str
    description:str
    completed:bool=False


@api.post('tasks/',auth=JWTAuth())
def task_create(request,payload:TaskSchema):  
    task=Task.objects.create(
        title=payload.title,
        description=payload.description,
        completed=payload.completed,
        created_by=request.auth
    )
    return {"status": True, "message": "New task created successfully!", "data": task.serializer()}


@api.put('tasks/{task_id}/',auth=JWTAuth())  
def task_update(request, task_id: int,payload:TaskSchema):
    user=request.auth
    try:
        task=Task.objects.get(id=task_id,created_by=user)
        if task:
            task.title=payload.title
            task.description=payload.description
            task.completed=payload.completed
            task.save()
            return {"status": True, "message": f"Task {task_id} updated successfully!", "data": task.serializer()}
        else:
            return {"status": False, "message": f"Task {task_id} not found!", "data": ""}
    except Exception as e:
        return {"status": False, "message": f"Task {task_id} not found!", "data": ""}


@api.delete('tasks/{task_id}/',auth=JWTAuth())
def task_delete(request, task_id: int):
    user=request.auth
    try:
        task=Task.objects.get(id=task_id,created_by=user)
        if task:
            task.delete()
            return {"status": True, "message": f"Task {task_id} deleted successfully!", "data": task.serializer()}
        else:
            return {"status": False, "message": f"Task {task_id} not found!", "data": ""}

    except Exception as e:
        return {"status": False, "message": f"Task {task_id} not found!", "data": ""}

class MarkCompletedSchema(Schema):
    completed:bool=False

@api.patch('mark/tasks/{task_id}/',auth=JWTAuth())
def mark_completed(request,task_id:int,payload:MarkCompletedSchema):
    user=request.auth
    try:
        task=Task.objects.get(id=task_id,created_by=user)
        if task:
            task.completed=payload.completed
            task.save()
            return {"status": True, "message": f"Task {task_id} completed flage updated to {task.completed} successfully!", "data": task.serializer()}
        else:
            return {"status": False, "message": f"Task {task_id} not found!", "data": ""}
    
    except Exception as e:
        return {"status": False, "message": f"Task {task_id} not found!", "data": ""}

