import { spawn } from "node:child_process";

const child = spawn(process.execPath, ["src/server.mjs"], { stdio: ["pipe", "pipe", "pipe"] });
const pending = new Map();
let buffer = "";
child.stdout.on("data", (chunk) => {
  buffer += chunk.toString();
  const lines = buffer.split("\n");
  buffer = lines.pop();
  for (const line of lines) {
    const msg = JSON.parse(line);
    pending.get(msg.id)?.(msg);
    pending.delete(msg.id);
  }
});

function send(id, method, params = {}) {
  return new Promise((resolve) => {
    pending.set(id, resolve);
    child.stdin.write(JSON.stringify({ jsonrpc: "2.0", id, method, params }) + "\n");
  });
}

const init = await send(1, "initialize", { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "smoke", version: "1" } });
if (!init.result?.serverInfo) throw new Error("initialize failed");
const list = await send(2, "tools/list");
if (list.result?.tools?.length !== 3) throw new Error("expected three tools");
const call = await send(3, "tools/call", { name: "get_equipment_errors", arguments: { equipmentId: "PRESS-01", startDate: "2026-08-11", endDate: "2026-08-17" } });
if (!call.result?.content?.[0]?.text.includes("ERR-204")) throw new Error("tool call failed");
child.kill();
console.log("PASS: initialize, tools/list, tools/call");

