import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))


from lib.lib import Plugin

PLUGIN = Plugin(
    name="biome",
    cmd="biome",
    repo_name="biomejs/biome",
    filename_template="biome-{platform}-{arch}",
    arch_map={
        "x86_64": "x64",
        "aarch64": "arm64",
    },
    bin_path="biome",
    is_compressed=False,
    recover_raw_version=lambda x: f"cli/v{x}",
    normalize_version=lambda x: x.removeprefix("cli/v"),
    release_filter=lambda x: x["tag_name"].startswith("cli/v") and x["prerelease"] is False,
)
