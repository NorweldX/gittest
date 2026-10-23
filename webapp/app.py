from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health(): 
    return "OK"

@app.route("/")
def hello():
    return "Hello, DevOps!"

import psycopg2
@app.route("/visits")
def visits():
    conn = psycopg2.connect(host="db", port=5432, user="Igor", password="12345", dbname="User")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS visits (id SERIAL PRIMARY KEY)")
    cur.execute("INSERT INTO visits DEFAULT VALUES")
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]

    conn.commit()
    conn.close()

    return f"Visits: {count}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)