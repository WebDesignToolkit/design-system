# Agency Component Foundry v0.2 — Local QA Evidence

Date: 2026-10-27 (Asia/Kolkata)
Execution environment: authorized Neo Windows workstation, authenticated GitHub CLI, Python 3.13, Node 22, locally installed Google Chrome driven through Puppeteer. No GitHub Actions executed.

## Canonical registry and snapshot

- Source: design-system/library/registry.json.
- Entries: 44 total; 17 v0.1 preserved and 27 new v0.2.
- New families: headers, navigation, heroes, pricing, testimonials, portfolio, products, booking, landing-pages; three variants per family.
- Structural validation: PASS. Unique stable IDs, documented props on all new records, correctly associated form labels, local example URLs, demo-only status.
- Canonical source and website snapshot: byte-for-byte match across registry, shared CSS, optional no-send JS, and five page templates (8/8 paths).

## Actual Chrome browser execution

Test driver: website/library/tests/browser.cjs.
Local static HTTP server and headless Chrome, no external accounts or third-party pages interacted with.

**Result: PASS — 28 assertions, zero page errors.**

Coverage includes:
- Gallery loads with 44 entries at 360px, 768px, 1280px; zero document-level horizontal overflow at these widths.
- Header family filtering and direct canonical ID selection.
- Native responsive details navigation opens at mobile width.
- Theme switching and viewport presets function.
- Booking family filter and required field validation. The form prevents submission and explicitly displays that no booking was made or data sent.
- Editable props inspector contains per-item contracts.
- SaaS, local business, and commerce complete HTML templates serve successfully, contain semantic main, and reflow at 360px.
- Reduced-motion feature emulation recognized by the browser.
- Every one of the 44 preview entries renders at 360px with source markup and no page-level horizontal overflow.
- Approximate 200% browser zoom/reflow using CSS zoom; keyboard Tab reaches the family selector from search input.
- Zero uncaught browser page errors.

## Deliberately not claimed

- Not a WCAG certification, Lighthouse performance benchmark, full screen-reader audit or production deployment test.
- Theme/text contrast not individually audited for every combination.
- Zoom check approximated with CSS zoom; native browser UI zoom and manual visual acceptance are still outstanding.
- Static previews use illustrative client data and links. Prices, customer quotes, inventory, live appointments and conversion claims are not real.
- All records remain status=draft-demo and verified=false pending scoped manual acceptance.

## Publication constraints

Both repositories are updated only on existing draft PR feature branches, leaving main and the live website unchanged. All GitHub Actions workflow directories remain absent. After human review, merge canonical design-system PR first, then the website snapshot PR.
