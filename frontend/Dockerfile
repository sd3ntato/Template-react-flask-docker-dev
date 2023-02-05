FROM node:16-alpine

WORKDIR /frontend

# this is done before so I don't need to re-install
# dependencies every time I change the code
COPY package.json ./
RUN npm i

# COPY ./src ./src # this is done in docker-compose
COPY ./public ./public


EXPOSE 3000

CMD ["npm", "start"]