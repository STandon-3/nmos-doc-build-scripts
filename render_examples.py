import os
import common


def render_examples(dir):
    """Renders the sourceexamples/ into destination tree dir/examples"""
    if os.path.isdir(common.SRC_DIR + "/examples"):
        print(f"Rendering examples into {dir}/examples...")
        os.mkdir(dir + "/examples")
