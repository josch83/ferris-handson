# How to run the web app locally aka Development Mode

In order to run the web app locally, including the supporting services that Ferris usually provides, follow the steps.

**Note**: All bash commands should be run from from the **root** folder of the repository.

1. Create the `ferris-dev` docker network manually
```console
docker network create ferris-dev
```

2. Build the Docker image of the web app
```console
docker build -f Dockerfile -t magdemo:0.0.1 .
```

3. Run all the services (Web App, Postgres, Kafka/Zookeeper, Consul, etc.)
```console
docker compose -f local_environment/docker-compose.yml up -d
```

4. Add the needed key-value pairs to Consul. The default examples are in the folder local_environment/consul_key_value_pairs. The *key* **must** be the filename (**without .json suffix**, so for example `ferris.env`), and the *value* should be the file content.
5. Run the commands:
    1. ```console
        docker exec -it web-app bash
        ```
    2. ```console
        export FLASK_APP=app
        ```
    3. ```console
        flask fab create-admin
        ```
6. The Web App UI should be available at [http://localhost:9999](http://localhost:9999). Login with the user credentials created in the previous step.


**Note**: The steps 1, 4 and 5 are part of the initialization and should only be run the first time. Or when doing a clean install.


## How to check the logs from any container
```console
docker logs -f container_name
```
`container_name` can be checked in the [docker-compose file](docker-compose.yml)