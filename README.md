# devops-new
1. Created a simple web app using flash 
2. Created a Docker image using below docker commands.
	docker build --tag flask-docker-info-app .
        docker run --name flask-docker-info-app -p 5001:5001 flask-docker-info-app
3.check the  container is started or not using docker ps -a.
4. access application using https://ipoftheserver:5001/info
