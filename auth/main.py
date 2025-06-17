from supabase import create_client
from fastapi import FastAPI

app = FastAPI()

supabase_url = "https://bzxbqtofhsydqxxnythj.supabase.co"
supabase_api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ6eGJxdG9maHN5ZHF4eG55dGhqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk4MjE5OTUsImV4cCI6MjA2NTM5Nzk5NX0.DdrA-hhjFYyAZBSlPAToK_CC_1o7EKPzOIpl_murS6E"

database = create_client(supabase_url, supabase_api_key)

#Read
# result = database.table("app_users").select('*').execute()

@app.get("/users")
def read_users():
    result = database.table("app_users").select('*').execute()
    return result.data

@app.post('/create')
def create_user(name,username, age, password):
    value=database.table("app_users").select("*").eq("username",username).eq("password",password).execute()
    if len(value.data)==0:  
        result = database.table('app_users').insert({
            'name': name,
            'age': age,
            'username':username,
            'password': password
        }).execute()

        return "registerd"
    else:
        return "this credentials already exsist"


@app.post('/login')
def login(username,password):
    value=database.table("app_users").select("*").eq("username",username).eq("password",password).execute()
    if len(value.data)==0:
        return False
    else :
        return True
    