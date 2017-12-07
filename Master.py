# -*- coding: utf-8 -*-
"""
Master for retrieving Git repo, assigning SHAs to workers, and returning the final cyclomatic complexity
Created on Wed Dec  6 14:53:48 2017

@author: Hanut
"""

from flask import Flask, jsonify
from flask_restful import Resource,Api, reqparse
import os,sys,requests,time,getpass

app = Flask(__name__)
api = Api(app)

class Manager():
    def __init__(self):
        self.timeStart = 0          ## timer variable to compute compilation time
        self.WorkerTotal = int(input('Enter total number of workers required'))     ##no. of workers available 
        self.WorkerCount = 0        ## Currently engaged workers
        print('Working with unauthenticated requests')
        print('Repositories upto a maximum of 200 commits')
        response = requests.get('url to github repo')
        resp_data = jsonify(response)
        self.commits = []               ##class commit list variable for storing all sha values
        for i in resp_data:
            self.commits.append(i['sha'])
        
        self.numCommits = len(self.commits)         ##Total number of commits
        

class getRepo():
    def __init__(self):
        pass
    
    def get(self):
        pass
    
    def post(self):
        pass

class API_Cyclo():
    def __init__(self):
        pass
    
    def get(self):
        pass
    
    def post(self):
        pass


## Add functions to API
#api.add_resource(func,extension,endpoint)

if __name__ == "__main__":

    managerServer = Manager()
    app.run(port=50000)                      