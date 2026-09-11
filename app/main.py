from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape
from database.database import get_connection
from calendar_data import calendarData

app = Flask(__name__)

@app.route("/")
def show_calendar():
    return render_template(
        "calendar.html", data_by_entity = calendarData()
    )
    

# def main():
# if __name__ == "__main__":
#     main()