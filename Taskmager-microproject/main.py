from fastapi import FastAPI

app=FastAPI()
task=[]


@app.get("/task/get")
def get():
    return task
@app.put("/task/put")
def put(taskid,desc):
    for i in task:
        i["Task_id"]==taskid
        i[desc]=desc 
        return i
@app.post("/task/post")
def post(taskid,desc):
    for i in task:
        if i["Task_id"] == taskid:
            return "this task already exsist"
    else:
        task.append({"Task_id":taskid,"descreption":desc})
        return task
@app.delete("/task/delete")
def delete(taskid):
    for i in task:
        if i["Task_id"]==taskid:
            return task.pop(task.index(i))



