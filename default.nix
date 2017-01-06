let
  pkgs = (import <nixpkgs> { }).overridePackages (pkgs: self: {
    # Upstream PR: https://github.com/NixOS/nixpkgs/pull/20590
    python3Packages = self.python3Packages // {
      flask = pkgs.python3Packages.buildPythonPackage {
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

      flask_restful = pkgs.python3Packages.buildPythonPackage {
        name = "flask-restful-0.3.5";

        src = pkgs.fetchurl {
          url = "mirror://pypi/F/Flask-RESTful/Flask-RESTful-0.3.5.tar.gz";
          sha256 = "0hjcmdb56b7z4bkw848lxfkyrpnkwzmqn2dgnlv12mwvjpzsxr6c";
        };

        propagatedBuildInputs = with pkgs.python3Packages; [ flask pytz six aniso8601 ];

        doCheck = false;
      };

      flask_jwt = pkgs.python3Packages.buildPythonPackage {
        name = "flask-jwt-0.3.2";

        src = pkgs.fetchurl {
          url = "mirror://pypi/F/Flask-JWT/Flask-JWT-0.3.2.tar.gz";
          sha256 = "49c0672fbde0f1cd3374bd834918d28956e3c521c7e00089cdc5380d323bd0ad";
        };

        propagatedBuildInputs = with pkgs.python3Packages; [ flask pyjwt ];

        doCheck = false;
      };

      aniso8601 = pkgs.python3Packages.buildPythonPackage {
        name = "aniso8601-1.2.0";

        src = pkgs.fetchurl {
          url = "mirror://pypi/a/aniso8601/aniso8601-1.2.0.tar.gz";
          sha256 = "1m2d83rm684xdf54ynfd9lv3slv7bkqq6pcirh2aibvl4pw0092h";
        };

        propagatedBuildInputs = with pkgs.python3Packages; [ dateutil ];
      };
    };
  });

in pkgs.python3Packages.buildPythonApplication {
  name = "heutagogy";

  propagatedBuildInputs = [
    pkgs.python3Packages.flask
    pkgs.python3Packages.flask_restful
    pkgs.python3Packages.flask_jwt
    pkgs.python3Packages.flask_sqlalchemy
  ];
}
