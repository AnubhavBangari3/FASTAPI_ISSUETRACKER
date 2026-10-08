from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.routes.issues import router as issues_router
from apps.middleware.timing import timing_middleware

app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
          return {"status":"ok"}


app.include_router(issues_router)
'''

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]


@app.get("/items")
def get_items():
        return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item

    return {"error": "Item not found"}

@app.post("/items")
def create_items(item: dict):
      items.append(item)
      return item

'''