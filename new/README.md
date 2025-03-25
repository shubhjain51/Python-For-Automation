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
1. Pod is stuck in CrashLoopBackOff state. How do you debug and fix it?    
2. Pod is stuck in ContainerCreating state. How do you investigate?    
3. Pod is failing with OOMKilled. What does this mean, and how do you resolve it?    
4. A container inside a pod is taking too long to start. How do you debug startup issues?    
5. You have configured liveness and readiness probes, but your pod is continuously restarting. What could be the issue?    
6. How would you debug a container that exits immediately after starting?     
7. Your pod is failing due to missing environment variables. How do you debug it?    
8. You deployed an application, but logs are not visible using kubectl logs. What could be the reason?          

## 2. Service & Networking Issues
1. A Service is created, but it’s not routing traffic to the pods. How do you debug it?     
2. A pod is unable to reach another pod on a different node. How do you troubleshoot networking issues?    
3. Your Kubernetes NodePort service is not accessible externally. What do you check?     
4. You have a LoadBalancer service, but it’s not getting an external IP. How do you debug it?      
5. Ingress is not working as expected. How do you debug it?     
6. A pod cannot resolve an external domain (e.g., google.com). What could be the problem?     
7. Network policies are blocking traffic between services. How do you identify and fix this?    

## 3. Node & Cluster Issues
1. One of the nodes is in NotReady state. How do you investigate?      
2. Pods are not being scheduled on a particular node. What could be the reasons?   
3. You have a node that is running low on CPU and memory. How do you optimize resource allocation?     
4. How do you drain a node safely before maintenance?    
5. How do you recover a Kubernetes node that is down?     
6. Kubelet is not running on a node. How do you debug and fix this?    
7. You see DiskPressure or MemoryPressure taints on a node. What should you do?     

## 4. Persistent Storage Issues
1. A Persistent Volume Claim (PVC) is stuck in Pending state. How do you resolve it?     
2. A pod is unable to mount a Persistent Volume. What could be the issue?    
3. You deleted a pod, but its volume data is missing when a new pod is created. Why?   
4. A StatefulSet pod is failing to mount the expected storage. How do you debug this?    

## 5. Deployment & Scaling Issues
1. A Deployment is stuck in Pending state. How do you debug it?    
2. You scaled your Deployment, but new pods are not being created. What do you check?    
3. A rolling update is failing and causing downtime. How do you troubleshoot?    
4. You want to roll back a failed deployment. How do you do it?    
5. A pod takes a long time to terminate. What could be causing this delay?     
6. How do you ensure zero downtime while deploying a new version of an application?    
7. Your Kubernetes cluster is experiencing high latency. How do you optimize it?     
8. Your Horizontal Pod Autoscaler (HPA) is not scaling up pods. What could be the issue?    
9. Your pods are scaling up but not down when load decreases. What do you check?    

## 6. Security & Access Control Issues
1. A user is unable to create a resource in a namespace. How do you check their permissions?   
2. How do you prevent a pod from running as root?   
3. A pod is unable to access a Kubernetes secret. What could be the issue?   
4. A pod is running with more privileges than expected. How do you fix this?   
5. How do you restrict access to certain namespaces for a specific user?   
6. How do you ensure secure communication between services in Kubernetes?   
7. A ServiceAccount is missing necessary permissions. How do you debug RBAC issues?   

## 7. Logging, Monitoring, & Debugging
1. How do you debug a pod that does not generate logs?   
2. How do you check real-time logs of a failing pod?    
3. Your cluster is experiencing CPU and memory spikes. How do you monitor resource usage?    
4. How do you set up centralized logging for a Kubernetes cluster?   
5. How do you enable and use Kubernetes audit logs?    
6. A pod is experiencing intermittent failures. How do you collect metrics to debug it?    
7. How do you use Prometheus and Grafana to monitor Kubernetes metrics?    

## 8. ConfigMaps & Secrets Issues
1. A pod is failing because it cannot read a ConfigMap. How do you fix it?    
2. How do you update a ConfigMap without restarting the pods?    
3. A pod is unable to read a Secret. How do you debug and resolve it?    
4. You need to update a Secret without restarting your application. How do you achieve this?    

## 9. StatefulSet, DaemonSet & Job Issues
1. A StatefulSet pod is not coming up after a restart. How do you debug it?     
2. A DaemonSet is not running on all nodes. What could be the reason?   
3. How do you restart a specific pod in a StatefulSet?    
4. A Kubernetes Job is not completing. How do you debug it?     
5. A CronJob is not triggering as expected. How do you troubleshoot it?     

## 10. Kubernetes API & Controller Issues
1. The Kubernetes API server is down. How do you recover it?     
2. A custom controller is not reconciling resources as expected. How do you debug it?      
3. How do you debug an issue where kubectl apply takes too long?     
4. A Kubernetes Operator is not managing CRDs correctly. How do you troubleshoot it?     




# 📌 Linux Commands Cheat Sheet

## 🔹 1. Basic Linux Commands
| Command | Description |
|---------|------------|
| `pwd` | Print the current working directory. |
| `ls` | List files and directories in the current directory. |
| `cd <dir>` | Change the directory to `<dir>`. |
| `mkdir <dir>` | Create a new directory. |
| `rmdir <dir>` | Remove an empty directory. |
| `rm <file>` | Remove a file. |
| `rm -r <dir>` | Remove a directory and its contents recursively. |
| `cp <source> <destination>` | Copy a file or directory. |
| `mv <source> <destination>` | Move or rename a file or directory. |
| `touch <file>` | Create a new empty file. |
| `cat <file>` | Display the contents of a file. |
| `more <file>` | View file contents page by page. |
| `less <file>` | View file contents (allows scrolling). |
| `echo "text"` | Print text to the terminal. |
| `clear` | Clear the terminal screen. |

