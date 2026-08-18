import fs from "node:fs";
import path from "node:path";
import { runPipeline } from "./pipeline.mjs";

const args = process.argv.slice(2);
const valueAfter = (name) => {
  const index = args.indexOf(name);
  return index >= 0 ? args[index + 1] : null;
};
const result = runPipeline({
  fault: valueAfter("--fault"),
  persistentFault: args.includes("--persistent-fault"),
  approve: args.includes("--approve")
});
const runId = `run-${Date.now()}`;
const dir = path.join("runs", runId);
fs.mkdirSync(dir, { recursive: true });
for (const key of ["plan", "evidence", "verification", "approval"]) {
  if (result[key] != null) fs.writeFileSync(path.join(dir, `${key}.json`), JSON.stringify(result[key], null, 2) + "\n");
}
fs.writeFileSync(path.join(dir, "events.jsonl"), result.events.map((e) => JSON.stringify(e)).join("\n") + "\n");
console.log(JSON.stringify({ runId, state: result.state, eventCount: result.events.length }, null, 2));

