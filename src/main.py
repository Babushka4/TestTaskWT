from fastapi import FastAPI, APIRouter, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.auth.auth import auth_backend
from src.auth.auth_routers import auth_router
from src.auth.database import User
from src.auth.manager import get_user_manager
from src.auth.shemas import UserRead, UserCreate
from fastapi_users import FastAPIUsers

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory='static'), name='static')

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


# auth router
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth',
    tags=['auth']
)

# register router
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/register',
    tags=['register']
)

# base page routers
base_router = APIRouter(
    prefix='/main',
    tags=['Main']
)


@base_router.get('/posts')
def get_reg_page(request: Request):
    return templates.TemplateResponse("post.html", {"request": request})


app.include_router(auth_router)
app.include_router(base_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
