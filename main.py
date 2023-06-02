from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

url = "https://error-test-mk.azurewebsites.net/api/HttpTriggerOpen?"

@app.get("/")
async def root():
    my_response = requests.get(url)
    #print(my_response)
    return {"message": "Hello World " + str(my_response.status_code)}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)