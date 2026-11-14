# Flaky test

Procedure for a test whose outcome changes between runs of unchanged code. The Flaky anti-pattern in [SKILL.md](../SKILL.md) prevents one while writing a test; this reference decides what an observed one means and when it is closed. A flaky failure is a real failure whose trigger is not known yet. Its cause sits in the test or in the product, and a rerun cannot tell which.

## Keep the failure

Before rerunning, keep the failing output, the command, and what else was running on the machine. The check counts as failed until its mechanism is named.

## Name the mechanism

Read the failing assertion and list the uncontrolled inputs it depends on, starting from the anti-pattern's list. Reproduce by amplifying one input at a time instead of rerunning unchanged: repeat the test, run it alone, run it beside the work that was running when it failed, add CPU or disk load, enable the toolchain's race detector, reorder or reseed. Load `principle-fix-root-causes` for the causal trace and consume the root cause it reaches.

Completion: one sentence states the interleaving or input under which unchanged code fails, backed by a run that fails on demand or at a measured rate. "Load" or "timing" without the interleaving is not a mechanism. If no amplification reproduces the failure, report it as unexplained with the kept evidence.

## Find the owner

- **Product**: the interleaving can occur outside the test, such as a race, a lost update, or a partial read. The test was right. Treat it as a bug that already has its reproduction.
- **Test**: the test assumes an order, duration, uniqueness, or resource the product does not promise. Repair it with the anti-pattern's remedies.

Suspect the product until the trace places the assumption in the test.

## Scope

Fix a test the current change wrote or modified, or a product path it touched, before its checks count. For any other owner, report the mechanism, the kept failure, and the reproduction command as a separate defect, then continue. "Pre-existing" settles who decides on the fix; it does not turn the failure into a pass.

## Close

The repair removes the uncontrolled input. A retry, a longer sleep, a skip, or a tolerance that no longer separates correct from regressed behavior leaves it in place. Delete the test only through the candidate evidence and retention bar in [audit.md](audit.md). When controlling the input would need a test-only seam, keep the seam out and report the behavior as proven only by the amplified run.

Proof, both required:

- the amplified run that failed is green under the same conditions and count;
- one deliberate mutation of the guarded behavior turns the repaired test red, then is reverted.
