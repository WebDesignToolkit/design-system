# Agency Component Foundry v0.2

27 new patterns in nine families (three variants each): headers, navigation, heroes, pricing, testimonials, portfolio, products, booking, landing pages. Existing 17 v0.1 records preserved: 44 total.

## Contracts
Canonical registry: library/registry.json. Unique ID, group, variant, version, status, editable props, dependencies and verification contract are tracked per item. The props array is a copy/edit HTML contract, NOT a reactive framework runtime API. See each prop's name, type, example default and usage guidance.

Copy item HTML and library/styles/library.css and wrap it in a data-wd-theme scope (hardline, studio, or calm). Booking form demos also require library/scripts/interactions.js, which ONLY validates and announces no submission. Real bookings need explicit backend integration and privacy review.

All records begin as draft-demo / verified=false. Copyable markup does not guarantee production security, WCAG conformity, working client links, consent, accurate pricing or authorized images. Replacement of all illustrative information is mandatory.

## Provenance and philosophy
Inspired by the organization and canonical IDs of SabPuja Component Lab, but all patterns here are original brand-neutral work. No SabPuja customer statements, brand artwork, product media or Liquid source copied.

## Verification
Run python library/tests/validate_foundry.py and the Puppeteer browser tests against a local HTTP server. Verify 360, 768, 1280, keyboard, reduced motion and source snapshot. See docs/QA-EVIDENCE.md.
