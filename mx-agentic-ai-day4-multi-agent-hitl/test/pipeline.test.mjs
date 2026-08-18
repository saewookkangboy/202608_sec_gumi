import test from "node:test";
import assert from "node:assert/strict";
import { runPipeline } from "../src/pipeline.mjs";

test("clean run waits for approval", () => {
  const result = runPipeline();
  assert.equal(result.state, "AWAITING_APPROVAL");
  assert.equal(result.verification.verdict, "PASS");
});

test("explicit approval completes the run", () => {
  const result = runPipeline({ approve: true });
  assert.equal(result.state, "APPROVED");
  assert.ok(result.events.some((event) => event.state === "APPROVED"));
});

test("one injected defect is rejected then repaired", () => {
  const result = runPipeline({ fault: "missing-evidence" });
  assert.equal(result.state, "AWAITING_APPROVAL");
  assert.ok(result.events.some((event) => event.state === "REJECTED"));
});

test("persistent defect escalates after three attempts", () => {
  const result = runPipeline({ fault: "bad-join", persistentFault: true });
  assert.equal(result.state, "ESCALATED");
  assert.equal(result.events.filter((event) => event.state === "REJECTED").length, 3);
});

test("bad rate is detected", () => {
  const result = runPipeline({ fault: "bad-rate", persistentFault: true });
  assert.match(result.verification.reasons.join(" "), /불량률 계산 불일치/);
});

