{ pkgs, python }:

self: super: {
  lxml = python.overrideDerivation super.lxml (old: {
    propagatedNativeBuildInputs = [ ];
  });
}
