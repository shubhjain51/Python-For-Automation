# 🚀 Docker Commands Cheat Sheet (With Explanations)

## 📌 1. Basic Docker Commands

| Command            | Description                              |
|--------------------|------------------------------------------|
| `docker version`   | Shows installed Docker version.         |
| `docker info`      | Displays system-wide Docker info.       |
| `docker help`      | Shows general help for Docker commands. |

---

## 📌 2. Working with Containers

| Command                                    | Description                                        |
|--------------------------------------------|----------------------------------------------------|
| `docker run <image>`                        | Runs a container from an image.                   |
| `docker run -d <image>`                     | Runs a container in the background (detached).    |
| `docker run -it <image> bash`               | Runs a container interactively with a shell.      |
| `docker run --rm <image>`                   | Runs and removes the container after it exits.    |
| `docker ps`                                 | Lists running containers.                         |
| `docker ps -a`                              | Lists all containers (including stopped ones).    |
| `docker stop <container>`                   | Stops a running container.                        |
| `docker kill <container>`                   | Forces a container to stop immediately.           |
| `docker restart <container>`                | Restarts a stopped/running container.            |
| `docker rm <container>`                     | Removes a stopped container.                     |
| `docker rm -f <container>`                  | Force removes a running container.               |
| `docker logs <container>`                   | Shows logs of a running container.               |
| `docker exec -it <container> bash`          | Enters a running container with an interactive shell. |
| `docker inspect <container>`                | Shows detailed information about a container.    |

---

## 📌 3. Working with Images

| Command                        | Description                          |
|--------------------------------|--------------------------------------|
| `docker images`                | Lists all available images.          |
| `docker pull <image>`          | Downloads an image from Docker Hub.  |
| `docker rmi <image>`           | Removes an image.                    |
| `docker tag <source_image> <new_image>` | Tags an image with a new name. |
| `docker save -o <file>.tar <image>` | Saves an image as a tar file.  |
| `docker load -i <file>.tar`    | Loads an image from a tar file.      |

---

## 📌 4. Building Docker Images

| Command                                        | Description                                        |
|------------------------------------------------|----------------------------------------------------|
| `docker build -t <image_name> .`              | Builds an image from a Dockerfile in the current directory. |
| `docker build -f <Dockerfile> -t <image_name> .` | Builds an image using a specific Dockerfile. |

---

## 📌 5. Managing Volumes (Persistent Storage)

| Command                                    | Description                              |
|--------------------------------------------|------------------------------------------|
| `docker volume create <volume_name>`      | Creates a volume.                        |
| `docker volume ls`                         | Lists all volumes.                       |
| `docker volume inspect <volume_name>`      | Shows details of a volume.               |
| `docker volume rm <volume_name>`          | Deletes a volume.                        |
| `docker run -v <volume_name>:/data <image>` | Mounts a volume to a container.         |

---

## 📌 6. Networking in Docker

| Command                                   | Description                          |
|-------------------------------------------|--------------------------------------|
| `docker network ls`                       | Lists available networks.           |
| `docker network create <network_name>`    | Creates a new network.              |
| `docker network inspect <network_name>`   | Shows details of a network.         |
| `docker network connect <network> <container>` | Connects a container to a network. |
| `docker network disconnect <network> <container>` | Disconnects a container from a network. |

---

## 📌 7. Docker Compose (Multi-Container Management)

| Command                        | Description                                           |
|--------------------------------|-------------------------------------------------------|
| `docker-compose up`            | Starts all containers defined in `docker-compose.yml`. |
| `docker-compose up -d`         | Starts containers in the background (detached mode). |
| `docker-compose down`          | Stops and removes all containers defined in the file. |
| `docker-compose ps`            | Lists running containers managed by Docker Compose.  |

---

## 📌 8. Docker Logs & Debugging

| Command                        | Description                                     |
|--------------------------------|-----------------------------------------------|
| `docker logs <container>`      | Displays logs of a running container.         |
| `docker stats`                 | Shows real-time CPU and memory usage.        |
| `docker top <container>`       | Shows running processes inside a container.  |
| `docker events`                | Streams real-time Docker events.             |

---

## 📌 9. Cleaning Up Unused Resources

| Command                        | Description                                    |
|--------------------------------|----------------------------------------------|
| `docker system prune`          | Removes all unused containers, networks, and images. |
| `docker system prune -a`       | Removes everything including stopped containers and unused images. |
| `docker container prune`       | Removes all stopped containers.              |
| `docker image prune`           | Removes all dangling images.                 |
| `docker volume prune`          | Removes all unused volumes.                  |

---

## 📌 10. Security & User Management

| Command                                  | Description                                     |
|------------------------------------------|-----------------------------------------------|
| `sudo usermod -aG docker $USER`         | Adds a user to the Docker group (avoids using sudo). |
| `docker scan <image>`                    | Scans an image for vulnerabilities.          |

---

## 🎯 **Conclusion**
This cheat sheet provides a **quick reference** for essential Docker commands, covering everything from **container management** to **networking, security, and debugging**. Bookmark this page for **fast access** during your Docker workflows! 🚀





📌 Dockerfile Commands & Their Explanation

|Command|	Explanation|	Example|
| 	:-----:	 | 	:-----:	 | 	:-----:	 | 
|FROM| Sets the base image for the container.|	FROM python:3.9|
|LABEL|	Adds metadata (author, version, description).	|LABEL maintainer="admin@example.com"|
|WORKDIR|	Sets the working directory inside the container.	|WORKDIR /usr/src/app|
|COPY|	Copies files from the host machine to the container.	|COPY . /app|
|ADD|	Similar to COPY, but can also download from URLs and extract archives.	|ADD app.tar.gz /app|
|RUN|	Executes a command while building the image.	|RUN apt update && apt install -y curl|
|ENV|	Sets environment variables inside the container.	|ENV PORT=8080|
|EXPOSE|	Informs Docker that the container listens on a specific port.	|EXPOSE 80|
|CMD|	Defines the default command that runs when the container starts.	|CMD ["python", "app.py"]|
|ENTRYPOINT|	Similar to CMD, but cannot be overridden at runtime.	|ENTRYPOINT ["nginx", "-g", "daemon off;"]|
|VOLUME|	Creates a mount point for persistent storage.	|VOLUME /data|
|ARG|	Defines a build-time variable (used during docker build).	|ARG APP_VERSION=1.0|
|USER|	Specifies which user should run the container.	|USER appuser|
|HEALTHCHECK|	Defines a health check for the container.	|`HEALTHCHECK CMD curl -f http://localhost|
|ONBUILD|	Defines a command to run only when used as a base image.	|ONBUILD COPY . /app|
|SHELL	|Changes the default shell inside the container.	|SHELL ["/bin/bash", "-c"]|
|STOPSIGNAL|	Defines the system signal to stop the container.	|STOPSIGNAL SIGTERM|