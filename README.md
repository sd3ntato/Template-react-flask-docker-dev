# Template-react-flask-docker-dev
 
This template allows to bootsrap a flask+react dockerized project.

The frontend is done with [Create-React-App](https://create-react-app.dev/) with the [minimal template](https://www.npmjs.com/package/cra-template-minimal)
The backend is a minimal implementation of a [flask](https://flask.palletsprojects.com/en/2.2.x/) app

The source code is sent to the containers with volumes, so real-time re-compiling is possible

you can run the template in development mode, or you can build the app and serve the production version (both of fe and be)
In case you run the production mode, the built up frontend is served with nginx

## runnning

to run the template in development mode:
```
docker-compose up --build
```

to run the template in production mode first build the app:
```
cd frontend && npm run build && cd ..
```
and then run it:
```
docker compose -f ./docker-compose-prod.yaml up --build
```

after some time (installing dependencies and starting the servers) you should be able to connect to http://localhost:3000/ with your brouser.
Happy Hacking!!
