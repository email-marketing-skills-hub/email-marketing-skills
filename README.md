# Email Marketing Skills

![Email marketing skills illustration: an agent sorts requests into campaigns, popups, automations, and segments.](assets/email-marketing-skills-hero.svg)

**20 focused AI-agent skills for email marketing and audience growth, brought together by [Poptin](https://www.poptin.com/).**

Plan campaigns, write copy, design automations, define segments, improve signup experiences, and review deliverability. Choose a general workflow or an industry specialist. Install only what you need, or install the full collection.

Each skill lives in its own `skills/<skill-name>/` directory with its own `SKILL.md` and supporting files. There is no combined mega-skill and no dependency on installing the other skills.

If this collection helps your work, star this repository so more marketers can find it.

## Install

Use the [Skills CLI](https://github.com/vercel-labs/skills) with Node.js 22.20 or later. Run commands from the project where you want the skills installed.


List the available skills without installing:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --list
```

Install one skill:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --skill ecommerce-email-marketing-specialist
```

Select multiple skills:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --skill email-campaign-specialist --skill email-segmentation-specialist
```

Install all 20 skills and choose your agent in the installer:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --skill '*'
```

Target one agent explicitly, for example Codex:

```bash
npx skills add email-marketing-skills-hub/email-marketing-skills --skill email-campaign-specialist -a codex
npx skills add email-marketing-skills-hub/email-marketing-skills --skill '*' -a codex
```

Installation is project-scoped by default. Add `-g` only if you want user-wide installation. The CLI's `--all` option targets all agents as well as all skills; `--skill '*'` lets you choose the target agent instead. See the [official installation reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add) for supported agents and options. These are portable instruction files; installation support does not guarantee identical behavior in every agent or provide access to marketing platforms.

### Manual installation

Copy the entire directory for a selected skill, including its references and examples, into the skill location documented by your agent. Do not copy `SKILL.md` alone. Keep the original directory name. You can also read a skill directly without installing it.

## Choose your skill

### Core workflows

| Skill | Use it for |
| --- | --- |
| [email-campaign-specialist](skills/email-campaign-specialist/SKILL.md) | Plan and draft newsletters, promotions, campaign briefs, and measurement plans. |
| [email-automation-specialist](skills/email-automation-specialist/SKILL.md) | Design lifecycle workflows with entry criteria, exclusions, exits, and QA. |
| [email-segmentation-specialist](skills/email-segmentation-specialist/SKILL.md) | Define actionable audiences, Boolean rules, exclusions, and overlap handling. |
| [email-deliverability-specialist](skills/email-deliverability-specialist/SKILL.md) | Audit permission-based sending, authentication, reputation, and inbox placement. |
| [lead-generation-popup-specialist](skills/lead-generation-popup-specialist/SKILL.md) | Plan signup popups and forms, offers, targeting, consent, and experiments. |

### Industry specialists

| Skill | Use it for |
| --- | --- |
| [automotive-email-marketing-specialist](skills/automotive-email-marketing-specialist/SKILL.md) | Support automotive inquiries, service reminders, and customer retention. |
| [ecommerce-email-marketing-specialist](skills/ecommerce-email-marketing-specialist/SKILL.md) | Grow store subscribers and improve cart recovery, retention, and email revenue. |
| [education-email-marketing-specialist](skills/education-email-marketing-specialist/SKILL.md) | Plan education inquiry, enrollment, and learner communications. |
| [events-email-marketing-specialist](skills/events-email-marketing-specialist/SKILL.md) | Plan event promotion, registrations, reminders, and follow-up. |
| [financial-services-marketing-specialist](skills/financial-services-marketing-specialist/SKILL.md) | Prepare financial-services marketing with careful claims and review gates. |
| [fitness-email-marketing-specialist](skills/fitness-email-marketing-specialist/SKILL.md) | Support fitness trials, member onboarding, engagement, and retention. |
| [food-restaurants-email-marketing-specialist](skills/food-restaurants-email-marketing-specialist/SKILL.md) | Plan restaurant and food-business subscriber growth and repeat visits. |
| [healthcare-marketing-specialist](skills/healthcare-marketing-specialist/SKILL.md) | Prepare healthcare marketing with privacy and sensitive-data safeguards. |
| [hr-recruitment-marketing-specialist](skills/hr-recruitment-marketing-specialist/SKILL.md) | Plan employer, recruiting, and candidate engagement communications. |
| [nonprofit-engagement-specialist](skills/nonprofit-engagement-specialist/SKILL.md) | Plan donor, volunteer, and supporter engagement. |
| [publisher-audience-growth-specialist](skills/publisher-audience-growth-specialist/SKILL.md) | Grow and engage publisher and newsletter audiences. |
| [real-estate-marketing-specialist](skills/real-estate-marketing-specialist/SKILL.md) | Plan property inquiry and real-estate audience nurture. |
| [saas-email-marketing-specialist](skills/saas-email-marketing-specialist/SKILL.md) | Support trial activation, onboarding, product adoption, and retention. |
| [security-services-marketing-specialist](skills/security-services-marketing-specialist/SKILL.md) | Prepare security-services marketing with confidentiality safeguards. |
| [travel-marketing-specialist](skills/travel-marketing-specialist/SKILL.md) | Plan travel inquiries, booking nurture, and repeat-traveler engagement. |

## Example requests

- “Use email-campaign-specialist to draft a launch email from this approved brief. Flag any missing facts.”
- “Use email-automation-specialist to design a welcome flow with consent checks, exit rules, and a QA plan.”
- “Use ecommerce-email-marketing-specialist to audit these cart-recovery emails without inventing discounts.”
- “Use email-segmentation-specialist to define engaged subscribers and avoid overlapping sends.”

Supply your business, audience, objective, platform, approved offer, and available evidence when relevant. Start with one skill closest to the task; add another only when it helps.

## Scope and safety

These skills provide planning, drafting, analysis, and implementation guidance. They do not grant account access or permission to send campaigns, change settings, publish content, or make commitments. Review facts, consent, exclusions, claims, and launch readiness before taking action. Regulated-industry content requires appropriate professional review; it is not legal, medical, or financial advice.

## About Poptin

[Poptin](https://www.poptin.com/) provides tools for website lead capture and email marketing. The collection includes relevant Poptin context while keeping each skill's main workflow usable with the user's chosen stack. A Poptin account is not required to read or use these instructions.

## Provenance and maintenance

This collection preserves the 20 standalone skills from [Email Marketing Skills Hub](https://github.com/email-marketing-skills-hub). All 88 source files were copied without content changes, preserving their relative references, examples, and existing test materials. The original repositories are unchanged.

[sources.json](sources.json) records the source repository, snapshot tree SHA, and Git blob SHA for every file. This snapshot was verified on November 4, 2026. To validate the local collection:

```bash
python -m pip install PyYAML
python scripts/validate_collection.py
```

The validator checks unique names, frontmatter, required descriptions, local Markdown references, file inventories, and original-content hashes. These structural checks are not a substitute for testing skill behavior in your agent. See [VALIDATION.md](VALIDATION.md) for the exact validation scope and limitations.

## Licensing

This collection is licensed under the [MIT License](LICENSE).

Copyright (c) 2026 Poptin LTD.
