from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .repository import CommentsRepository, Comment

app = FastAPI()
repository = CommentsRepository()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request, start: int = 1, end: int = 10):
    cmnts = repository.get_all()
    start_index = (start - 1) * end
    last_index = start_index + end
    paginated_cmnts = cmnts[start_index:last_index]
    paginated_cmnts = paginated_cmnts[::-1] 
    return templates.TemplateResponse("index.html", {"request": request, "comments": paginated_cmnts})


@app.get("/add/message")
def add_message(request: Request):
    return templates.TemplateResponse("comments/comment.html", {"request": request})


@app.post("/add/message")
def add_message(request: Request, message: str = Form(...), type: str = Form(...)):

    repository.save(Comment(ctg=type, msg=message))
    return RedirectResponse("/", status_code = 303)

