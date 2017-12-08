# -*- coding: utf-8 -*-
"""
Worker for receiving commit sha, and calculating Cyclomatic Complexity Value
Created on Thu Dec  7 02:58:24 2017

@author: Hanut
"""

import os,sys,requests,json

def execute():
    ip = input('Enter manager server IP')
    port = input('Enter manager server port')
    reqURL = 'http://' + ip + '/' + port
    getURL = reqURL + '/repo'
    cycURL = reqURL + '/cyclo'
    getCommit = requests.get(getURL,json = {'pullStatus' : True})
    commitData = json.loads(getCommit.text)
    repoURL = commitData['repo']
    ## Pull git repo to local for evaluation
    
    ##Notify manager of pull success
    _ = requests.get(getURL,json = {'pullStatus' : False})
    
    ## GET tasks from getrepo completed
    
    
if __name__ == '__main__':
    execute()

