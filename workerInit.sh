#!/bin/bash

cd repo

rm -rf ./git

git init

git remote add origin $1

git pull

