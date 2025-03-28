# JSCTZIAPI jsctzi Web App

This Ferris Web App is using Flask-AppBuilder as skeleton.

## How to run in Local Environment

[Here](/local_environment) you can find information about how to run locally

## How to add/update dependent libraries of the application
1. Update [Pipfile](Pipfile) **or**, if using the Model View Generator, add/edit the packages in the config file, under the *package_pipfile* key
2. On the **root** folder of the repository, run:
```console
pipenv update
```
```console
pipenv requirements > requirements.txt
```
This will ensure the requirements are updated for running in both local environment and in the cloud.

## App Configuration

A working configuration example can be found [here](local_environment/consul_key_value_pairs/ferris.apps.mag_demo_webapp1.json).

The app reads the configuration values from Consul. A tutorial on how to add the json values is [here](/local_environment/README.md).

Quick example (not exaustive, the app will not work with just these):
```json
{
  "APP_TITLE": "FERRIS APP",
  "DEFAULT_TOPIC": "ferris.events",
  "ADDON_MANAGERS": [
    "ferris_fab_consul.manager.FerrisConsulManager",
    "ferris_fab_minio.manager.FerrisMinioManager"],
  "DB_NAME": "ferris_all",
  "DB_HOST": "ferris-postgres",
  "DB_PORT": 5432,
  "DB_USERNAME": "admin",
  "DEFAULT_BROKER": "kafka://ferris-broker:29092",
  "AUTH_TYPE": 0,
  "AUTH_USER_REGISTRATION": true,
  "AUTH_USER_REGISTRATION_ROLE": "regular_user",
}
```

### Details on some of the available configuration options
|Key | Description |
|---|---|
|APP_TITLE| Title of the app that will be shown on UI|
|APP_THEME| UI theme that will be used by application|
|DEFAULT_TOPIC| Kafka topic that will be used for sending events|
|ADDON_MANAGERS| List of addon managers to be included in application (full list can be found bellow)|
|DB_NAME| Name of the database used by application|
|DB_HOST| Database host uri|
|DB_PORT| Database port|
|DB_USERNAME| Database user name|
|DEFAULT_BROKER| Address of default broker that will be used for sending events|
|AUTH_TYPE| Authentication type that will be used by application (`0` for DB auth, `1` for OIDC)|
|AUTH_USER_REGISTRATION| Whether or not to enable user registration|
|AUTH_USER_REGISTRATION_ROLE| Default role for newly registered users|
---


More details about the available configuration options can be found at the [Flask-AppBuilder official documentation](https://flask-appbuilder.readthedocs.io/en/latest/config.html)