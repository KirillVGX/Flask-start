from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("main.db")
conn.row_factory = sqlite3.Row
curs = conn.cursor()

curs.execute("DROP TABLE IF EXISTS cities")

curs.execute("""
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER, 
    name_ VARCHAR(50), 
    population_ INTEGER, 
    description_ TEXT, 
    year_of_foundation DATE, 
    image_ VARCHAR(255)
)
""")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (1, 'Одеса', 1000000, 'Перлина у моря', 1794, 'https://osama.com.ua/wp-content/uploads/2021/12/36.jpg')")
curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (2, 'Київ', 3000000, 'Столиця України', 430, 'https://www.nta.ua/wp-content/uploads/2022/02/kyyiv.jpg')")

conn.commit()

template = """
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <header></header>
    <main>hello</main>
    <footer></footer>
  </body>
</html>
"""

curs.execute("SELECT * FROM cities")
data = curs.fetchall()
for d in data:
    print(d)
    
@app.route("/")
def index():
    return render_template('index.html', sities=data)

@app.route('/<name>')
def print_name(name):
    return f"<h1>Hello {name} </h1>"

app.run(debug=True)