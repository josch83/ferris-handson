# Warning: The readme is not up to date!


# Ferris web module for MAGDEMOAPI API

## 1. Add new version of the magdemo-api-client package if available
If you generated a new version of the server from  then you probably generated a new version of the client too.

In this case there is a new package for ```magdemo-api-client``` that should be added to this repo as done for ```magdemo-api-client-0.0.2.tar.gz```.

Different packages versions for ```magdemo-api-client``` can coexists in this repo. It is your job to select the one needed/used.
## 2. Select a specific version of magdemo-api-client if needed

If you have multiple versions of the package ```magdemo-api-client``` present in this repo, you can select a specific one by changing the 
file ```setup.py``` by selecting/requiring a specific version.

In this case, if by accident  installs a version that is not required by this module, the error that this module requires another version will be reported and you should then add the right package version for ```magdemo-api-client``` in /tree/main/ferrisapp/provisioning/dist and accordingly change the version of the installed package in /blob/main/ferrisapp/provisioning/dev.Dockerfile
## 3. Develop

The main things to do when adding for example other endpoints, view, etc.:

- go to the directory ```fab_addon_magdemo_api/services``` and add the services you want/need
- go to the directory ```fab_addon_magdemo_api/models``` and add the generic model, generic interface and generic session accordingly for the entities
- go to the directory ```fab_addon_magdemo_api/views``` and add the views you want/need
- go to the file ```fab_addon_magdemo_api/manager.py``` and register the views you want/need

## 4. Bump module version

If you have made any changes, please remember to bump the version of this module by heading to the file

```fab_addon_magdemo_api/version.py``` and changing to an appropriate version. As you can see the version string will be built
out of the three number provided in the variables:

```python
VERSION_MAJOR
VERSION_MINOR
VERSION_BUILD
```

## 4. Build the package to include in the webapp repo 

From the root of the repo (i.e. where the setup.py lives) execute

```bash
python setup.py sdist
```

to build the package.

Now a new package has been created in the ```dist``` directory.

You can copy this generated package into /tree/main/ferrisapp/provisioning/dist .

If you also generated a new ```magdemo-api-client``` package, please remember to copy this also into /tree/main/ferrisapp/provisioning/dist


## Note
Having permission to access a resource and perform an operation, doesn't mean that the user should manipulate all data returned by that endpoint.

Finer grained access control that takes into account which users created the records (and eventually related records) have to be managed by the service itself (it means that the logic needs to be coded) and not by the AUTH server/service (KC in this case).
The protected endpoints have access to the user id (sub/uid from the AUTH server/service) and the scopes (permission on a resource). 
The scopes control should be authomatic (permission on a resource) but getting the proper data based on the user is not.
