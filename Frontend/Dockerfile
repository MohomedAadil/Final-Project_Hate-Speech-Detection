FROM nginx:alpine

COPY default.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html/

# COPY . ./
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]