from ninja import Router

api = Router()

@api.get('task/list/')
def task_list(request):
    return {"status": True, "message": "List of all tasks fetched!", "data": ""}
