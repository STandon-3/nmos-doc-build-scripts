#!/usr/bin/env python3

import yaml
from git import Repo

with open(r'_config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

repo_address = Repo().remotes.origin.url

print(f"Cloning {repo_address} as source-repo")

Repo.clone_from(repo_address, 'source-repo', multi_options=['--no-checkout'])
