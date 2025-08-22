🍻 Flask Pub

A fun beginner-friendly Flask web app where you can explore a pub’s menu, place an order, leave sticky notes, and read some gossip blogs — all powered by Flask.

📂 Project Structure
flask_pub/
│── app.py                # Main Flask app
│── requirements.txt       # Python dependencies
│── README.md              # Project guide
│
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── menu.html
│   ├── order.html
│   ├── todo.html
│   ├── blog_home.html
│   ├── blog_post.html
│   ├── about.html
│   └── welcome.html
│
└── static/
    └── style.css          # Styling (CSS)

🚀 How to Run the Project
1. Clone or Download the Project

  If you already have the files, just navigate to the folder. Otherwise:
  
  git clone https://github.com/your-username/flask_pub.git
  cd flask_pub

2. Create a Virtual Environment
   a) python -m venv venv

    
   b) Activate it:
      
   On Windows (PowerShell):venv\Scripts\activate
   On Mac/Linux:source venv/bin/activate

3. Install Dependencies
   a) pip install -r requirements.txt
    
    
   If you don’t have a requirements.txt, just install Flask:
   b) pip install flask

4. Run the Flask App: python app.py

5. Open in Browser

  After running, the terminal will show something like:
  * Running on http://127.0.0.1:5000


Now open your browser and visit:
👉 http://127.0.0.1:5000

🌐 Available Routes
Route	Description
/	Home page with welcome message
/menu	See the pub’s drink menu 🍹
/order	Place a drink order 📝
/todo	Sticky notes wall 📌
/blog	Gossip hub 📰
/post/<id>	Read a single gossip post
/about	About page ℹ️
📸 Preview

When you run the app, you’ll see the Flask Pub Homepage. From there you can click links or directly go to routes like /menu, /todo, /blog, etc.

🛠️ Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS (Jinja2 Templates)
Other: Virtualenv, Python 3.x

🏆 Future Enhancements
Add a database (SQLite) for To-Do and Blog posts
Add user login & authentication
Dockerize for easy deployment
