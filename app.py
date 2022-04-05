from flask import *
import mysql.connector

app = Flask(__name__)

'''
conn = mysql.connector.connect(host='34.142.45.84',
                               database='reymysterio',
                               user='root',
                               password='root437root')
cursor = conn.cursor()

'''


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
