# Heutagogy backend [![Build Status](https://travis-ci.org/heutagogy/heutagogy-backend.svg?branch=master)](https://travis-ci.org/heutagogy/heutagogy-backend)

The Heutagogy backend is a core of the [Heutagogy project](https://github.com/heutagogy).

## Requirements
- python3
- postgresql
- redis

## Preparing
### Using pip
Install all necessary build requirements.
```sh
pip3 install -r requirements.txt
```

Configure environment variables.
```sh
export FLASK_APP=heutagogy
```

This tells Flask which application to use.


### Using [Nix](https://nixos.org/nix/)
Use the following command to install all necessary dependencies and set environment variables.
```sh
nix-shell
```

## Database setup
Heutagogy requires Postgresql (for storing user data) and Redis (for work queue) databases to function properly.

The postgresql database configuration is passed via `DATABASE_URL` environment variable, which defaults to `postgresql:///heutagogy` (that is, postgersql database on localhost, database name `heutagogy`).

Redis database configuration is passed via `REDIS_URL` environment variable and defaults to `redis://localhost:6379`.

## Create database tables
Before starting the server, you need to create/upgrade the database/schema. This should be done with the following command.
```sh
flask db upgrade
```

## Debug run
```sh
./run.py
```

## Run
```sh
flask run
```

## Registration
Navigate to <http://127.0.0.1:5000/user/register> to register your user.

## What's next
After you have your server running, use [the frontend](https://github.com/heutagogy/heutagogy-frontend) or [the google chrome extension](https://github.com/heutagogy/heutagogy-chrome-extension) to communicate with the server.

## Reporting an issue
### Our process
We follow the [C4.2 process](https://rfc.zeromq.org/spec:42) for working with Heutagogy, which means that every change is tracked as an issue. You can either:

- Define an issue for a problem and then propose your own patch, or wait for someone else to fix it, or
- Come immediately with a patch, and submit that as a pull request, without a separate issue.

An ideal description for an issue goes:
```
Problem: (describe the problem here)
Solution: (describe your solution here)
```

## License
The heutagogy-backend source code is licensed by GNU Affero General Public License version 3 (APGLv3).

The full text of the Heutagogy license is available in [LICENSE](./LICENSE) file.
