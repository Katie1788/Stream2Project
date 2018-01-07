from flask import Flask, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MOGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorsUSA'
COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False}
        #above block of code credited to Richard Dalton on slack

@app.route('/')
def home():
    return render_template('home.html')

    @app.route("/donorsUS/projects")
    def donor_projects():
        connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
        collection = connection[DBS_NAME][COLLECTION_NAME]
        projects = collection.find(projection=FIELDS, limit=55000)
        json_projects = []
        for projects in projects:
            json_projects.append(project)
            json_projects = json.dumps(json_projects
            connection.close()
            return json_projects
        #above code block credited to Richard Dalton

if __name__ == '__main__':
    app.run()
