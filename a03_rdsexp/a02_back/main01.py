from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
import uvicorn
import database01
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
# 절대 경로를 사용하여 템플릿 경로 오류(TemplateNotFound) 방지
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "../a01_front"))



# http://127.0.0.1:8000/
@app.get("/")
async def heroList(request:Request):
    return templates.TemplateResponse(request=request, name="a02_hero.html")


# http://127.0.0.1:8000/api/heros
@app.get("/api/heros")
def get_heros(hero_name:str = "", job_class:str=""):
    return database01.select_heros(hero_name,job_class)



# 4. main() 실행시, 메모리에 로딩할 코드 처리..
if __name__ == "__main__":
    # 서버 실행 
    uvicorn.run("main01:app", host="127.0.0.1", port=8000, reload=True)    
