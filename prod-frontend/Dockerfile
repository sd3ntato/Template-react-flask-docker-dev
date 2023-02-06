FROM nginx:alpine

# Copy config nginx
COPY .nginx/nginx.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

# Remove default nginx static assets
RUN rm -rf ./*

COPY ./build .

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]


# docker build -t nginx . && docker run -p 3000:3000  nginx