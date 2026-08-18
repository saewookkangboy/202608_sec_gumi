---
name: request-human-approval
description: Assemble a human-approval packet after verification passes and block final prioritization until an explicit approve, reject, or revise decision is provided.
---

# Request Human Approval

Include the recommendation, evidence summary, verifier result, and remaining uncertainty.

Keep the run in `AWAITING_APPROVAL` until an explicit decision is received. Do not treat silence, prior approval, or verifier PASS as human approval.

기술 배경(HITL 승인 게이트, 승인 패킷)은 [skill·기술 참고 자료](../../../docs/skill-and-tech-reference.md)를 참고한다.

