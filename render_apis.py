import os
from common import SRC_DIR


def render_apis(dir):
    """Renders the source APIs/ into destination tree dir/APIs"""
    if os.path.isdir(SRC_DIR + "/APIs"):
        print(f"Rendering APIs into {dir}/APIs...")
        os.mkdir(dir + "/APIs")
