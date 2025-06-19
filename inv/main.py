from supabase import create_client
from fastapi import FastAPI

database_url="https://zxcinfaprezgvhgvnwyh.supabase.co"
database_api="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp4Y2luZmFwcmV6Z3ZoZ3Zud3loIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAxOTEyNzIsImV4cCI6MjA2NTc2NzI3Mn0.iEBk5TxKoIh7cPdJOb_cNyDCFyOcYwG9qUmDdFqRa2E"

database=create_client(supabase_url=database_url,supabase_key=database_api)

app =FastAPI()

# --------------supplier-----------------------------

@app.post("/supplier")
def get_supplier():
    result = database.table("supplier").select('*').execute()
    return result


@app.post("/supplier/create")
def create_supplier(name,age,contact):
    valid=database.table("supplier").select('*').eq("supplier_name",name).execute()
    if len(valid.data)==0:
        new_entry=database.table('supplier').insert(
            {
                'supplier_name':name,
                'supplier_age':age,
                'contact_info':contact
            }
        ).execute()
        return new_entry.data
    else:
        return "This person already exsist"





@app.post("/product")
def create(name,quantity,catagory):
    pass
    