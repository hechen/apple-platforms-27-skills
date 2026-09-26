# Working on this repository

This repository publishes portable Agent Skills for Apple platform development.

- Read CONTRIBUTING.md before editing skills or packaging.
- Keep one canonical copy of each skill under skills/. Avoid per-agent forks of the instructions.
- Preserve relative sibling links; installation instructions should install the complete set.
- Use Apple primary documentation and the selected public SDK for technical claims. Record the date and version of changing behavior.
- Keep agents/openai.yaml optional; core instructions must remain useful without it.
- Run scripts/validate.py and the repository unit tests for packaging changes. Run scripts/check-sdk.sh on a compatible Mac when changing probe-covered Swift APIs.
- Do not label installer smoke checks as end-to-end agent or application tests.
- iPhone Duo guidance lives in hechen/iphone-duo-skills. Route Duo work there by skill name and repository URL; do not add Duo skills or Duo API probes here.
