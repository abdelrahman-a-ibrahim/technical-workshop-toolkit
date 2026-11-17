# Operations plan

Status: design only. No resources are provisioned by this scaffold.

## Local path
The only runnable command currently supplied is `python3 tools/check_foundation.py`. Interfaces are unimplemented; the synthetic fixture requires no account or network. Choose runtime versions and pin dependencies when implementation begins.

## Cloud / external adapter gate
Before introducing live services, fill in:
- Dedicated sandbox account/project and intended identity:
- Region and resource inventory:
- Per-resource expected hourly/request/storage cost:
- Total planned experiment allowance and how usage is checked:
- Maximum experiment duration:
- Permission boundaries and short-lived authentication approach:
- Third-party model/provider usage limits, if used:
- Creation, verification and teardown commands:
- Retained state, backups, artifacts and their retention:
- How residual billable resources will be checked:

Do not assume a trial or free tier is available. Alerts do not stop spending. The initial repository contains no cloud deploy or destructive cleanup script.

## Implementation runbook to write
Document setup, normal operation, health signals, common failures, recovery, backup/restore where relevant, credential rotation and complete decommission. Distinguish automatic recovery from operator action.

## Incident exercise
Use the failure-lab template. Record the difference between a failed experiment, a service incident and an instrumentation problem.
