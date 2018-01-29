{ pkgs ? import <nixpkgs> { } }:
let
  python = import ./requirements.nix { inherit pkgs; };
in python.mkDerivation {
  name = "heutagogy-1.0";

  buildInputs = [
    pkgs.python3Packages.flake8
    python.packages.psycopg2
    python.packages.gunicorn
  ];

  propagatedBuildInputs = [
    python.packages.google-auth
    python.packages.Flask
    python.packages.Flask-JWT
    python.packages.Flask-Login
    python.packages.Flask-Migrate
    python.packages.Flask-RESTful
    python.packages.Flask-SQLAlchemy
    python.packages.Flask-User
    python.packages.LinkHeader
    python.packages.newspaper3k
    python.packages.rq
  ];

  checkPhase = ''
    ./tests.py

    flake8 . --exclude=migrations
  '';

  # This sets FLASK_APP environment variable, so you don't have to.
  FLASK_APP = "heutagogy";
}
