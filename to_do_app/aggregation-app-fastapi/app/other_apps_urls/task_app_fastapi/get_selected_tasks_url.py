import httpx
import json

async def get_selected_tasks_url(tasks_ids: list):
    list_of_tasks_ids = []
    for _ in tasks_ids:
        list_of_tasks_ids.append(_['id'])
    
    tasks_ids = {'tasks_ids': list_of_tasks_ids}
    
    url = f'http://task-app-fastapi/task/selected'

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=tasks_ids)
        print(response.content)
    return json.loads(response.content)