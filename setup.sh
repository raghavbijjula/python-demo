#!/bin/bash
# =========== Setup Git Hooks ==========
curl https://pre-commit.com/install-local.py | python3 -
curl --silent  https://raw.githubusercontent.com/thoughtworks/talisman/master/global_install_scripts/install.bash | bash

ln -sf "$(PWD)/hooks/pre-commit" .git/hooks/pre-commit
