## Assignement
[x] Write a Dockerfile for any project (see [app directory](./app/) )
[x] Make it multistage compatible (see [app directory](./app/) )
[x] Make it multiplatform compatible with buildx
 - generally: `$ docker buildx build --platform linux/amd64 --platform linux/arm64 -t -t ashraftheminhaj/basic_api:v1 .`
 - else -
   ```
   docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder
   docker buildx inspect --bootstrap
   docker buildx build --platform linux/amd64 --platform linux/arm64 --push  -t ashraftheminhaj/basic_api:v1 .
   ```

   > ` docker buildx create --use --platform=linux/arm64,linux/amd64 --name multi-platform-builder` - This command creates a new builder instance. In this case, it supports both linux/arm64 and linux/amd64 platforms. The --name flag sets a name for the builder- "multi-platform-builder".

   > `docker buildx inspect --bootstrap` This command inspects the builder created in the previous step and performs any necessary setup or configuration. The --bootstrap flag indicates that the builder should be initialized if it hasn't been already

   > `docker buildx build --platform=linux/arm64,linux/amd64 --push --tag project-name:latest -f ./project-name/Dockerfile .` This command builds a Docker image using the builder created earlier.

[x] Push the image to the docker hub
 - used push in the previous step or usually - 
   ```
   docker push ashraftheminhaj/basic_api:v1
   ```
[x] Write commands to Run containers from image
 - `docker run -d -p 8080:8080 ashraftheminhaj/basic_api:v1 `
 - `docker run --env-file ./.env .`
[x] Open a shell inside the container
 - `docker run -it -p 8080:8080 ashraftheminhaj/basic_api:v1 bash`
[x] Submit the git repository with the project, Dockerfile, bash script if any, and documentation
