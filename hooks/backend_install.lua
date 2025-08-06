function PLUGIN:BackendInstall(ctx)
  local tool = ctx.tool
  local version = ctx.version
  local install_path = ctx.install_path

  local cmd = require("cmd")

  local install_cmd = "python3 "
    .. RUNTIME.pluginDirPath
    .. "/lib/lib.py install "
    .. tool
    .. " "
    .. version
    .. " "
    .. install_path
  local _ = cmd.exec(install_cmd)

  return {}
end
