
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from fasthtml.common import *
from collections import namedtuple

from apps.nav.nav import app as nav
from apps.todo.todo import app as todo
from apps.h2f.h2f import app as h2f
from apps.card3d.card3d import app as card3d

apps = FastAPI()

@apps.get("/", response_class=RedirectResponse)
def homepage(request: Request) -> RedirectResponse:
    return RedirectResponse("/nav/", status_code=301)


#@apps.post("/")
#async def post(request: Request): return {"message": "", "root_path": request.scope.get("root_path")}

nav = nav
todo = todo
h2f = h2f
card3d = card3d

apps.mount("/nav", nav)
apps.mount("/todo", todo)
apps.mount("/h2f", h2f)
apps.mount("/card3d", card3d)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:apps", host="0.0.0.0", port=8000, reload=True, access_log=True)
