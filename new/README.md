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






# 📌 Dockerfile Commands & Their Explanation

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




# Kubernetes Scenario Based Questions

 ## 1. Pod & Container Issues
Pod is stuck in CrashLoopBackOff state. How do you debug and fix it?
Pod is stuck in ContainerCreating state. How do you investigate?
Pod is failing with OOMKilled. What does this mean, and how do you resolve it?
A container inside a pod is taking too long to start. How do you debug startup issues?
You have configured liveness and readiness probes, but your pod is continuously restarting. What could be the issue?
How would you debug a container that exits immediately after starting?
Your pod is failing due to missing environment variables. How do you debug it?
You deployed an application, but logs are not visible using kubectl logs. What could be the reason?

## 2. Service & Networking Issues
A Service is created, but it’s not routing traffic to the pods. How do you debug it?
A pod is unable to reach another pod on a different node. How do you troubleshoot networking issues?
Your Kubernetes NodePort service is not accessible externally. What do you check?
You have a LoadBalancer service, but it’s not getting an external IP. How do you debug it?
Ingress is not working as expected. How do you debug it?
A pod cannot resolve an external domain (e.g., google.com). What could be the problem?
Network policies are blocking traffic between services. How do you identify and fix this?

## 3. Node & Cluster Issues
One of the nodes is in NotReady state. How do you investigate?
Pods are not being scheduled on a particular node. What could be the reasons?
You have a node that is running low on CPU and memory. How do you optimize resource allocation?
How do you drain a node safely before maintenance?
How do you recover a Kubernetes node that is down?
Kubelet is not running on a node. How do you debug and fix this?
You see DiskPressure or MemoryPressure taints on a node. What should you do?

## 4. Persistent Storage Issues
A Persistent Volume Claim (PVC) is stuck in Pending state. How do you resolve it?
A pod is unable to mount a Persistent Volume. What could be the issue?
You deleted a pod, but its volume data is missing when a new pod is created. Why?
A StatefulSet pod is failing to mount the expected storage. How do you debug this?

## 5. Deployment & Scaling Issues
A Deployment is stuck in Pending state. How do you debug it?
You scaled your Deployment, but new pods are not being created. What do you check?
A rolling update is failing and causing downtime. How do you troubleshoot?
You want to roll back a failed deployment. How do you do it?
A pod takes a long time to terminate. What could be causing this delay?
How do you ensure zero downtime while deploying a new version of an application?
Your Kubernetes cluster is experiencing high latency. How do you optimize it?
Your Horizontal Pod Autoscaler (HPA) is not scaling up pods. What could be the issue?
Your pods are scaling up but not down when load decreases. What do you check?

## 6. Security & Access Control Issues
A user is unable to create a resource in a namespace. How do you check their permissions?
How do you prevent a pod from running as root?
A pod is unable to access a Kubernetes secret. What could be the issue?
A pod is running with more privileges than expected. How do you fix this?
How do you restrict access to certain namespaces for a specific user?
How do you ensure secure communication between services in Kubernetes?
A ServiceAccount is missing necessary permissions. How do you debug RBAC issues?

## 7. Logging, Monitoring, & Debugging
How do you debug a pod that does not generate logs?
How do you check real-time logs of a failing pod?
Your cluster is experiencing CPU and memory spikes. How do you monitor resource usage?
How do you set up centralized logging for a Kubernetes cluster?
How do you enable and use Kubernetes audit logs?
A pod is experiencing intermittent failures. How do you collect metrics to debug it?
How do you use Prometheus and Grafana to monitor Kubernetes metrics?

## 8. ConfigMaps & Secrets Issues
A pod is failing because it cannot read a ConfigMap. How do you fix it?
How do you update a ConfigMap without restarting the pods?
A pod is unable to read a Secret. How do you debug and resolve it?
You need to update a Secret without restarting your application. How do you achieve this?

## 9. StatefulSet, DaemonSet & Job Issues
A StatefulSet pod is not coming up after a restart. How do you debug it?
A DaemonSet is not running on all nodes. What could be the reason?
How do you restart a specific pod in a StatefulSet?
A Kubernetes Job is not completing. How do you debug it?
A CronJob is not triggering as expected. How do you troubleshoot it?

## 10. Kubernetes API & Controller Issues
The Kubernetes API server is down. How do you recover it?
A custom controller is not reconciling resources as expected. How do you debug it?
How do you debug an issue where kubectl apply takes too long?
A Kubernetes Operator is not managing CRDs correctly. How do you troubleshoot it?