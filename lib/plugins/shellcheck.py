
import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="shellcheck",
    cmd="shellcheck",
    repo_name="koalaman/shellcheck",
    filename_template="shellcheck-{version}.{platform}.{arch}.tar.xz",
    bin_path="shellcheck-{version}/shellcheck",
    recover_raw_version=lambda x: f"v{x}",
)
