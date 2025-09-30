from ninja import Router

api = Router()

@api.get('task/list/')
def task_list(request):
    return {"status": True, "message": "List of all tasks fetched!", "data": ""}


@api.get('task/{task_id}/')
def task_detail(request, task_id: int):
    return {"status": True, "message": f"Details of task {task_id} fetched!", "data": ""}

@api.post('task/create/')
def task_create(request):
    return {"status": True, "message": "New task created successfully!", "data": ""}

@api.put('task/update/{task_id}/')  
def task_update(request, task_id: int):
    return {"status": True, "message": f"Task {task_id} updated successfully!", "data": ""}

@api.delete('task/delete/{task_id}/')
def task_delete(request, task_id: int):
    return {"status": True, "message": f"Task {task_id} deleted successfully!", "data": ""}

