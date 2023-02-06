# Template-react-flask-docker-dev
 
This template allows to bootsrap a flask+react dockerized project.

The frontend is done with [Create-React-App](https://create-react-app.dev/) with the [minimal template](https://www.npmjs.com/package/cra-template-minimal)
The backend is a minimal implementation of a [flask](https://flask.palletsprojects.com/en/2.2.x/) app

The source code is sent to the containers with volumes, so real-time re-compiling is possible

## runnning
```
docker-compose up --build
```

after some time (installing dependencies and starting the servers, you should be able to connect to http://localhost:3000/ with your brouser.
Happy Hacking!!
