# generated using pypi2nix tool (version: 1.6.0)
#
# COMMAND:
#   pypi2nix -V 3.5 -r requirements.txt -E libffi -E postgresql -E libxml2 -E libxslt -E zlib -E libjpeg -E pkgconfig -v
#

{ pkgs, python, commonBuildInputs ? [], commonDoCheck ? false }:

self: {

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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "A microframework based on Werkzeug, Jinja2 and good intentions";
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
      homepage = "";
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
      homepage = "";
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
      homepage = "";
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
      homepage = "";
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
      homepage = "";
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Adds SQLAlchemy support to your Flask application";
    };
  };



  "Flask-Script" = python.mkDerivation {
    name = "Flask-Script-2.0.5";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/66/e9/2b3c7c548a6bad0b59da21e2050613da43aae4da617fb98847efa3e09a43/Flask-Script-2.0.5.tar.gz"; sha256 = "cef76eac751396355429a14c38967bb14d4973c53e07dec94af5cc8fb017107f"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."Flask"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Scripting support for Flask";
    };
  };



  "Flask-User" = python.mkDerivation {
    name = "Flask-User-0.6.11";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/48/3d/9e94d980626a4c533b8bf3e0ae203574ded41274480b6cc9fe319f79c227/Flask-User-0.6.11.tar.gz"; sha256 = "fc12968b8fa437942116c0f03b2346b25b9b25ee6ff63acb89f626f80aef35bc"; };
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Customizable User Account Management for Flask: Register, Confirm email, Login, Change username, Change password, Forgot password and more.";
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Simple integration of Flask and WTForms.";
    };
  };



  "Jinja2" = python.mkDerivation {
    name = "Jinja2-2.9.5";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/71/59/d7423bd5e7ddaf3a1ce299ab4490e9044e8dfd195420fc83a24de9e60726/Jinja2-2.9.5.tar.gz"; sha256 = "702a24d992f856fa8d5a7a36db6128198d0c21e1da34448ca236c42e92384825"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."MarkupSafe"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Parse and format link headers according to RFC 5988 \"Web Linking\"";
    };
  };



  "Mako" = python.mkDerivation {
    name = "Mako-1.0.6";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/56/4b/cb75836863a6382199aefb3d3809937e21fa4cb0db15a4f4ba0ecc2e7e8e/Mako-1.0.6.tar.gz"; sha256 = "48559ebd872a8e77f92005884b3d88ffae552812cdf17db6768e5c3be5ebbe0d"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."MarkupSafe"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "A super-fast templating language that borrows the  best ideas from the existing templating languages.";
    };
  };



  "MarkupSafe" = python.mkDerivation {
    name = "MarkupSafe-0.23";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/c0/41/bae1254e0396c0cc8cf1751cb7d9afc90a602353695af5952530482c963f/MarkupSafe-0.23.tar.gz"; sha256 = "a4ec1aff59b95a14b45eb2e23761a0179e98319da5a7eb76b56ea8cdc7b871c3"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Implements a XML/HTML/XHTML Markup safe string for Python";
    };
  };



  "Pillow" = python.mkDerivation {
    name = "Pillow-4.0.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/8d/80/eca7a2d1a3c2dafb960f32f844d570de988e609f5fd17de92e1cf6a01b0a/Pillow-4.0.0.tar.gz"; sha256 = "ee26d2d7e7e300f76ba7b796014c04011394d0c4a5ed9a288264a3e443abca50"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."olefile"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = "Standard PIL License";
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
      homepage = "";
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
      homepage = "";
      license = licenses.mit;
      description = "YAML parser and emitter for Python";
    };
  };



  "SQLAlchemy" = python.mkDerivation {
    name = "SQLAlchemy-1.1.6";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/24/de/66d96cbad7a91443af1399469e9aa0aec8a41669ba6d0faae8b8411ddb27/SQLAlchemy-1.1.6.tar.gz"; sha256 = "815924e3218d878ddd195d2f9f5bf3d2bb39fabaddb1ea27dace6ac27d9865e4"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."psycopg2"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "A flexible forms validation and rendering library for python web development.";
    };
  };



  "Werkzeug" = python.mkDerivation {
    name = "Werkzeug-0.11.15";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/fe/7f/6d70f765ce5484e07576313897793cb49333dd34e462488ee818d17244af/Werkzeug-0.11.15.tar.gz"; sha256 = "455d7798ac263266dbd38d4841f7534dd35ca9c3da4a8df303f8488f38f3bcc0"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "The Swiss Army knife of Python web development";
    };
  };



  "alembic" = python.mkDerivation {
    name = "alembic-0.9.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/84/6e/31f0e7058c82ce177b58e52f927756fca6aea33c8565ad8a9ce42ce144a9/alembic-0.9.0.tar.gz"; sha256 = "d6ccb61fa5abc266fde9c1303d8640498ebc72c7bf8e1591acf6a89a2b1dfa19"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."Mako"
      self."SQLAlchemy"
      self."python-editor"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "A database migration tool for SQLAlchemy.";
    };
  };



  "aniso8601" = python.mkDerivation {
    name = "aniso8601-1.2.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/5b/fb/251a0dd2f4710e60664ddd8bd3485bd8362530f47af9e88f4061fe589ebf/aniso8601-1.2.0.tar.gz"; sha256 = "502400f82574afa804cc915d83f15c67533d364dcd594f8a6b9d2053f3404dd4"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."python-dateutil"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "A library for parsing ISO 8601 strings.";
    };
  };



  "bcrypt" = python.mkDerivation {
    name = "bcrypt-3.1.3";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/58/e9/6d7f1d883d8c5876470b5d187d72c04f2a9954d61e71e7eb5d2ea2a50442/bcrypt-3.1.3.tar.gz"; sha256 = "6645c8d0ad845308de3eb9be98b6fd22a46ec5412bfc664a423e411cdd8f5488"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."cffi"
      self."six"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.asl20;
      description = "Modern password hashing for your software and your servers";
    };
  };



  "beautifulsoup4" = python.mkDerivation {
    name = "beautifulsoup4-4.5.3";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/9b/a5/c6fa2d08e6c671103f9508816588e0fb9cec40444e8e72993f3d4c325936/beautifulsoup4-4.5.3.tar.gz"; sha256 = "b21ca09366fa596043578fd4188b052b46634d22059e68dd0077d9ee77e08a3e"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."lxml"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
      license = licenses.mit;
      description = "Fast, simple object-to-object and broadcast signaling";
    };
  };



  "cffi" = python.mkDerivation {
    name = "cffi-1.9.1";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/a1/32/e3d6c3a8b5461b903651dd6ce958ed03c093d2e00128e3f33ea69f1d7965/cffi-1.9.1.tar.gz"; sha256 = "563e0bd53fda03c151573217b3a49b3abad8813de9dd0632e10090f6190fdaf8"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."pycparser"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "Foreign Function Interface for Python calling C code.";
    };
  };



  "click" = python.mkDerivation {
    name = "click-6.7";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/95/d9/c3336b6b5711c3ab9d1d3a80f1a3e2afeb9d8c02a7166462f6cc96570897/click-6.7.tar.gz"; sha256 = "f15516df478d5a56180fbf80e68f206010e6d160fc39fa508b65e035fd75130b"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "A simple wrapper around optparse for powerful command line utilities.";
    };
  };



  "cssselect" = python.mkDerivation {
    name = "cssselect-1.0.1";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/77/ff/9c865275cd19290feba56344eba570e719efb7ca5b34d67ed12b22ebbb0d/cssselect-1.0.1.tar.gz"; sha256 = "73db1c054b9348409e2862fc6c0dde5c4e4fbe4da64c5c5a9e05fbea45744077"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
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
      homepage = "";
      license = "License :: OSI Approved";
      description = "Universal feed parser, handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds";
    };
  };



  "gunicorn" = python.mkDerivation {
    name = "gunicorn-19.6.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/84/ce/7ea5396efad1cef682bbc4068e72a0276341d9d9d0f501da609fab9fcb80/gunicorn-19.6.0.tar.gz"; sha256 = "813f6916d18a4c8e90efde72f419308b357692f81333cb1125f80013d22fb618"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "WSGI HTTP Server for UNIX";
    };
  };



  "idna" = python.mkDerivation {
    name = "idna-2.3";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/81/62/c32d933d487d9756f55782de85a70b90cd6827a59a3e330f6adada408241/idna-2.3.tar.gz"; sha256 = "fe077ccaefbcc84b1b1fe8fae9dc0c3b71079df4bf5398796ece0b84be9cbdc3"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
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
      homepage = "";
      license = "";
      description = "Chinese Words Segementation Utilities";
    };
  };



  "lxml" = python.mkDerivation {
    name = "lxml-3.7.3";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/39/e8/a8e0b1fa65dd021d48fe21464f71783655f39a41f218293c1c590d54eb82/lxml-3.7.3.tar.gz"; sha256 = "aa502d78a51ee7d127b4824ff96500f0181d3c7826e6ee7b800d068be79361c7"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."beautifulsoup4"
      self."cssselect"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
      license = licenses.mit;
      description = "Simplified python article discovery & extraction.";
    };
  };



  "nltk" = python.mkDerivation {
    name = "nltk-3.2.2";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/13/ce/cba8bf82c8ab538d444ea4ab6f4eb1d80340c7b737d7a8d1f08b429fccae/nltk-3.2.2.tar.gz"; sha256 = "1b37db344770021c9be3d68f48d1667a8dae6eeff0e502b7bfb01638d288a88e"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."six"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.asl20;
      description = "Natural Language Toolkit";
    };
  };



  "olefile" = python.mkDerivation {
    name = "olefile-0.44";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/35/17/c15d41d5a8f8b98cc3df25eb00c5cee76193114c78e5674df6ef4ac92647/olefile-0.44.zip"; sha256 = "61f2ca0cd0aa77279eb943c07f607438edf374096b66332fae1ee64a6f0f73ad"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Python package to parse, read and write Microsoft OLE2 files (Structured Storage or Compound Document, Microsoft Office) - Improved version of the OleFileIO module from PIL, the Python Image Library.";
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "comprehensive password hashing framework supporting over 30 schemes";
    };
  };



  "psycopg2" = python.mkDerivation {
    name = "psycopg2-2.6.2";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/7b/a8/dc2d50a6f37c157459cd18bab381c8e6134b9381b50fbe969997b2ae7dbc/psycopg2-2.6.2.tar.gz"; sha256 = "70490e12ed9c5c818ecd85d185d363335cc8a8cbf7212e3c185431c79ff8c05c"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.lgpl2;
      description = "psycopg2 - Python-PostgreSQL Database Adapter";
    };
  };



  "pycparser" = python.mkDerivation {
    name = "pycparser-2.17";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/be/64/1bb257ffb17d01f4a38d7ce686809a736837ad4371bcc5c42ba7a715c3ac/pycparser-2.17.tar.gz"; sha256 = "0aac31e917c24cb3357f5a4d5566f2cc91a19ca41862f6c3c22dc60a629673b6"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "C parser in Python";
    };
  };



  "pycryptodome" = python.mkDerivation {
    name = "pycryptodome-3.4.5";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/45/ca/f0c2ca6c65084d60f68553cf072de7db0d918c7bb07ece88781f6af24625/pycryptodome-3.4.5.tar.gz"; sha256 = "be84544eadc2bb71d4ace39e4984ed2990111f053f24267a07afb4b4e1e5428f"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Cryptographic library for Python";
    };
  };



  "python-dateutil" = python.mkDerivation {
    name = "python-dateutil-2.6.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/51/fc/39a3fbde6864942e8bb24c93663734b74e281b984d1b8c4f95d64b0c21f6/python-dateutil-2.6.0.tar.gz"; sha256 = "62a2f8df3d66f878373fd0072eacf4ee52194ba302e00082828e0d263b0418d2"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."six"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
      license = "License :: OSI Approved :: Apache Software License";
      description = "Programmatically open an editor, capture the result.";
    };
  };



  "pytz" = python.mkDerivation {
    name = "pytz-2016.10";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/d0/e1/aca6ef73a7bd322a7fc73fd99631ee3454d4fc67dc2bee463e2adf6bb3d3/pytz-2016.10.tar.bz2"; sha256 = "7016b2c4fa075c564b81c37a252a5fccf60d8964aa31b7f5eae59aeb594ae02b"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "World timezone definitions, modern and historical";
    };
  };



  "redis" = python.mkDerivation {
    name = "redis-2.10.5";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/68/44/5efe9e98ad83ef5b742ce62a15bea609ed5a0d1caf35b79257ddb324031a/redis-2.10.5.tar.gz"; sha256 = "5dfbae6acfc54edf0a7a415b99e0b21c0a3c27a7f787b292eea727b1facc5533"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "Python client for Redis key-value store";
    };
  };



  "requests" = python.mkDerivation {
    name = "requests-2.13.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/16/09/37b69de7c924d318e51ece1c4ceb679bf93be9d05973bb30c35babd596e2/requests-2.13.0.tar.gz"; sha256 = "5722cd09762faa01276230270ff16af7acf7c5c45d623868d9ba116f15791ce8"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."idna"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.asl20;
      description = "Python HTTP for Humans.";
    };
  };



  "requests-file" = python.mkDerivation {
    name = "requests-file-1.4.1";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/d4/6a/3503eaf7b8c8b85fc07485234d914fd264b5e81bbb0c6bdf591ccb09972b/requests-file-1.4.1.tar.gz"; sha256 = "d75823cccd271caa7303304f9f7d44e12db9f77d844491c5ec9bd44af0844ebc"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."requests"
      self."six"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
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
      homepage = "";
      license = licenses.bsdOriginal;
      description = "RQ is a simple, lightweight, library for creating background jobs, and processing them.";
    };
  };



  "six" = python.mkDerivation {
    name = "six-1.10.0";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/b3/b2/238e2590826bfdd113244a40d9d3eb26918bd798fc187e2360a8367068db/six-1.10.0.tar.gz"; sha256 = "105f8d68616f8248e24bf0e9372ef04d3cc10104f1980f54d57b2ce73a5ad56a"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "Python 2 and 3 compatibility utilities";
    };
  };



  "tldextract" = python.mkDerivation {
    name = "tldextract-2.0.2";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/44/db/ab27d3003968f766bff7bde238de418d2b8ddd727c3e56346ffd3ef05e27/tldextract-2.0.2.tar.gz"; sha256 = "3d6050d48803eef7a3e3a92b840f46477761d4423fe90f68e57b420fec7f19ab"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [
      self."idna"
      self."requests"
      self."requests-file"
    ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.bsdOriginal;
      description = "Accurately separate the TLD from the registered domain andsubdomains of a URL, using the Public Suffix List.";
    };
  };

}