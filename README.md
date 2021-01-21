# Three Web Servers demonstrating Pyramid in Docker

## helloworld

This server just returns a text response

## htmlpage

This server returns an HTML response (with associated CSS)

## htmltemplatepage

This server returns an HTML response that is templatized (more power!!!)

## Rest with JS

This server combines the principles of REST to make resource requests to the server!

## Usage

1. Install Docker Desktop (<https://docs.docker.com/engine/install/>)
2. Install Docker Compose (<https://docs.docker.com/compose/install/>)
3. Inside each folder, build the image and run the container:

   ```bash
    docker-compose up --build
   ```

4. The specific server should be running on: <http://0.0.0.0:6543/>
