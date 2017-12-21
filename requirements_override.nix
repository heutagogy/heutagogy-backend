{ pkgs, python }:

self: super: {
  lxml = python.overrideDerivation super.lxml (old: {
    # This is to avoid the next error:
    #
    # $ nix-shell --show-trace
    # error: while evaluating the attribute ‘propagatedBuildInputs’ of the derivation ‘python3.5-heutagogy-1.0’ at <nixpkgs>/pkgs/stdenv/generic/make-derivation.nix:98:11:
    # while evaluating the attribute ‘propagatedBuildInputs’ of the derivation ‘python3.5-newspaper3k-0.1.9’ at <nixpkgs>/pkgs/stdenv/generic/make-derivation.nix:98:11:
    # while evaluating the attribute ‘propagatedBuildInputs’ of the derivation ‘python3.5-beautifulsoup4-4.6.0’ at <nixpkgs>/pkgs/stdenv/generic/make-derivation.nix:98:11:
    # while evaluating the attribute ‘propagatedBuildInputs’ of the derivation ‘python3.5-python3.5-lxml-4.1.1’ at <nixpkgs>/pkgs/stdenv/generic/make-derivation.nix:98:11:
    # infinite recursion encountered, at undefined position
    propagatedBuildInputs = [ ];
  });
}
