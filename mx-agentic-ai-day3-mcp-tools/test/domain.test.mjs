import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import { getEquipmentErrors, listEquipmentLogs, writeAnalysisReport } from "../src/domain.mjs";

test("lists records by equipment", () => {
  const result = listEquipmentLogs({ startDate: "2026-08-11", endDate: "2026-08-17" });
  assert.equal(result.total, 15);
  assert.ok(result.byEquipment["PRESS-01"] > 0);
});

test("returns counts and evidence", () => {
  const result = getEquipmentErrors({ equipmentId: "PRESS-01", startDate: "2026-08-11", endDate: "2026-08-17" });
  assert.equal(result.counts["ERR-204"], 4);
  assert.equal(result.evidence.length, 5);
});

test("rejects reversed dates", () => {
  assert.throws(() => listEquipmentLogs({ startDate: "2026-08-17", endDate: "2026-08-11" }));
});

test("write requires approval token", () => {
  const result = writeAnalysisReport({ title: "테스트", body: "내용" });
  assert.equal(result.status, "dry-run");
  assert.equal(fs.existsSync("outputs/analysis-report.md"), false);
});

