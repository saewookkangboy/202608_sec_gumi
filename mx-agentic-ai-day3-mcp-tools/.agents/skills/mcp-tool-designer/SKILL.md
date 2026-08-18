---
name: mcp-tool-designer
description: Design or revise the local equipment-log MCP tool contracts with narrow permissions, explicit schemas, and testable errors before changing server code.
---

# MCP Tool Designer

Use this skill before adding or changing a tool in `src/server.mjs`.

## Contract

1. Define one clear job, required inputs, output evidence, and failure cases.
2. Keep read tools separate from write tools.
3. Restrict writes to `outputs/` and require an explicit approval token.
4. Add domain tests and a smoke-test assertion for observable behavior.
5. Preserve stdout for JSON-RPC; send diagnostics to stderr.

Do not add credentials or live business data to this training repository.

