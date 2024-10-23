from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def first_page():
    return render_template("firstpage.html", title="Три ківбаски", order="Замовлення", news="Новини", menu_pizza="Меню піццерії")

@app.get("/menu/")
def menu_list():
    return render_template("menu.html", menu="Меню", our_pizza="Наша піцца")

if __name__ == '__main__':
    app.run(port=5051, debug=True)