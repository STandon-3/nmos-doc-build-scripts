import os
import common


def render_docs(dir):
    """Renders the source docs/ into destination tree dir/docs"""
    if os.path.isdir(common.SRC_DIR + "/docs"):
        print(f"Rendering docs into {dir}/docs...")
        os.mkdir(dir + "/docs")


def render_apis(dir):
    """Renders the source APIs/ into destination tree dir/APIs"""
    if os.path.isdir(common.SRC_DIR + "/APIs"):
        print(f"Rendering APIs into {dir}/APIs...")
        os.mkdir(dir + "/APIs")


def render_examples(dir):
    """Renders the sourceexamples/ into destination tree dir/examples"""
    if os.path.isdir(common.SRC_DIR + "/examples"):
        print(f"Rendering examples into {dir}/examples...")
        os.mkdir(dir + "/examples")
