{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = with pkgs; [
    go_1_21

    go-outline
    gopls
    gopkgs
    go-tools
    goimports-reviser
    delve
  ];

  hardeningDisable = [ "all" ];
}
