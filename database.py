import firebase_admin
from firebase_admin import db,credentials
import requests
import json
from dotenv import load_dotenv
import os
import datetime

load_dotenv()
CLIST_UNAME = os.getenv('CLIST_UNAME')
CLIST_KEY = os.getenv('CLIST_KEY')
DB_URL = os.getenv('DB_URL')
TS = str(datetime.datetime.now()).replace(" ",'T')

key_set= {
	'atcoder.jp', 
	'codedrills.io', 
	'kaggle.com',
	'ctftime.org', 
	'codechef.com',   
	'quora.com',  
	'aigaming.com', 
	'codingcompetitions.withgoogle.com', 
	 'hackerrank.com',
	 'uva.onlinejudge.org',
	 'binarysearch.com', 
	 'yukicoder.me', 
	 'icpc.global', 
	 'facebook.com/hackercup', 
	 'codeforces.com', 
	 'hackerearth.com', 
	 'geeksforgeeks.org', 
	 'leetcode.com', 
	 'codeforces.com/gyms'
	 }

cred = credentials.Certificate("c0d3r.json")
firebase_admin.initialize_app(cred, {
	'databaseURL': DB_URL
	})


url = "https://clist.by/api/v2/contest/?username="+CLIST_UNAME+"&api_key="+CLIST_KEY+"&format=json&resource="+",".join(key_set)+"&start__gte="+TS
r = requests.get(url)

cont_list = r.json()["objects"]
cont_dict={}
for cont in cont_list:
	if cont["resource_id"] not in cont_dict:
		cont_dict[cont["resource_id"]]=[]
	cont_dict[cont["resource_id"]].append(cont)
cont_json=json.dumps(cont_dict)
file_contents = json.loads(cont_json)
ref = db.reference("/")
ref.set(file_contents)