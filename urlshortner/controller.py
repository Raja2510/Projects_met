from fastapi import APIRouter
from supabase import create_client
import random
import string
from fastapi.responses import RedirectResponse 
database=create_client(supabase_url='https://jnlyousreadkouyuxono.supabase.co',supabase_key='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpubHlvdXNyZWFka291eXV4b25vIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAzNjY2NDQsImV4cCI6MjA2NTk0MjY0NH0.pnH8-TtWNF1vpRhoPKykOzCDzjwnAYxMeQ9dQ9HdXmY')

router=APIRouter()

def randomstring(length=7):
    random_string="".join(random.choices(string.ascii_letters + string.digits,  k=length))
    return random_string

@router.post("/")
def create_db_entery(long_url):
    res=database.table("url").insert({
        "long_url":long_url,
        "short_url": randomstring(length=7)
    }).execute()
    return 'http://127.0.0.1:8000/'+ res.data[0]["short_url"]

@router.get("/{short}")
def redirect(short):
    redlink=database.table("url").select("long_url").eq("short_url",short).execute()
    return RedirectResponse(redlink.data[0]["long_url"])