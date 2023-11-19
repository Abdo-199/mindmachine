# Stage 1: Build the React app
FROM node:latest as build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the source code to the container
COPY . .

# Build the React app for production
RUN npm run build

# Stage 2: Create the final production image
FROM nginx:latest

# Copy the production-ready React app from the build stage to the nginx document root
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port that nginx will listen on (usually 80)
EXPOSE 80

# Define the command to start nginx (it will start automatically)
CMD ["nginx", "-g", "daemon off;"]
