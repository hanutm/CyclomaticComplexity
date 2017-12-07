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

class Manager:
    def __init__(self):
        self.timeStart = 0
        self.WorkerTotal = int(input('Enter total number of workers required'))
        self.WorkerCount = 0
        print('Working with unauthenticated requests')
        print('Repositories upto a maximum of 200 commits')
        response = requests.get('url to github repo')
        resp_data = jsonify(response)
        
    pass


class getRepo():
    
    pass


if __name__ == "__main__":

    managerServer = Manager()
    app.run(port=50000)                      