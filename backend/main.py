from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import date
import json
import datetime

from backend.logic import get_day_order

app = FastAPI()

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


def load_data():
    with open("backend/holidays.json", "r") as f:
        return json.load(f)


@app.get("/api/today")
def today():
    data = load_data()

    semester_start = datetime.date.fromisoformat(
        data["semester_start"]
    )

    day_order, working = get_day_order(
        today=date.today(),
        semester_start=semester_start,
        cycle_length=data["cycle_length"],
        holidays=data["holidays"]
    )

    return {
        "date": str(date.today()),
        "working_day": working,
        "day_order": day_order
    }