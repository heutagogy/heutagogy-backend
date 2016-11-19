let pkgs = import <nixpkgs> { };
in pkgs.python3Packages.buildPythonApplication {
  name = "heutagogy";

  propagatedBuildInputs = [
    pkgs.python3Packages.flask
  ];
}
