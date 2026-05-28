from fastapi import FastAPI , Request
from mockdata import product
from dtos import productDTO





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
    for oneproduct in product:
        if oneproduct.get("id") == product_id:
            return oneproduct
        
    
    return "Error ! Finding the product with the given ID ! "




#query parameters - instead of dynamic thing we will write a query for getting the value . 


# Fixed parameters 
@app.get("/greet")
def greet(name:str,age:int): # passed here 
    return { "greet" : f"Hello ! {name} welcome to the store . your age is {age}" }

#n number of parameters 

# import Request type for handeling n number of queries 
@app.get("/namaste")
async def namaste(request:Request):
    print(request.query_params) # this is object
    
# now we are taking any query request now we are not using those query parameters . 


# using query request parameters . 
@app.get("/tango")
def tango(request:Request):
    query_param = dict(request.query_params)
    print(query_param)
    
    return {
        "greet" : f"Hiii ! {query_param.get("name")} , and your age is {query_param.get("age")}"
    }
    
    


#Different types of HTTP methods 
# how to validate data - DTOS 
# How to call different HTTP methods ?

#DTO - data transfer object


@app.post("/create_products")
async def create_product(data:productDTO):
    data = data.model_dump() # model dump creates a dict like the key value pairs . 
    print(data)
    product.append(data) # adds the created product to the original product list  
    print("product added successfully")
    return {"status":"product added successfully !!!" }




@app.put("/update_product/{product_id}")

async def update_prodcut(product_data:productDTO , product_id:int):
    for index,oneproduct in enumerate(product):
        if oneproduct.get("id") == product_id:
            product[index] = product_data
            return {"status":"product updated successfully"}
    
    return {"status":"product not found in the list !!!"}