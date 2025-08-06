import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="taplo",
    cmd="taplo",
    repo_name="tamasfe/taplo",
    filename_template="taplo-full-{platform}-{arch}.gz",
    bin_path="taplo",
)
