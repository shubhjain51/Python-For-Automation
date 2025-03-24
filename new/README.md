📌 Dockerfile Commands & Their Explanation

Command	Explanation	Example
FROM	Sets the base image for the container.	FROM python:3.9
LABEL	Adds metadata (author, version, description).	LABEL maintainer="admin@example.com"
WORKDIR	Sets the working directory inside the container.	WORKDIR /usr/src/app
COPY	Copies files from the host machine to the container.	COPY . /app
ADD	Similar to COPY, but can also download from URLs and extract archives.	ADD app.tar.gz /app
RUN	Executes a command while building the image.	RUN apt update && apt install -y curl
ENV	Sets environment variables inside the container.	ENV PORT=8080
EXPOSE	Informs Docker that the container listens on a specific port.	EXPOSE 80
CMD	Defines the default command that runs when the container starts.	CMD ["python", "app.py"]
ENTRYPOINT	Similar to CMD, but cannot be overridden at runtime.	ENTRYPOINT ["nginx", "-g", "daemon off;"]
VOLUME	Creates a mount point for persistent storage.	VOLUME /data
ARG	Defines a build-time variable (used during docker build).	ARG APP_VERSION=1.0
USER	Specifies which user should run the container.	USER appuser
HEALTHCHECK	Defines a health check for the container.	`HEALTHCHECK CMD curl -f http://localhost
ONBUILD	Defines a command to run only when used as a base image.	ONBUILD COPY . /app
SHELL	Changes the default shell inside the container.	SHELL ["/bin/bash", "-c"]
STOPSIGNAL	Defines the system signal to stop the container.	STOPSIGNAL SIGTERM