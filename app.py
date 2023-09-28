from flask import Flask, render_template


app = Flask(__name__)

from blog.views import blog_blueprint
app.register_blueprint(blog_blueprint)

from main.views import main_blueprint
app.register_blueprint(main_blueprint)

from users.views import users_blueprint
app.register_blueprint(users_blueprint)


if __name__ == '__main__':
    app.run()
