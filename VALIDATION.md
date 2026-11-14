# Validation

Original snapshot validated on November 4, 2026. Collection addition validated on November 14, 2026.

## Passed

- All 20 public standalone repositories returned complete, non-truncated default-branch Git trees through the GitHub connector.
- All 88 files in those trees are present in `skills/<skill-name>/`.
- Every copied file matches its source Git blob SHA exactly. No skill instruction, supporting reference, example, or existing test file was rewritten.
- All 20 `SKILL.md` files have parseable YAML frontmatter, a valid lowercase hyphenated name matching their directory, and a nonempty description within the Agent Skills length limits.
- No duplicate skill names, duplicate skill files, or identical supporting files were found.
- All 69 local Markdown file references resolve inside the individual skill's own directory. No skill requires another skill's directory to resolve its linked files.
- No root `SKILL.md` shadows the individual skills.
- The `skills/<name>/SKILL.md` layout and the documented named-selection, list, and all-skills flags match the official Skills CLI documentation reviewed on the validation date.

Run `python scripts/validate_collection.py` to repeat the structural and content-preservation checks. It requires PyYAML. `sources.json` is the captured source inventory; this offline check does not poll GitHub for subsequent upstream changes.

## Not verified

- Actual CLI listing and single/all-skill installation have not been executed. The official `skills` npm package was not installed or cached in the build environment. An offline CLI probe returned `ENOTCACHED`; no substitute installer was used and no external agent installation was changed.
- The public repository tree was verified after publication: all 92 files match the validated local content hashes. Remote CLI installation remains untested in this environment.
- These checks do not certify marketing outcomes, external links, every agent's runtime behavior, or legal compliance. Existing skill-local test materials were preserved, not represented as newly executed evaluations.

## Suggested post-publication smoke test

In a disposable project, with the official Skills CLI installed and telemetry disabled if desired:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --list
npx skills add email-marketing-skills-hub/email-marketing-skills --skill email-campaign-specialist -a codex --copy -y
```

Confirm exactly one skill and its references are installed. In a second disposable project, test the complete set:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --skill '*' -a codex --copy -y
```

Confirm that all 21 uniquely named skills and their supporting files are installed. Do not run smoke tests against an existing project's skill installation without checking for name collisions first.

## Documentation sources

- [Skills CLI installation flags](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)
- [Skill structure and discovery](https://github.com/vercel-labs/skills/blob/main/docs/creating-skills.md)
- [Skills CLI requirements](https://github.com/vercel-labs/skills/blob/main/README.md)

## November 14 collection addition

- Added `poptin-mcp-email-campaigns` with two supporting references.
- Original 20-skill / 88-file snapshot and all original Git blob hashes remain unchanged.
- Validator now checks the original snapshot plus explicitly recorded `collection_additions`; it still enforces the original snapshot count and all content hashes.
- Structural validation covers 21 skills / 91 skill files. Mock scenario expectations cover draft-only execution, supported/unsupported HTML, eligible versus matching audience counts, send/schedule confirmation, changed audiences, ambiguous times, uncertain sends, human edits and missing capabilities.
- Official public MCP guide reviewed November 14. The guide confirms gallery/saved templates, segments, draft/send/schedule, but does not document exact tool schemas or HTML import. Runtime discovery and an explicit HTML fallback prevent unsupported capability claims.
- No Poptin account was connected, campaign created, audience changed, test email sent, campaign launched or scheduled during this documentation update. End-to-end MCP execution and delivery remain untested.
