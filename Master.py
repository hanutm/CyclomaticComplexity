# -*- coding: utf-8 -*-
"""
Master for retrieving Git repo, assigning SHAs to workers, and returning the final cyclomatic complexity
Created on Wed Dec  6 14:53:48 2017

@author: Hanut
"""

from flask import Flask
from flask_restful import Resource,Api, reqparse
import os,sys,requests,time, json

app = Flask(__name__)
api = Api(app)


##Class to initialise all variables used by the system manager
class Manager():
    def __init__(self):
        self.timeStart = 0          ## timer variable to compute compilation time
        self.WorkerTotal = int(input('Enter total number of workers required'))     ##no. of workers available 
        self.WorkerCount = 0        ## Currently engaged workers
        print('Working with unauthenticated requests')
        print('Repositories upto a maximum of 200 commits')
        response = requests.get('url to github repo')
        resp_data = json.loads(response)
        self.commits = []               ##class commit list variable for storing all sha values
        for i in resp_data:
            self.commits.append(i['sha'])
        
        self.numCommits = len(self.commits)         ##Total number of commits
        

class getRepo():
    def __init__(self):
        global managerServer
        self.server = managerServer
        super(getRepo,self).__init__()
        self.parser = reqparser.RequestParser()
        
        ## Add relevant arguments to work be used by workers (all coming in json format)
        self.parser.add_argument('pullStatus',type = int, location = 'json')
        self.parser.add_argument('ccVal',type = float, location = 'json')
        
    
    def get(self):
        arguments = self.reqparser.parse_args()
        if arguments['pullStatus'] == True:
            print('Not Pulled')
            return {'repo':'git url'}
        else :
            print('Pulled')
            self.server.WorkerCount += 1
            if self.server.WorkerCount == self.server.WorkerTotal:
                self.server.timeStart = time.time()
            print('Number of Active Workers =',self.server.WorkerCount)
        pass
    
    def post(self):
        ##No need for post method while 
        ##fetching repository from github
        pass

class API_Cyclo():
    def __init__(self):
        global managerServer
        self.server = managerServer
        super(API_Cyclo,self).__init__()
        
        self.parser = reqparse.RequestParser()
        
        ##Add required arguments to parser
        self.parser.add_argument('sha', type = str, location = 'json')
        self.parser.add_argument('ccVal', type = float, location = 'json')
        
        
    def get(self):
        if self.server.WorkerCount < self.server.WorkerTotal:
            ##Still Waiting for all workers to join
            return {'shaVal': 'wait'}
        elif len(self.server.commits) == 0:
            ##No Commits to send to worker
            return {'shaVal' : 'no commits'}
        else:
            shaVal = self.server.commits[0]
            del self.server.commits[0]
            return {'shaVal' : shaVal}
        
    
    def post(self):
	arguments = self.reqparser.parse_args()
	self.server.commits.append({'sha':args['commitSha'], 'complexity':arguments['complexity']})

	if len(self.server.commits) == self.server.numCommits:
		endtime = time.time() - self.server.timeStart
		avgCC = 0
		for x in self.server.commits:
			avgCC += commits(x['complexity'])
	avgCC = avgCC/numCommits
	print("Overall Cyclomatic Complexity = ", avgCC)

## Add functions to API
#api.add_resource(func,extension,endpoint)

if __name__ == "__main__":

    managerServer = Manager()
    app.run(port=50000)                      
