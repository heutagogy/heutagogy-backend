{ pkgs ? import <nixpkgs> { } }:
let
  python = import ./requirements.nix { inherit pkgs; };
in python.mkDerivation {
  name = "heutagogy-1.0";

  buildInputs = [
    pkgs.python3Packages.flake8
  ];

  propagatedBuildInputs = [
    python.packages.Flask
    python.packages.Flask-RESTful
    python.packages.Flask-JWT
    python.packages.Flask-SQLAlchemy
    python.packages.bcrypt
  ];

  checkPhase = ''
    ./tests.py

    flake8 .
  '';
}
