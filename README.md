# Heutagogy backend

## Install requirements
### Using pip
```sh
pip3 install -r requirements.txt
```

### Using Nix
```sh
nix-shell
```

## Debug run
```sh
./run.py
```

## Create a database
```sh
env FLASK_APP=heutagogy/heutagogy.py flask initdb
```
