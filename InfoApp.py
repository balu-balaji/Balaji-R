from flask import Flask, redirect, url_for
app = Flask(__name__)


jsonString = ''' 
{
  "service_name": "myapplication",
  "version": "1.0.0",
  "git_commit_sha" :"abc5789789",
  "environment" : {
    "service_port":"8080",
    "log_level":"INFO"
  }
}'''

@app.route('/info')
def processInfo():
   return jsonString

if __name__ == '__main__':
   app.run(host ='0.0.0.0', port = 5001, debug = True)
