from flask import Flask, render_template, request
import mysql.connector
from config import Config

app = Flask(__name__)
config = Config()


def get_db_connection():
    return mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )



def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/add", methods=["GET", "POST"])
def add_feedback():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)",
                (name, email, message)
            )

            conn.commit()
            cursor.close()
            conn.close()

            return "Feedback submitted successfully"

        except Exception as e:
            return f"Error: {e}"

    return render_template("add_feedback.html")


# @app.route("/submit", methods=["POST"])
# def submit():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     message = request.form.get("message")

#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         cursor.execute(
#             "INSERT INTO feedback (name, email, message) VALUES (%s, %s, %s)",
#             (name, email, message)
#         )

#         conn.commit()
#         cursor.close()
#         conn.close()

#         return "Feedback stored successfully"

#     except Exception as e:
#         return f"Error: {e}"


if __name__ == "__main__":
    init_db()
    app.run(port=5000, debug=config.DEBUG)