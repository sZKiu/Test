# Dockerfile

# Use the Nginx image from Docker Hub
FROM nginx:1.19-alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the configuration file from the current directory to the Nginx directory
COPY nginx.conf /etc/nginx/conf.d
