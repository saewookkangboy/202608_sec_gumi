import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const DATA = path.join(ROOT, "data", "equipment_logs.csv");
const OUTPUTS = path.join(ROOT, "outputs");

export function loadRows() {
  const lines = fs.readFileSync(DATA, "utf8").trim().split(/\r?\n/);
  const headers = lines.shift().split(",");
  return lines.map((line, index) => {
    const values = line.split(",");
    const row = Object.fromEntries(headers.map((key, i) => [key, values[i] ?? ""]));
    row.evidence_id = `LOG-${String(index + 1).padStart(3, "0")}`;
    return row;
  });
}

function validRange(startDate, endDate) {
  if (!/^\d{4}-\d{2}-\d{2}$/.test(startDate) || !/^\d{4}-\d{2}-\d{2}$/.test(endDate)) {
    throw new Error("dates must use YYYY-MM-DD");
  }
  if (startDate > endDate) throw new Error("startDate must be before or equal to endDate");
}

export function listEquipmentLogs({ startDate, endDate }) {
  validRange(startDate, endDate);
  const rows = loadRows().filter((r) => r.timestamp.slice(0, 10) >= startDate && r.timestamp.slice(0, 10) <= endDate);
  const byEquipment = {};
  for (const row of rows) byEquipment[row.equipment_id] = (byEquipment[row.equipment_id] ?? 0) + 1;
  return { startDate, endDate, total: rows.length, byEquipment };
}

export function getEquipmentErrors({ equipmentId, startDate, endDate }) {
  validRange(startDate, endDate);
  const rows = loadRows().filter((r) => r.equipment_id === equipmentId && r.level === "ERR" && r.timestamp.slice(0, 10) >= startDate && r.timestamp.slice(0, 10) <= endDate);
  const counts = {};
  for (const row of rows) counts[row.error_code] = (counts[row.error_code] ?? 0) + 1;
  return { equipmentId, startDate, endDate, counts, evidence: rows.map(({ evidence_id, timestamp, error_code }) => ({ evidence_id, timestamp, error_code })) };
}

export function writeAnalysisReport({ title, body, approvalToken }) {
  const preview = `# ${title}\n\n${body}\n`;
  if (approvalToken !== "APPROVE_WRITE") return { status: "dry-run", preview };
  fs.mkdirSync(OUTPUTS, { recursive: true });
  const target = path.join(OUTPUTS, "analysis-report.md");
  fs.writeFileSync(target, preview, "utf8");
  return { status: "written", path: "outputs/analysis-report.md" };
}

