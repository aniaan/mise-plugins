import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="fzf",
    cmd="fzf",
    repo_name="junegunn/fzf",
    filename_template="fzf-{normalize_version}-{platform}_{arch}.tar.gz",
    platform_map={
        "darwin": "darwin",
        "linux": "linux",
    },
    arch_map={
        "x86_64": "amd64",
        "aarch64": "arm64",
    },
    checksum_filename_template="fzf_{normalize_version}_checksums.txt",
    bin_path="fzf",
    recover_raw_version=lambda x: f"v{x}",
)
