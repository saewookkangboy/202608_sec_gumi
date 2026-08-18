import readline from "node:readline";
import { getEquipmentErrors, listEquipmentLogs, writeAnalysisReport } from "./domain.mjs";

const protocolVersion = "2025-06-18";

const tools = [
  {
    name: "list_equipment_logs",
    description: "List synthetic equipment log counts for a date range.",
    inputSchema: { type: "object", properties: { startDate: { type: "string" }, endDate: { type: "string" } }, required: ["startDate", "endDate"] }
  },
  {
    name: "get_equipment_errors",
    description: "Count error codes and return evidence rows for one equipment ID.",
    inputSchema: { type: "object", properties: { equipmentId: { type: "string" }, startDate: { type: "string" }, endDate: { type: "string" } }, required: ["equipmentId", "startDate", "endDate"] }
  },
  {
    name: "write_analysis_report",
    description: "Write a Markdown report only when approvalToken is APPROVE_WRITE; otherwise return a dry-run preview.",
    inputSchema: { type: "object", properties: { title: { type: "string" }, body: { type: "string" }, approvalToken: { type: "string" } }, required: ["title", "body"] }
  }
];

function result(id, payload) {
  process.stdout.write(JSON.stringify({ jsonrpc: "2.0", id, result: payload }) + "\n");
}

function failure(id, message) {
  process.stdout.write(JSON.stringify({ jsonrpc: "2.0", id, error: { code: -32602, message } }) + "\n");
}

function callTool(name, args) {
  if (name === "list_equipment_logs") return listEquipmentLogs(args);
  if (name === "get_equipment_errors") return getEquipmentErrors(args);
  if (name === "write_analysis_report") return writeAnalysisReport(args);
  throw new Error(`unknown tool: ${name}`);
}

const rl = readline.createInterface({ input: process.stdin, crlfDelay: Infinity });
rl.on("line", (line) => {
  let message;
  try { message = JSON.parse(line); } catch { return; }
  try {
    if (message.method === "initialize") {
      result(message.id, { protocolVersion, capabilities: { tools: {} }, serverInfo: { name: "equipment-log-mcp", version: "1.0.0" } });
    } else if (message.method === "tools/list") {
      result(message.id, { tools });
    } else if (message.method === "tools/call") {
      const value = callTool(message.params?.name, message.params?.arguments ?? {});
      result(message.id, { content: [{ type: "text", text: JSON.stringify(value, null, 2) }], isError: false });
    } else if (message.id !== undefined) {
      failure(message.id, `unsupported method: ${message.method}`);
    }
  } catch (error) {
    failure(message.id, error.message);
  }
});
console.error("equipment-log-mcp ready on stdio");

