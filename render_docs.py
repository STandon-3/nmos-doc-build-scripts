import os
import shutil

from common import SRC_DIR


def render_docs(dir):
    """Renders the source docs/ into destination tree dir/docs"""
    if os.path.isdir(SRC_DIR + "/docs"):
        print(f"Copying docs into {dir}/docs...")
        # os.mkdir(dir + "/docs")
        # for file in glob.glob(SRC_DIR + "/docs/[1-9]*.md"):
        #     shutil.copy(file, dir + "/docs/")
        # if os.path.isdir(SRC_DIR + "/docs/images"):
        #     print(f"Copying images into {dir}/docs/images...")
        #     os.mkdir(dir + "/docs/images")
        #     for file in glob.glob(SRC_DIR + "/docs/images/*"):
        #         shutil.copy(file, dir + "/docs/images/")
        shutil.copytree(SRC_DIR + '/docs', dir + '/docs')
