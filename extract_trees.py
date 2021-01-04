#!/usr/bin/env python3

# Copyright 2021 British Broadcasting Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from git import Repo
import os
import re

from common import get_config, SRC_DIR
from render_docs import render_docs
from render_apis import render_apis
from render_examples import render_examples


def extract_tree(repo, dir, checkout):
    """Checks out a branch or tag and extracts docs, APIs, examples"""
    print(f"Extracting {checkout} into {dir}")
    if not os.path.isdir(dir):
        os.mkdir(dir)
    repo.git.checkout(checkout)
    tree = dir + '/' + checkout.name
    os.mkdir(tree)
    render_docs(tree)
    render_apis(tree)
    render_examples(tree)


config = get_config()
repo = Repo(SRC_DIR)

for branch in tuple(_ for _ in repo.branches if re.match(config['show_branches'], _.name)):
    extract_tree(repo, "branches", branch)

for tag in tuple(_ for _ in repo.tags if re.match(config['show_tags'], _.name)):
    extract_tree(repo, "tags", tag)
