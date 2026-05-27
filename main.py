from fastapi import FastAPI 
from mockdata import product

app = FastAPI()

@app.get("/")
def home():
    return "Happy fastapi !!!"
@app.get("/contact")
def contact():
    return "contact us details , you can send us anything chat with us here are the contact details of the company"

@app.get("/aboutus")
def aboutus():
    return "this is about us page of ours . you ll get all the info about us by reading this page ."
@app.get("/products")





# path parameters - q - if product aviable with the id number return the product else return the error message . 

@app.get("/product/{product_id}")
def products(product_id:int): # important function as this will be usefull for mostly all the website like every company has their list of products and all 
    
    
    return {"id":product_id}


