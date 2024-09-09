from fasthtml.common import *
from icecream import ic
from dataclasses import dataclass


class Todo:
    id: int
    title: str
    done: bool
    name: str
    details: str
    priority: int


app,rt,todos,Todo = fast_app(
    'data/todos.db',
    hdrs=[SortableJS(),Style(":root { --pico-font-size: 100%; }")],
    id=int, priority=int, title=str, done=bool, pk='id')


id_curr = 'current-todo'
def tid(id): return f'todo-{id}'


@patch
def __ft__(self:Todo):
    show = AX(self.title, f'/todo/todos/{self.id}', id_curr)
    edit = AX('edit',     f'/todo/edit/{self.id}' , id_curr)
    dt = ' ✅' if self.done else ''
    cts = Li(Button(dt, show, ' | ', edit, Hidden(id="id", value=self.id), Hidden(id="priority", value="0")))
    return Li(*cts, id=f"todo-{self.id}")

def mk_input(**kw):
    return Input(id="new-title", name="title", placeholder="New Todo", required=True, **kw)


@rt("/")
async def get():
    add = Form(Group(mk_input(), Button("Add")), hx_post="/todo/", target_id='todo-list', hx_swap="beforeend")
    frm = Form(*todos(order_by="priority"), id="todo-list", cls="sortable", hx_post="/todo/reorder", hx_trigger="end")
    card = Card(Ul(frm), header=add, footer=Div(id=id_curr)),
    title = 'Todo list'
    return Title(title), Main(H1(title), card, id="page-content")


@rt("/todos/{id}")
async def delete(id:int):
    todos.delete(id)
    return clear(id_curr)


@rt("/")
async def post(todo:Todo):
    return todos.insert(todo), mk_input(hx_swap_oob='true')


@rt("/edit/{id}")
async def get(id:int):
    res = Form(Group(Input(id="title"), Button("Save")),
        Hidden(id="id"), Hidden(id="priority"), CheckboxX(id="done", label='Done'),
        hx_put="/todo/", target_id=tid(id), id="edit")
    ic(fill_form(res, todos.get(id)))
    return fill_form(res, todos.get(id))


@rt("/")
async def put(todo: Todo):
    return todos.upsert(todo), clear(id_curr)


@rt("/reorder")
async def post(id:list[int]):
    for i,id_ in enumerate(id): todos.update({"priority":i}, id_)
    return tuple(todos(order_by="priority"))


@rt("/todos/{id}")
async def get(id:int):
    todo = todos.get(id)
    btn = Button('delete', hx_delete=f'/todo/todos/{todo.id}', target_id=tid(todo.id), hx_swap="outerHTML")
    return Div(Div(todo.title), btn)
