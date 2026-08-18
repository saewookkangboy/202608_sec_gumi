---
name: mcp-smoke-test
description: Verify this repository's local stdio MCP server through initialize, tools/list, safe tools/call, error handling, and approval-gated writes.
---

# MCP Smoke Test

Run `npm test` and `npm run smoke`.

Confirm:

- the server advertises exactly three intended tools;
- `get_equipment_errors` returns counts and evidence IDs;
- reversed dates return a structured error without stopping the server;
- a missing approval token produces dry-run output and no file;
- the raw CSV remains unchanged.

Report the failing method and expected corrective action.

