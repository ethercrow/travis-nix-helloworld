{
    packageOverrides = pkgs_: with pkgs_; {
        all = with pkgs; buildEnv {
            name = "all";
            paths = [
                gnumake
            ];
        };
    };
}