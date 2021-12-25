{ pkgs ? import <nixpkgs> {}
, python3Packages ? pkgs.python3Packages
}:

with python3Packages;
buildPythonApplication {
  pname = "mb";
  version = "1.0.0";
  src = ./.;
}
