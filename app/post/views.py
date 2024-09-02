from app.models import Post,db
from app.post import post_blueprint
from flask import render_template,request,redirect,url_for


@post_blueprint.route("", endpoint="index")
def post_index():
    posts=Post.query.all()
    return render_template("post/index.html",posts=posts)

@post_blueprint.route("<int:id>/show", endpoint="show")
def post_show(id):
    post = db.get_or_404(Post, id)
    return render_template ("post/show.html",post=post)


@post_blueprint.route("<int:id>/delete", endpoint="delete")
def post_delete(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect (url_for("post.index"))

@post_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
def post_create():
    if request.method=="POST":
        post=Post(name=request.form["name"],image=request.form["image"],description=request.form["description"])
        db.session.add(post)
        db.session.commit()

        return redirect (url_for("post.index"))
    return render_template("post/create.html")

@post_blueprint.route("<int:id>/edit", endpoint="edit", methods=["GET", "POST"])
def post_edit(id):
    post = db.get_or_404(Post, id)
    if request.method=="POST":
        post.image = request.form["image"]
        post.name=request.form["name"]
        post.description=request.form["description"]
        db.session.commit()

        return redirect (url_for("post.index"))
    return render_template("post/edit.html",post=post)
