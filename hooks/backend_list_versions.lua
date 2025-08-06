local cache = {}
local cache_ttl = 12 * 60 * 60

function PLUGIN:BackendListVersions(ctx)
  local tool = ctx.tool
  local tool_cache = cache[tool]
  local now = os.time()

  if tool_cache and tool_cache.versions and tool_cache.timestamp and (now - tool_cache.timestamp) < cache_ttl then
    return tool_cache.versions
  end

  local cmd = require("cmd")
  local json = require("json")

  local list_cmd = "python3 " .. RUNTIME.pluginDirPath .. "/lib/lib.py list " .. tool
  local result = cmd.exec(list_cmd)
  local versions = json.decode(result)

  cache[tool] = {
    versions = versions,
    timestamp = now,
  }

  return { versions = versions }
end
