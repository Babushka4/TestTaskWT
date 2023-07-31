from fastapi import APIRouter, Request
from fastapi_users import schemas
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
import fastapi_users

from src.auth.database import User

templates = Jinja2Templates(directory="templates")

auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@auth_router.get('/registration')
def get_reg_page(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})
