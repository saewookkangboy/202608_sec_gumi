import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const errors = JSON.parse(fs.readFileSync(path.join(ROOT, "fixtures/equipment_errors.json"), "utf8"));
const quality = JSON.parse(fs.readFileSync(path.join(ROOT, "fixtures/quality_summary.json"), "utf8"));

export function plan() {
  return {
    state: "PLANNED",
    goal: "오류 급증 설비의 품질 영향과 점검 우선순위를 근거와 함께 제안한다.",
    steps: ["오류 Top 3 확인", "설비 ID로 품질 데이터 조인", "불량률 계산", "근거 검증", "사람 승인"],
    acceptance: ["모든 추천에 로그와 품질 evidence ID가 있음", "불량률 계산이 일치함", "승인 전 최종 확정 없음"]
  };
}

export function execute({ fault = null } = {}) {
  const rows = errors.map((item, index) => {
    const lookupId = fault === "bad-join" && index === 0 ? "PRESS-99" : item.equipment_id;
    const q = quality.find((row) => row.equipment_id === lookupId);
    const rate = q ? Number(((q.defects / q.inspected) * 100).toFixed(2)) : null;
    return {
      rank: index + 1,
      equipment_id: item.equipment_id,
      error_count: item.error_count,
      top_error: item.top_error,
      defect_rate_pct: fault === "bad-rate" && index === 0 ? 99 : rate,
      log_evidence_ids: fault === "missing-evidence" && index === 0 ? [] : item.evidence_ids,
      quality_evidence_id: q?.evidence_id ?? null
    };
  });
  return { state: "EXECUTED", rows };
}

export function verify(evidence) {
  const reasons = [];
  for (const row of evidence.rows) {
    if (!row.log_evidence_ids?.length) reasons.push(`${row.equipment_id}: 로그 근거 없음`);
    if (!row.quality_evidence_id) reasons.push(`${row.equipment_id}: 품질 조인 실패`);
    const q = quality.find((item) => item.equipment_id === row.equipment_id);
    const expected = q ? Number(((q.defects / q.inspected) * 100).toFixed(2)) : null;
    if (expected !== row.defect_rate_pct) reasons.push(`${row.equipment_id}: 불량률 계산 불일치`);
  }
  return reasons.length ? { state: "REJECTED", verdict: "REJECT", reasons } : { state: "VERIFIED", verdict: "PASS", reasons: [] };
}

export function runPipeline({ fault = null, persistentFault = false, approve = false, maxRetries = 3 } = {}) {
  const events = [];
  const add = (state, detail) => events.push({ sequence: events.length + 1, state, detail });
  const planResult = plan();
  add("PLANNED", "조사 계획과 완료 기준 생성");
  let evidence;
  let verification;
  for (let attempt = 1; attempt <= maxRetries; attempt += 1) {
    const activeFault = attempt === 1 || persistentFault ? fault : null;
    evidence = execute({ fault: activeFault });
    add("EXECUTED", `실행 시도 ${attempt}`);
    verification = verify(evidence);
    add(verification.state, verification.reasons.join("; ") || "검증 통과");
    if (verification.verdict === "PASS") break;
  }
  if (verification.verdict !== "PASS") {
    add("ESCALATED", `${maxRetries}회 반려 후 사람에게 이관`);
    return { state: "ESCALATED", plan: planResult, evidence, verification: { ...verification, verdict: "ESCALATE" }, approval: null, events };
  }
  const approval = {
    state: approve ? "APPROVED" : "AWAITING_APPROVAL",
    decision: approve ? "APPROVE" : null,
    summary: evidence.rows,
    verification: verification.verdict,
    uncertainty: "합성 데이터 기반 교육 결과이며 실제 정비 지시가 아님"
  };
  add("AWAITING_APPROVAL", "정비 우선순위 확정 전 사람 승인 요청");
  if (approve) add("APPROVED", "명시적 승인 후 최종 확정");
  return { state: approval.state, plan: planResult, evidence, verification, approval, events };
}

