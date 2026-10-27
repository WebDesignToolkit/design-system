# WebDesignToolkit Agency UI Library — v0.1
An original, brand-neutral HTML/CSS collection of components, blocks, full-width sections, page templates, and design-token themes. This is a **draft demonstration cohort**; do not describe it as production-certified.

## Inventory
- 5 components, 3 composable blocks, 4 sections, 2 full-page templates, and 3 themes = **17** registry entries.
- Canonical IDs `WDT-COMP-`, `WDT-BLOCK-`, `WDT-SEC-`, `WDT-TPL-`, and `WDT-THEME-` never change after acceptance.
- `library/registry.json` is the canonical machine-readable manifest. Each entry has `status: draft-demo` and `verified: false`.
- `library/styles/library.css` contains namespace-scoped tokens and styles; no external font, icon library, JS framework or build required.
- `library/templates/*.html` are **complete** HTML pages with placeholders marked clearly.
- The separate `WebDesignToolkit/website` repository will host the public interactive preview; publication requires reviewed sync from this registry.

## Reusing an item
1. Copy an entry's `html` from registry or from the demo's **Copy HTML** button.
2. Include `library/styles/library.css` and wrap the section in `<div data-wd-theme="hardline">…</div>` (or use the theme attribute on `html`).
3. For a full-page template, copy its HTML and stylesheet, then replace sample copy, example URLs and contact information.
4. Test in your client environment; passing a demo does not establish WCAG compliance.

## Themes
`hardline` (sharp/tactile), `studio` (cool/professional) and `calm` (warm/editorial). Themes override semantic variables only. The hardline reference style remains the default.

## Quality contract
- Semantic HTML, visible focus, native keyboard disclosures, meaningful labels, responsive intrinsic grids and reduced motion.
- No fabricated customer reviews, results, real logos, or business performance metrics.
- No tracking, remote JS, background GitHub Actions, third-party downloads or copying of Sabpuja branded assets.
- Registry is for **our UI artifacts**, separate from `WebDesignToolkit/catalog` of external open-source projects.
See [quality](./docs/QUALITY.md) and [provenance](./docs/PROVENANCE.md).

## Agency Component Foundry v0.2

Nine families, 27 new variants, 44 total draft library entries. See [Foundry contract](./docs/FOUNDRY.md), [canonical registry](./registry.json), and optional booking-demo-only [local interactions](./scripts/interactions.js). No fabricated product reviews, price claims, or real appointment submissions.
