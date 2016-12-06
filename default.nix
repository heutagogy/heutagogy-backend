let
  pkgs = (import <nixpkgs> { }).overridePackages (pkgs: self: {
    # Upstream PR: https://github.com/NixOS/nixpkgs/pull/20590
    python3Packages = self.python3Packages // {
      flask = self.python3Packages.buildPythonPackage {
        name = "flask-0.11.1";

        src = pkgs.fetchurl {
          url = "mirror://pypi/F/Flask/Flask-0.11.1.tar.gz";
          sha256 = "03kbfll4sj3v5z7r31c7bhfpi11r1np076d4p1k2kg4yzcmkywdl";
        };

        propagatedBuildInputs = with pkgs.python3Packages; [ itsdangerous click werkzeug jinja2 ];

        meta = with pkgs.lib; {
          homepage = http://flask.pocoo.org/;
          description = "A microframework based on Werkzeug, Jinja 2, and good intentions";
          license = licenses.bsd3;
        };
      };
    };
  });

in pkgs.python3Packages.buildPythonApplication {
  name = "heutagogy";

  propagatedBuildInputs = [
    pkgs.python3Packages.flask
    pkgs.python3Packages.flask_login
  ];
}
