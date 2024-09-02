from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db=SQLAlchemy()


class Post(db.Model):
    __tablename__="post"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    description=db.Column(db.String(500))
    image=db.Column(db.String(50))
    @property
    def image_url(self):
        return url_for("static", filename=f"posts/images/{self.image}")
    
    @property
    def delete_url(self):
        return  url_for("post.delete", id=self.id)

    @property
    def show_url(self):
        return url_for("post.show", id=self.id)
    

