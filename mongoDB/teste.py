import pymongo

client = pymongo.MongoClient("mongodb+srv://teste:teste@cluster0-irx95.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

db.posts.insert_one({"title": "My first post", "body": "This is the body of my first blog post", "slug": "first-post"})

for post in client.test.posts.find():
    print(post)