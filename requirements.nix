# generated using pypi2nix tool (version: 1.8.1)
# See more at: https://github.com/garbas/pypi2nix
#
# COMMAND:
#   pypi2nix -V 3.6 -r requirements.txt -E libffi -E postgresql -E libxml2 -E libxslt -E zlib -E libjpeg -E pkgconfig
#

{ pkgs ? import <nixpkgs> {}
}:

let

  inherit (pkgs) makeWrapper;
  inherit (pkgs.stdenv.lib) fix' extends inNixShell;

  pythonPackages =
  import "${toString pkgs.path}/pkgs/top-level/python-packages.nix" {
    inherit pkgs;
    inherit (pkgs) stdenv;
    python = pkgs.python36;
    # patching pip so it does not try to remove files when running nix-shell
    overrides =
      self: super: {
        bootstrapped-pip = super.bootstrapped-pip.overrideDerivation (old: {
          patchPhase = old.patchPhase + ''
            sed -i               -e "s|paths_to_remove.remove(auto_confirm)|#paths_to_remove.remove(auto_confirm)|"                -e "s|self.uninstalled = paths_to_remove|#self.uninstalled = paths_to_remove|"                  $out/${pkgs.python35.sitePackages}/pip/req/req_install.py
          '';
        });
      };
  };

  commonBuildInputs = with pkgs; [ libffi postgresql libxml2 libxslt zlib libjpeg pkgconfig ];
  commonDoCheck = false;

  withPackages = pkgs':
    let
      pkgs = builtins.removeAttrs pkgs' ["__unfix__"];
      interpreter = pythonPackages.buildPythonPackage {
        name = "python36-interpreter";
        buildInputs = [ makeWrapper ] ++ (builtins.attrValues pkgs);
        buildCommand = ''
          mkdir -p $out/bin
          ln -s ${pythonPackages.python.interpreter}               $out/bin/${pythonPackages.python.executable}
          for dep in ${builtins.concatStringsSep " "               (builtins.attrValues pkgs)}; do
            if [ -d "$dep/bin" ]; then
              for prog in "$dep/bin/"*; do
                if [ -f $prog ]; then
                  ln -s $prog $out/bin/`basename $prog`
                fi
              done
            fi
          done
          for prog in "$out/bin/"*; do
            wrapProgram "$prog" --prefix PYTHONPATH : "$PYTHONPATH"
          done
          pushd $out/bin
          ln -s ${pythonPackages.python.executable} python
          ln -s ${pythonPackages.python.executable}               python3
          popd
        '';
        passthru.interpreter = pythonPackages.python;
      };
    in {
      __old = pythonPackages;
      inherit interpreter;
      mkDerivation = pythonPackages.buildPythonPackage;
      packages = pkgs;
      overrideDerivation = drv: f:
        pythonPackages.buildPythonPackage (drv.drvAttrs // f drv.drvAttrs //                                            { meta = drv.meta; });
      withPackages = pkgs'':
        withPackages (pkgs // pkgs'');
    };

  python = withPackages {};

  generated = self: {

    "Flask" = python.mkDerivation {
      name = "Flask-0.11.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/55/8a/78e165d30f0c8bb5d57c429a30ee5749825ed461ad6c959688872643ffb3/Flask-0.11.1.tar.gz"; sha256 = "b4713f2bfb9ebc2966b8a49903ae0d3984781d5c878591cf2f7b484d28756b0e"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Jinja2"
      self."Werkzeug"
      self."click"
      self."itsdangerous"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/pallets/flask/";
        license = licenses.bsdOriginal;
        description = "A microframework based on Werkzeug, Jinja2 and good intentions";
      };
    };



    "Flask-Compress" = python.mkDerivation {
      name = "Flask-Compress-1.4.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/0e/2a/378bd072928f6d92fd8c417d66b00c757dc361c0405a46a0134de6fd323d/Flask-Compress-1.4.0.tar.gz"; sha256 = "468693f4ddd11ac6a41bca4eb5f94b071b763256d54136f77957cfee635badb3"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://libwilliam.github.io/flask-compress/";
        license = licenses.mit;
        description = "Compress responses in your Flask app with gzip.";
      };
    };



    "Flask-JWT" = python.mkDerivation {
      name = "Flask-JWT-0.3.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/9b/8a/5d3b2e593f1fc5c1b464aa1cbf35023a4400a2b53ce6a52801f68d7a1eeb/Flask-JWT-0.3.2.tar.gz"; sha256 = "49c0672fbde0f1cd3374bd834918d28956e3c521c7e00089cdc5380d323bd0ad"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."PyJWT"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/mattupstate/flask-jwt";
        license = licenses.mit;
        description = "JWT token authentication for Flask apps";
      };
    };



    "Flask-Login" = python.mkDerivation {
      name = "Flask-Login-0.4.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/70/96/20cae731ef27084dcb183f3a6e3073d0232f10c1fd7be76729bd7bd4b994/Flask-Login-0.4.0.tar.gz"; sha256 = "d25e356b14a59f52da0ab30c31c2ad285fa23a840f0f6971df7ed247c77082a7"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/maxcountryman/flask-login";
        license = licenses.mit;
        description = "User session management for Flask";
      };
    };



    "Flask-Mail" = python.mkDerivation {
      name = "Flask-Mail-0.9.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/05/2f/6a545452040c2556559779db87148d2a85e78a26f90326647b51dc5e81e9/Flask-Mail-0.9.1.tar.gz"; sha256 = "22e5eb9a940bf407bcf30410ecc3708f3c56cc44b29c34e1726fe85006935f41"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."blinker"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/rduplain/flask-mail";
        license = licenses.bsdOriginal;
        description = "Flask extension for sending email";
      };
    };



    "Flask-Migrate" = python.mkDerivation {
      name = "Flask-Migrate-2.0.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/f8/ba/827214fb932fb1de1fac7d992f0958c799bfc50ea471b0b8792d5e72daa6/Flask-Migrate-2.0.2.tar.gz"; sha256 = "c77272b936ec94209d5c709f9ec43947f4a25513c1b12cc25241586abdfa84b1"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."Flask-SQLAlchemy"
      self."Flask-Script"
      self."alembic"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/miguelgrinberg/flask-migrate/";
        license = licenses.mit;
        description = "SQLAlchemy database migrations for Flask applications using Alembic";
      };
    };



    "Flask-RESTful" = python.mkDerivation {
      name = "Flask-RESTful-0.3.5";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/00/f6/250e9e11e96088a69a410adf6bcaa68651a285f40b2c41e0c27b2d579f4a/Flask-RESTful-0.3.5.tar.gz"; sha256 = "cce4aeff959b571136b5af098bebe7d3deeca7eb1411c4e722ff2c5356ab4c42"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."aniso8601"
      self."pytz"
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://www.github.com/flask-restful/flask-restful/";
        license = licenses.bsdOriginal;
        description = "Simple framework for creating REST APIs";
      };
    };



    "Flask-SQLAlchemy" = python.mkDerivation {
      name = "Flask-SQLAlchemy-2.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/b3/52/227aaf4e8cebb153e239c518a9e916590b2fe0e4350e6b02d92b546b69b7/Flask-SQLAlchemy-2.1.tar.gz"; sha256 = "c5244de44cc85d2267115624d83faef3f9e8f088756788694f305a5d5ad137c5"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."SQLAlchemy"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/mitsuhiko/flask-sqlalchemy";
        license = licenses.bsdOriginal;
        description = "Adds SQLAlchemy support to your Flask application";
      };
    };



    "Flask-Script" = python.mkDerivation {
      name = "Flask-Script-2.0.6";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/00/a4/cd587b2b19f043b65bf33ceda2f6e4e6cdbd0ce18d01a52b9559781b1da6/Flask-Script-2.0.6.tar.gz"; sha256 = "6425963d91054cfcc185807141c7314a9c5ad46325911bd24dcb489bd0161c65"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/smurfix/flask-script";
        license = licenses.bsdOriginal;
        description = "Scripting support for Flask";
      };
    };



    "Flask-User" = python.mkDerivation {
      name = "Flask-User-0.6.19";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/f8/e7/63794a1df4b80b709a935244f4c965043f8597b17e3a6c3745123dd8577a/Flask-User-0.6.19.tar.gz"; sha256 = "601abcc0343dfbae0c56273d98362d5cdc266ac84d20b3f65a212e4a2c83b302"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."Flask-Login"
      self."Flask-Mail"
      self."Flask-SQLAlchemy"
      self."Flask-WTF"
      self."bcrypt"
      self."passlib"
      self."pycryptodome"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/lingthio/Flask-User";
        license = licenses.bsdOriginal;
        description = "Customizable User Authentication and Management, and more.";
      };
    };



    "Flask-WTF" = python.mkDerivation {
      name = "Flask-WTF-0.14.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/ba/15/00a9693180f214225a2c0b1bb9077f3b0b21f2e86522cbba22e8ad6e570c/Flask-WTF-0.14.2.tar.gz"; sha256 = "5d14d55cfd35f613d99ee7cba0fc3fbbe63ba02f544d349158c14ca15561cc36"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Flask"
      self."WTForms"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/lepture/flask-wtf";
        license = licenses.bsdOriginal;
        description = "Simple integration of Flask and WTForms.";
      };
    };



    "Jinja2" = python.mkDerivation {
      name = "Jinja2-2.10";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/56/e6/332789f295cf22308386cf5bbd1f4e00ed11484299c5d7383378cf48ba47/Jinja2-2.10.tar.gz"; sha256 = "f84be1bb0040caca4cea721fcbbbbd61f9be9464ca236387158b0feea01914a4"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."MarkupSafe"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://jinja.pocoo.org/";
        license = licenses.bsdOriginal;
        description = "A small but fast and easy to use stand-alone template engine written in pure python.";
      };
    };



    "LinkHeader" = python.mkDerivation {
      name = "LinkHeader-0.4.3";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/27/d4/eb1da743b2dc825e936ef1d9e04356b5701e3a9ea022c7aaffdf4f6b0594/LinkHeader-0.4.3.tar.gz"; sha256 = "7fbbc35c0ba3fbbc530571db7e1c886e7db3d718b29b345848ac9686f21b50c3"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://bitbucket.org/asplake/link_header";
        license = licenses.bsdOriginal;
        description = "Parse and format link headers according to RFC 5988 \"Web Linking\"";
      };
    };



    "Mako" = python.mkDerivation {
      name = "Mako-1.0.7";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/eb/f3/67579bb486517c0d49547f9697e36582cd19dafb5df9e687ed8e22de57fa/Mako-1.0.7.tar.gz"; sha256 = "4e02fde57bd4abb5ec400181e4c314f56ac3e49ba4fb8b0d50bba18cb27d25ae"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."MarkupSafe"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://www.makotemplates.org/";
        license = licenses.mit;
        description = "A super-fast templating language that borrows the  best ideas from the existing templating languages.";
      };
    };



    "MarkupSafe" = python.mkDerivation {
      name = "MarkupSafe-1.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz"; sha256 = "a6be69091dac236ea9c6bc7d012beab42010fa914c459791d627dad4910eb665"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/pallets/markupsafe";
        license = licenses.bsdOriginal;
        description = "Implements a XML/HTML/XHTML Markup safe string for Python";
      };
    };



    "Pillow" = python.mkDerivation {
      name = "Pillow-5.0.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/0f/57/25be1a4c2d487942c3ed360f6eee7f41c5b9196a09ca71c54d1a33c968d9/Pillow-5.0.0.tar.gz"; sha256 = "12f29d6c23424f704c66b5b68c02fe0b571504459605cfe36ab8158359b0e1bb"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://python-pillow.org";
        license = "License :: Other/Proprietary License";
        description = "Python Imaging Library (Fork)";
      };
    };



    "PyJWT" = python.mkDerivation {
      name = "PyJWT-1.4.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/8f/10/9ce7e91d8ec9d852db6f9f2b076811d9f51ed7b0360602432d95e6ea4feb/PyJWT-1.4.2.tar.gz"; sha256 = "87a831b7a3bfa8351511961469ed0462a769724d4da48a501cb8c96d1e17f570"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/jpadilla/pyjwt";
        license = licenses.mit;
        description = "JSON Web Token implementation in Python";
      };
    };



    "PyYAML" = python.mkDerivation {
      name = "PyYAML-3.12";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/4a/85/db5a2df477072b2902b0eb892feb37d88ac635d36245a72a6a69b23b383a/PyYAML-3.12.tar.gz"; sha256 = "592766c6303207a20efc445587778322d7f73b161bd994f227adaa341ba212ab"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://pyyaml.org/wiki/PyYAML";
        license = licenses.mit;
        description = "YAML parser and emitter for Python";
      };
    };



    "SQLAlchemy" = python.mkDerivation {
      name = "SQLAlchemy-1.2.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/b9/fb/a56d2fc0ce3571328fa872734ad124cae25a4cea422088987f865fb71787/SQLAlchemy-1.2.2.tar.gz"; sha256 = "64b4720f0a8e033db0154d3824f5bf677cf2797e11d44743cf0aebd2a0499d9d"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."psycopg2"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://www.sqlalchemy.org";
        license = licenses.mit;
        description = "Database Abstraction Library";
      };
    };



    "WTForms" = python.mkDerivation {
      name = "WTForms-2.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/bf/91/2e553b86c55e9cf2f33265de50e052441fb753af46f5f20477fe9c61280e/WTForms-2.1.zip"; sha256 = "ffdf10bd1fa565b8233380cb77a304cd36fd55c73023e91d4b803c96bc11d46f"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://wtforms.simplecodes.com/";
        license = licenses.bsdOriginal;
        description = "A flexible forms validation and rendering library for python web development.";
      };
    };



    "Werkzeug" = python.mkDerivation {
      name = "Werkzeug-0.14.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/9f/08/a3bb1c045ec602dc680906fc0261c267bed6b3bb4609430aff92c3888ec8/Werkzeug-0.14.1.tar.gz"; sha256 = "c3fd7a7d41976d9f44db327260e263132466836cef6f91512889ed60ad26557c"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://www.palletsprojects.org/p/werkzeug/";
        license = licenses.bsdOriginal;
        description = "The comprehensive WSGI web application library.";
      };
    };



    "alembic" = python.mkDerivation {
      name = "alembic-0.9.7";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/80/bb/f294b8f7d6c4a0ab81babc6b863a0d9f708d93c5d5c5921910be765ca779/alembic-0.9.7.tar.gz"; sha256 = "46f4849c6dce69f54dd5001b3215b6a983dee6b17512efee10e237fa11f20cfa"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Mako"
      self."SQLAlchemy"
      self."python-dateutil"
      self."python-editor"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://bitbucket.org/zzzeek/alembic";
        license = licenses.mit;
        description = "A database migration tool for SQLAlchemy.";
      };
    };



    "aniso8601" = python.mkDerivation {
      name = "aniso8601-2.0.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/3c/31/c9bae7924453fd3da0587b22c7dc4df90bae85326961eb9c2445481fd94f/aniso8601-2.0.0.tar.gz"; sha256 = "085786415d3550e89785ffbedaa9bb37d41de0707a1268bdbba11249064b71d1"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."python-dateutil"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://bitbucket.org/nielsenb/aniso8601";
        license = licenses.bsdOriginal;
        description = "A library for parsing ISO 8601 strings.";
      };
    };



    "bcrypt" = python.mkDerivation {
      name = "bcrypt-3.1.4";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/f3/ec/bb6b384b5134fd881b91b6aa3a88ccddaad0103857760711a5ab8c799358/bcrypt-3.1.4.tar.gz"; sha256 = "67ed1a374c9155ec0840214ce804616de49c3df9c5bc66740687c1c9b1cd9e8d"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."cffi"
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/pyca/bcrypt/";
        license = licenses.asl20;
        description = "Modern password hashing for your software and your servers";
      };
    };



    "beautifulsoup4" = python.mkDerivation {
      name = "beautifulsoup4-4.6.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/fa/8d/1d14391fdaed5abada4e0f63543fef49b8331a34ca60c88bd521bcf7f782/beautifulsoup4-4.6.0.tar.gz"; sha256 = "808b6ac932dccb0a4126558f7dfdcf41710dd44a4ef497a0bb59a77f9f078e89"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."lxml"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://www.crummy.com/software/BeautifulSoup/bs4/";
        license = licenses.mit;
        description = "Screen-scraping library";
      };
    };



    "blinker" = python.mkDerivation {
      name = "blinker-1.4";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/1b/51/e2a9f3b757eb802f61dc1f2b09c8c99f6eb01cf06416c0671253536517b6/blinker-1.4.tar.gz"; sha256 = "471aee25f3992bd325afa3772f1063dbdbbca947a041b8b89466dc00d606f8b6"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://pythonhosted.org/blinker/";
        license = licenses.mit;
        description = "Fast, simple object-to-object and broadcast signaling";
      };
    };



    "cachetools" = python.mkDerivation {
      name = "cachetools-2.0.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/54/e4/ddaa319bf53f04cda4ef99201de1c402871151b6edefe631bd426dc621a3/cachetools-2.0.1.tar.gz"; sha256 = "ede01f2d3cbd6ddc9e35e16c2b0ce011d8bb70ce0dbaf282f5b4df24b213bc5d"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/tkem/cachetools";
        license = licenses.mit;
        description = "Extensible memoizing collections and decorators";
      };
    };



    "certifi" = python.mkDerivation {
      name = "certifi-2018.1.18";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/15/d4/2f888fc463d516ff7bf2379a4e9a552fef7f22a94147655d9b1097108248/certifi-2018.1.18.tar.gz"; sha256 = "edbc3f203427eef571f79a7692bb160a2b0f7ccaa31953e99bd17e307cf63f7d"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://certifi.io/";
        license = licenses.mpl20;
        description = "Python package for providing Mozilla's CA Bundle.";
      };
    };



    "cffi" = python.mkDerivation {
      name = "cffi-1.11.4";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/10/f7/3b302ff34045f25065091d40e074479d6893882faef135c96f181a57ed06/cffi-1.11.4.tar.gz"; sha256 = "df9083a992b17a28cd4251a3f5c879e0198bb26c9e808c4647e0a18739f1d11d"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."pycparser"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://cffi.readthedocs.org";
        license = licenses.mit;
        description = "Foreign Function Interface for Python calling C code.";
      };
    };



    "chardet" = python.mkDerivation {
      name = "chardet-3.0.4";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/fc/bb/a5768c230f9ddb03acc9ef3f0d4a3cf93462473795d18e9535498c8f929d/chardet-3.0.4.tar.gz"; sha256 = "84ab92ed1c4d4f16916e05906b6b75a6c0fb5db821cc65e70cbd64a3e2a5eaae"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/chardet/chardet";
        license = licenses.lgpl2;
        description = "Universal encoding detector for Python 2 and 3";
      };
    };



    "click" = python.mkDerivation {
      name = "click-6.7";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/95/d9/c3336b6b5711c3ab9d1d3a80f1a3e2afeb9d8c02a7166462f6cc96570897/click-6.7.tar.gz"; sha256 = "f15516df478d5a56180fbf80e68f206010e6d160fc39fa508b65e035fd75130b"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/mitsuhiko/click";
        license = licenses.bsdOriginal;
        description = "A simple wrapper around optparse for powerful command line utilities.";
      };
    };



    "cssselect" = python.mkDerivation {
      name = "cssselect-1.0.3";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/52/ea/f31e1d2e9eb130fda2a631e22eac369dc644e8807345fbed5113f2d6f92b/cssselect-1.0.3.tar.gz"; sha256 = "066d8bc5229af09617e24b3ca4d52f1f9092d9e061931f4184cd572885c23204"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/scrapy/cssselect";
        license = licenses.bsdOriginal;
        description = "cssselect parses CSS3 Selectors and translates them to XPath 1.0";
      };
    };



    "feedfinder2" = python.mkDerivation {
      name = "feedfinder2-0.0.4";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/35/82/1251fefec3bb4b03fd966c7e7f7a41c9fc2bb00d823a34c13f847fd61406/feedfinder2-0.0.4.tar.gz"; sha256 = "3701ee01a6c85f8b865a049c30ba0b4608858c803fe8e30d1d289fdbe89d0efe"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."beautifulsoup4"
      self."requests"
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/dfm/feedfinder2";
        license = licenses.mit;
        description = "Find the feed URLs for a website.";
      };
    };



    "feedparser" = python.mkDerivation {
      name = "feedparser-5.2.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/91/d8/7d37fec71ff7c9dbcdd80d2b48bcdd86d6af502156fc93846fb0102cb2c4/feedparser-5.2.1.tar.bz2"; sha256 = "ce875495c90ebd74b179855449040003a1beb40cd13d5f037a0654251e260b02"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/kurtmckee/feedparser";
        license = "License :: OSI Approved";
        description = "Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds";
      };
    };



    "google-auth" = python.mkDerivation {
      name = "google-auth-1.3.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/82/1a/161b77d248e55f85a9cb326d98fffcbc098f804ae07790783a02660299cb/google-auth-1.3.0.tar.gz"; sha256 = "d119b5954393d81c4a986ab420cf2c8129fc95ff5c4c6bb8ab5c8f3e6446394f"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."cachetools"
      self."pyasn1-modules"
      self."rsa"
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/GoogleCloudPlatform/google-auth-library-python";
        license = licenses.asl20;
        description = "Google Authentication Library";
      };
    };



    "gunicorn" = python.mkDerivation {
      name = "gunicorn-19.6.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/84/ce/7ea5396efad1cef682bbc4068e72a0276341d9d9d0f501da609fab9fcb80/gunicorn-19.6.0.tar.gz"; sha256 = "813f6916d18a4c8e90efde72f419308b357692f81333cb1125f80013d22fb618"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://gunicorn.org";
        license = licenses.mit;
        description = "WSGI HTTP Server for UNIX";
      };
    };



    "idna" = python.mkDerivation {
      name = "idna-2.6";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/f4/bd/0467d62790828c23c47fc1dfa1b1f052b24efdf5290f071c7a91d0d82fd3/idna-2.6.tar.gz"; sha256 = "2c6a5de3089009e3da7c5dde64a141dbc8551d5b7f6cf4ed7c2568d0cc520a8f"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/kjd/idna";
        license = licenses.bsdOriginal;
        description = "Internationalized Domain Names in Applications (IDNA)";
      };
    };



    "itsdangerous" = python.mkDerivation {
      name = "itsdangerous-0.24";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz"; sha256 = "cbb3fcf8d3e33df861709ecaf89d9e6629cff0a217bc2848f1b41cd30d360519"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/mitsuhiko/itsdangerous";
        license = licenses.bsdOriginal;
        description = "Various helpers to pass trusted data to untrusted environments and back.";
      };
    };



    "jieba3k" = python.mkDerivation {
      name = "jieba3k-0.35.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/a9/cb/2c8332bcdc14d33b0bedd18ae0a4981a069c3513e445120da3c3f23a8aaa/jieba3k-0.35.1.zip"; sha256 = "980a4f2636b778d312518066be90c7697d410dd5a472385f5afced71a2db1c10"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/fxsjy";
        license = "";
        description = "Chinese Words Segementation Utilities";
      };
    };



    "lxml" = python.mkDerivation {
      name = "lxml-4.1.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/e1/4c/d83979fbc66a2154850f472e69405572d89d2e6a6daee30d18e83e39ef3a/lxml-4.1.1.tar.gz"; sha256 = "940caef1ec7c78e0c34b0f6b94fe42d0f2022915ffc78643d28538a5cfd0f40e"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."beautifulsoup4"
      self."cssselect"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://lxml.de/";
        license = licenses.bsdOriginal;
        description = "Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.";
      };
    };



    "newspaper3k" = python.mkDerivation {
      name = "newspaper3k-0.1.9";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/85/66/3166c7fcf2736aaa7f682b4ba1b05d4e89aff9ae346de3116a366f52862d/newspaper3k-0.1.9.tar.gz"; sha256 = "0ac2c1d18e34bbf37c2e41b9b2f241aaefa1da9ba467d27ad0975ff6042016de"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."Pillow"
      self."PyYAML"
      self."beautifulsoup4"
      self."cssselect"
      self."feedfinder2"
      self."feedparser"
      self."jieba3k"
      self."lxml"
      self."nltk"
      self."python-dateutil"
      self."requests"
      self."tldextract"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/codelucas/newspaper/";
        license = licenses.mit;
        description = "Simplified python article discovery & extraction.";
      };
    };



    "nltk" = python.mkDerivation {
      name = "nltk-3.2.5";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/cc/87/76e691bbf1759ad6af5831649aae6a8d2fa184a1bcc71018ca6300399e5f/nltk-3.2.5.tar.gz"; sha256 = "2661f9971d983db314bbebd51ba770811a362c6597fd0f303bb1d3beadcb4834"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."requests"
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://nltk.org/";
        license = licenses.asl20;
        description = "Natural Language Toolkit";
      };
    };



    "passlib" = python.mkDerivation {
      name = "passlib-1.7.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/25/4b/6fbfc66aabb3017cd8c3bd97b37f769d7503ead2899bf76e570eb91270de/passlib-1.7.1.tar.gz"; sha256 = "3d948f64138c25633613f303bcc471126eae67c04d5e3f6b7b8ce6242f8653e0"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."bcrypt"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://bitbucket.org/ecollins/passlib";
        license = licenses.bsdOriginal;
        description = "comprehensive password hashing framework supporting over 30 schemes";
      };
    };



    "psycopg2" = python.mkDerivation {
      name = "psycopg2-2.7.3.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/dd/47/000b405d73ca22980684fd7bd3318690cc03cfa3b2ae1c5b7fff8050b28a/psycopg2-2.7.3.2.tar.gz"; sha256 = "5c3213be557d0468f9df8fe2487eaf2990d9799202c5ff5cb8d394d09fad9b2a"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://initd.org/psycopg/";
        license = licenses.lgpl2;
        description = "psycopg2 - Python-PostgreSQL Database Adapter";
      };
    };



    "pyasn1" = python.mkDerivation {
      name = "pyasn1-0.4.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/eb/3d/b7d0fdf4a882e26674c68c20f40682491377c4db1439870f5b6f862f76ed/pyasn1-0.4.2.tar.gz"; sha256 = "d258b0a71994f7770599835249cece1caef3c70def868c4915e6e5ca49b67d15"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/etingof/pyasn1";
        license = licenses.bsdOriginal;
        description = "ASN.1 types and codecs";
      };
    };



    "pyasn1-modules" = python.mkDerivation {
      name = "pyasn1-modules-0.2.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/ab/76/36ab0e099e6bd27ed95b70c2c86c326d3affa59b9b535c63a2f892ac9f45/pyasn1-modules-0.2.1.tar.gz"; sha256 = "af00ea8f2022b6287dc375b2c70f31ab5af83989fc6fe9eacd4976ce26cd7ccc"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."pyasn1"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/etingof/pyasn1-modules";
        license = licenses.bsdOriginal;
        description = "A collection of ASN.1-based protocols modules.";
      };
    };



    "pycparser" = python.mkDerivation {
      name = "pycparser-2.18";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/8c/2d/aad7f16146f4197a11f8e91fb81df177adcc2073d36a17b1491fd09df6ed/pycparser-2.18.tar.gz"; sha256 = "99a8ca03e29851d96616ad0404b4aad7d9ee16f25c9f9708a11faf2810f7b226"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/eliben/pycparser";
        license = licenses.bsdOriginal;
        description = "C parser in Python";
      };
    };



    "pycryptodome" = python.mkDerivation {
      name = "pycryptodome-3.4.8";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/5e/26/4ad71dbff7e7d5012d8388237e98f23efcf85db8bd4c76325e0da6df023a/pycryptodome-3.4.8.tar.gz"; sha256 = "ede7f1f44b0895feb8ddbf882d1a7eb504deb3fa34fcc4860d6065c25cbdf175"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://www.pycryptodome.org";
        license = licenses.bsdOriginal;
        description = "Cryptographic library for Python";
      };
    };



    "python-dateutil" = python.mkDerivation {
      name = "python-dateutil-2.6.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/54/bb/f1db86504f7a49e1d9b9301531181b00a1c7325dc85a29160ee3eaa73a54/python-dateutil-2.6.1.tar.gz"; sha256 = "891c38b2a02f5bb1be3e4793866c8df49c7d19baabf9c1bad62547e0b4866aca"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://dateutil.readthedocs.io";
        license = licenses.bsdOriginal;
        description = "Extensions to the standard Python datetime module";
      };
    };



    "python-editor" = python.mkDerivation {
      name = "python-editor-1.0.3";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/65/1e/adf6e000ea5dc909aa420352d6ba37f16434c8a3c2fa030445411a1ed545/python-editor-1.0.3.tar.gz"; sha256 = "a3c066acee22a1c94f63938341d4fb374e3fdd69366ed6603d7b24bed1efc565"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/fmoo/python-editor";
        license = "License :: OSI Approved :: Apache Software License";
        description = "Programmatically open an editor, capture the result.";
      };
    };



    "pytz" = python.mkDerivation {
      name = "pytz-2017.3";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/60/88/d3152c234da4b2a1f7a989f89609ea488225eaea015bc16fbde2b3fdfefa/pytz-2017.3.zip"; sha256 = "fae4cffc040921b8a2d60c6cf0b5d662c1190fe54d718271db4eb17d44a185b7"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://pythonhosted.org/pytz";
        license = licenses.mit;
        description = "World timezone definitions, modern and historical";
      };
    };



    "redis" = python.mkDerivation {
      name = "redis-2.10.6";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/09/8d/6d34b75326bf96d4139a2ddd8e74b80840f800a0a79f9294399e212cb9a7/redis-2.10.6.tar.gz"; sha256 = "a22ca993cea2962dbb588f9f30d0015ac4afcc45bee27d3978c0dbe9e97c6c0f"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/andymccurdy/redis-py";
        license = licenses.mit;
        description = "Python client for Redis key-value store";
      };
    };



    "requests" = python.mkDerivation {
      name = "requests-2.18.4";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/b0/e1/eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a329aa8d09/requests-2.18.4.tar.gz"; sha256 = "9c443e7324ba5b85070c4a818ade28bfabedf16ea10206da1132edaa6dda237e"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."certifi"
      self."chardet"
      self."idna"
      self."urllib3"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://python-requests.org";
        license = licenses.asl20;
        description = "Python HTTP for Humans.";
      };
    };



    "requests-file" = python.mkDerivation {
      name = "requests-file-1.4.3";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/a0/f9/8c1712aea1b70c6a77db322bb18610a078ba8f44876e95289137953db30d/requests-file-1.4.3.tar.gz"; sha256 = "8f04aa6201bacda0567e7ac7f677f1499b0fc76b22140c54bc06edf1ba92e2fa"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."requests"
      self."six"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://github.com/dashea/requests-file";
        license = licenses.asl20;
        description = "File transport adapter for Requests";
      };
    };



    "rq" = python.mkDerivation {
      name = "rq-0.7.1";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/4a/ee/30024f604d33b18e9e15e5780f20e1dc51a96f1a1162889694939a390593/rq-0.7.1.tar.gz"; sha256 = "b0e98fcfe980cbc7644447d17ea2c177fcbd5c04f1f92d5136c47f00ed2d583d"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."click"
      self."redis"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/nvie/rq/";
        license = licenses.bsdOriginal;
        description = "RQ is a simple, lightweight, library for creating background jobs, and processing them.";
      };
    };



    "rsa" = python.mkDerivation {
      name = "rsa-3.4.2";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/14/89/adf8b72371e37f3ca69c6cb8ab6319d009c4a24b04a31399e5bd77d9bb57/rsa-3.4.2.tar.gz"; sha256 = "25df4e10c263fb88b5ace923dd84bf9aa7f5019687b5e55382ffcdb8bede9db5"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."pyasn1"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://stuvel.eu/rsa";
        license = "License :: OSI Approved :: Apache Software License";
        description = "Pure-Python RSA implementation";
      };
    };



    "six" = python.mkDerivation {
      name = "six-1.11.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/16/d8/bc6316cf98419719bd59c91742194c111b6f2e85abac88e496adefaf7afe/six-1.11.0.tar.gz"; sha256 = "70e8a77beed4562e7f14fe23a786b54f6296e34344c23bc42f07b15018ff98e9"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [ ];
      meta = with pkgs.stdenv.lib; {
        homepage = "http://pypi.python.org/pypi/six/";
        license = licenses.mit;
        description = "Python 2 and 3 compatibility utilities";
      };
    };



    "tldextract" = python.mkDerivation {
      name = "tldextract-2.2.0";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/7d/8e/83b6cec169e2af1ea82447af844012fa445a414bcba326342ed935274dcb/tldextract-2.2.0.tar.gz"; sha256 = "29797125db1f2e72ce2ee51f7a764ec8b1e6588812520795ffeae93bcd46bab4"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."idna"
      self."requests"
      self."requests-file"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://github.com/john-kurkowski/tldextract";
        license = licenses.bsdOriginal;
        description = "Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List. By default, this includes the public ICANN TLDs and their exceptions. You can optionally support the Public Suffix List's private domains as well.";
      };
    };



    "urllib3" = python.mkDerivation {
      name = "urllib3-1.22";
      src = pkgs.fetchurl { url = "https://pypi.python.org/packages/ee/11/7c59620aceedcc1ef65e156cc5ce5a24ef87be4107c2b74458464e437a5d/urllib3-1.22.tar.gz"; sha256 = "cc44da8e1145637334317feebd728bd869a35285b93cbb4cca2577da7e62db4f"; };
      doCheck = commonDoCheck;
      buildInputs = commonBuildInputs;
      propagatedBuildInputs = [
      self."certifi"
      self."idna"
    ];
      meta = with pkgs.stdenv.lib; {
        homepage = "https://urllib3.readthedocs.io/";
        license = licenses.mit;
        description = "HTTP library with thread-safe connection pooling, file post, and more.";
      };
    };

  };
  localOverridesFile = ./requirements_override.nix;
  overrides = import localOverridesFile { inherit pkgs python; };
  commonOverrides = [

  ];
  allOverrides =
    (if (builtins.pathExists localOverridesFile)
     then [overrides] else [] ) ++ commonOverrides;

in python.withPackages
   (fix' (pkgs.lib.fold
            extends
            generated
            allOverrides
         )
   )