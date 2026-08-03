# Ariadne Repository Instructions

## Fixed identity

- Use **Ariadne** as the external name.
- Use **`ariadne-skill`** as the repository name and primary installable skill name.
- Use **Lattice Kernel** as the methodology-kernel name.
- Keep every installable module in the `ariadne-*` namespace.
- Do not depend on, mirror, or modify CrossFrame, world-structure, or other skill repositories.

## Source and scope

- Treat *跨尺度多圈层结构推演框架 v8.2* as the primary methodology source.
- Treat the referenced “数学结构概述” conversation as design context, not source authority.
- Build a methodology for agent work and human thinking, not an ontology, personality taxonomy, clinical tool, truth engine, or authorization system.
- Do not copy the source DOCX into the public repository.

## Mandatory implementation sequence

Follow this order without interleaving the phases:

1. Freeze requirements and record no-skill baseline failures.
2. Build the complete content of the primary skill and every module.
3. Confirm the whole-suite content-complete gate.
4. Only then begin integrated review, validation, forward testing, and correction.

Do not review, approve, reject, polish, or forward-test modules one by one while other module content is still incomplete. Do not request user approval between modules. Automated or human review begins only after all planned skill bodies, references, metadata, contracts, evaluation prompts, and repository validators exist.

## Local and publishing boundaries

- Test local skills only by explicit name or direct repository path.
- Do not copy, link, or install this repository into a global skills directory on this workstation.
- Do not publish partial implementation branches or partial skill releases.
- Keep skill files free of iteration narration, development diary text, and version-by-version explanations.