## 🔹 2. File Permissions & Ownership
| Command | Description |
|---------|------------|
| `ls -l` | List files with detailed permissions. |
| `chmod 755 <file>` | Change file permissions. |
| `chown user:group <file>` | Change file ownership. |
| `chgrp <group> <file>` | Change the group ownership of a file. |
| `umask` | Show default file permissions. |

## 🔹 3. Process Management
| Command | Description |
|---------|------------|
| `ps aux` | Show running processes. |
| `top` | Show system resource usage. |
| `htop` | Interactive process viewer (if installed). |
| `kill <PID>` | Kill a process by its Process ID. |
| `kill -9 <PID>` | Forcefully terminate a process. |
| `pkill <process-name>` | Kill a process by its name. |
| `jobs` | Show background jobs. |
| `bg <jobID>` | Resume a background job. |
| `fg <jobID>` | Bring a background job to the foreground. |
| `nohup <command> &` | Run a command in the background, ignoring hangups. |

## 🔹 4. Disk Usage & Storage Management
| Command | Description |
|---------|------------|
| `df -h` | Show disk usage in a human-readable format. |
| `du -sh <dir>` | Show the size of a directory. |
| `lsblk` | List information about block devices. |
| `mount /dev/sdX /mnt` | Mount a partition. |
| `umount /mnt` | Unmount a partition. |
| `fdisk -l` | List disk partitions. |
| `mkfs.ext4 /dev/sdX` | Format a partition with ext4 filesystem. |

## 🔹 5. User Management
| Command | Description |
|---------|------------|
| `whoami` | Show the current logged-in user. |
| `who` | Show logged-in users. |
| `id` | Show user and group IDs. |
| `adduser <username>` | Add a new user. |
| `userdel -r <username>` | Delete a user and their home directory. |
| `passwd <username>` | Change the user password. |
| `usermod -aG <group> <user>` | Add a user to a group. |
| `groups <user>` | Show groups a user belongs to. |

## 🔹 6. Networking Commands
| Command | Description |
|---------|------------|
| `ip a` | Show IP addresses. |
| `ifconfig` | Show network interfaces (older command). |
| `ping <hostname>` | Send ICMP packets to test network connectivity. |
| `netstat -tulnp` | Show listening ports and services. |
| `ss -tulnp` | Show active network connections (modern replacement for netstat). |
| `nslookup <domain>` | Query DNS records. |
| `dig <domain>` | Get detailed DNS information. |
| `traceroute <domain>` | Show the route packets take to a host. |
| `wget <URL>` | Download a file from a URL. |
| `curl -O <URL>` | Download a file from a URL. |

## 🔹 7. Package Management
### 🟢 Debian-based (Ubuntu, Debian)
| Command | Description |
|---------|------------|
| `apt update` | Update package lists. |
| `apt upgrade` | Upgrade installed packages. |
| `apt install <package>` | Install a package. |
| `apt remove <package>` | Remove a package. |

### 🔵 RHEL-based (CentOS, Fedora, RHEL)
| Command | Description |
|---------|------------|
| `yum update` | Update packages (RHEL 7). |
| `dnf update` | Update packages (RHEL 8+). |
| `yum install <package>` | Install a package. |
| `yum remove <package>` | Remove a package. |

### 🟠 Arch Linux
| Command | Description |
|---------|------------|
| `pacman -Syu` | Update system. |
| `pacman -S <package>` | Install a package. |

## 🔹 8. Logs & System Monitoring
| Command | Description |
|---------|------------|
| `journalctl -xe` | View system logs. |
| `dmesg` | Show kernel logs. |
| `uptime` | Show system uptime. |
| `free -m` | Show memory usage. |
| `vmstat` | Show system performance. |
| `iostat` | Show CPU and disk statistics. |
| `mpstat` | Show CPU usage. |

## 🔹 9. Compression & Archiving
| Command | Description |
|---------|------------|
| `tar -cvf archive.tar <dir>` | Create a `.tar` archive. |
| `tar -xvf archive.tar` | Extract a `.tar` archive. |
| `tar -czvf archive.tar.gz <dir>` | Create a compressed `.tar.gz` archive. |
| `tar -xzvf archive.tar.gz` | Extract a `.tar.gz` archive. |
| `zip -r archive.zip <dir>` | Create a `.zip` archive. |
| `unzip archive.zip` | Extract a `.zip` archive. |

## 🔹 10. Text Processing
| Command | Description |
|---------|------------|
| `grep "pattern" <file>` | Search for a pattern in a file. |
| `awk '{print $1}' <file>` | Process text in columns. |
| `sed 's/old/new/g' <file>` | Replace text in a file. |
| `cut -d':' -f1 /etc/passwd` | Extract specific fields from a file. |
| `sort <file>` | Sort lines in a file. |
| `uniq <file>` | Remove duplicate lines. |
| `wc -l <file>` | Count lines in a file. |

## 🔹 11. SSH & Remote Access
| Command | Description |
|---------|------------|
| `ssh user@host` | Connect to a remote system via SSH. |
| `scp file user@host:/path` | Securely copy files between systems. |
| `rsync -av source/ destination/` | Sync files efficiently. |

## 🔹 12. System Shutdown & Reboot
| Command | Description |
|---------|------------|
| `shutdown -h now` | Shutdown immediately. |
| `shutdown -r now` | Reboot the system. |
| `reboot` | Restart the system. |
