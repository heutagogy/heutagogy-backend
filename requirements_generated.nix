# generated using pypi2nix tool (version: 1.6.0)
#
# COMMAND:
#   pypi2nix -V 3.5 -r requirements.txt -E libffi
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



  "Jinja2" = python.mkDerivation {
    name = "Jinja2-2.9.4";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/f4/3f/28387a5bbc6883082c16784c6135440b94f9d5938fb156ff579798e18eda/Jinja2-2.9.4.tar.gz"; sha256 = "aab8d8ca9f45624f1e77f2844bf3c144d180e97da8824c2a6d7552ad039b5442"; };
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



  "SQLAlchemy" = python.mkDerivation {
    name = "SQLAlchemy-1.1.4";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/ca/ca/c2436fdb7bb75d772d9fa17ba60c4cfded6284eed053a7274b2beb96596a/SQLAlchemy-1.1.4.tar.gz"; sha256 = "701b57d628b9fa1cfb82f10665e7214d5d2db23251ca6f23b91c5f56fcdbdeb5"; };
    doCheck = commonDoCheck;
    buildInputs = commonBuildInputs;
    propagatedBuildInputs = [ ];
    meta = with pkgs.stdenv.lib; {
      homepage = "";
      license = licenses.mit;
      description = "Database Abstraction Library";
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
    name = "bcrypt-3.1.2";
    src = pkgs.fetchurl { url = "https://pypi.python.org/packages/4e/af/d276cf4ea4ea5ff1f1ee6382e5fd4193b18b834b206dd73ba6b5b0289a15/bcrypt-3.1.2.tar.gz"; sha256 = "346e175c820a111c17d4c2def181a96e1826652edb0bb16e565085ed542785aa"; };
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

}