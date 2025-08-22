from flask import Flask, render_template, request

app = Flask(__name__)

# --- GOSSIP DATA (BLOG POSTS) ---
posts = {
    1: {"title": "Pub Opened!", "content": "We are now serving drinks 🍹"},
    2: {"title": "Live Music Night", "content": "Join us at 8PM 🎶"},
    3: {"title": "New Drink Alert", "content": "Mango Mojito added! 🥭"},
}

# --- TODO WALL DATA (in-memory; resets on restart) ---
tasks = []

# --- ROUTES ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/menu")
def menu():
    drinks = ["Mojito", "Beer", "Coffee", "Juice"]
    return render_template("menu.html", drinks=drinks)

@app.route("/welcome/<name>")
def welcome(name):
    return render_template("welcome.html", person=name)

@app.route("/order", methods=["GET", "POST"])
def order():
    message = None
    if request.method == "POST":
        drink = request.form.get("drink", "").strip()
        message = f"🍹 Your {drink} is on the way!" if drink else "Please enter a drink name."
    return render_template("order.html", message=message)

@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        task = request.form.get("task", "").strip()
        if task:
            tasks.append(task)
    return render_template("todo.html", tasks=tasks)

@app.route("/blog")
def blog_home():
    return render_template("blog_home.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):
    post = posts.get(id, {"title": "Not Found", "content": "No such gossip"})
    return render_template("blog_post.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
