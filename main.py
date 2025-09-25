from flask import Flask
from flask_restful import Api, Resource ,reqparse , abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_UPI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.integer,primary_key=True)
    name = db.Column(db.string(100),nullable=False)
    views = db.Column(db.integer, nullable=False)
    likes = db.Column(db.integer, nullable=False)

db.create_all()

video_put_args = reqparse.RequestParser()##down below are the rules when i get an input via a url this line parses it and removes the information and the lines which are below this checks if the entry we got is in correct format or not and then it sends that to the dataset
video_put_args.add_argument("name" ,type=str, help="Name of the video")
video_put_args.add_argument("views" ,type=int, help="Views of the video")
video_put_args.add_argument("likes" ,type=int, help="Likes of the video")

names={"tim" : {"age":19 , "gender":"male"},
       "VHT":{"age":21,"gender": "male"}}

"""
class HelloWorld(Resource):
    def get(self, name):
        return names[name]

    def post(self):
        return {"data":"Posted"}
"""

videos = {}
def abort_(video_id):
    if video_id not in videos:
        abort(404, message= "Video id is not valid")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with this ID....")

class Video(Resource):
    def get(self,video_id):
        abort_(video_id)
        return videos[video_id]

    def put(self,video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_(video_id)
        del videos[video_id]
        return "", 204

api.add_resource(Video,"/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)