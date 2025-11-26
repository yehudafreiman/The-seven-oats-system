import csv
import io
from fastapi import UploadFile, File, HTTPException, FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Welcome to The-seven-oats-system"

@app.post("/assignWithCsv")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="File must be a CSV")

    content = await file.read()
    decoded = content.decode("utf-8")
    reader = csv.reader(io.StringIO(decoded))
    try:
        header = next(reader)
    except StopIteration:
        header = []
    soldiers = list(reader)

    class Soldier:
        def __init__(self, personal_number, first_name, last_name, gender, city, distance):
            self.personal_number = personal_number
            self.first_name = first_name
            self.last_name = last_name
            self.gender = gender
            self.city = city
            self.distance = distance

    all_soldiers = []
    for s in soldiers:
        all_soldiers.append(Soldier(personal_number=s[0], first_name=s[1], last_name=s[2], gender=s[3], city=s[4], distance=s[5]))

        def placement_logic():
            return

    return all_soldiers

@app.get("/placementSummary")
def show_summary():
    return










