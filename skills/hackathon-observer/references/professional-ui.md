# Professional UI Quality Module

## Professional UI quality module — mandatory when a digital interface is in scope

The goal is a credible, polished, purpose-built interface—not a generic page that looks automatically generated from a trendy prompt. Apply this module to web, mobile, desktop, game, dashboard, admin, and other digital interfaces. Skip it when the project has no UI or when the event deliverable is not an interface; do not invent a UI solely to satisfy this section.

### A. Design from the product, not from a trend

Before asking a coding/design agent to make screens, determine:
- the primary user, their context, top task, frequency of use, and cost of confusion;
- the product's domain, tone, trust requirements, content density, and key workflow;
- any established brand, design system, supplied references, existing UI, or hard competition requirements;
- the information hierarchy and the action the user should complete on each screen;
- what evidence is available: repository/styles/components, product screenshots, user feedback, assets, or official branding.

If these inputs are missing, prepare a compact `templates/ui-design-brief.md` using clearly labeled provisional choices. When the visual direction is a major decision, present one coherent, contextual direction for approval before producing a large implementation prompt. Do not ask a long list of low-value style questions when sensible decisions can be grounded in the project.

### B. Default visual quality policy — avoid generic AI-generated aesthetics

Unless the user explicitly asks for them or a binding existing brand/competition requirement forces a conflict that must be surfaced, DO NOT default to:
- black/dark-mode canvases or a purple-dominant palette;
- purple/blue/pink gradient backgrounds, gradient headline text, neon borders, glow effects, floating gradient blobs, or ambient light effects;
- glassmorphism, blurred translucent panels, glossy 3D decorations, or effects that reduce readability;
- a generic centered hero followed by repeated feature cards, decorative stat cards, fake dashboards, or the same card grid on every page;
- excessive pill-shaped buttons, indiscriminate huge corner radii, overuse of shadows/borders, or oversized whitespace that wastes space;
- generic AI/product landing-page copy, fake testimonials, invented metrics, meaningless labels, emoji used as interface icons, or unrelated stock illustrations;
- random visual flourishes added solely to make a page appear futuristic or “premium.”

Prefer a light or neutral, legible canvas as the default, with a restrained, context-appropriate palette selected for the product's audience and domain—not a fixed color recipe. The accent color must have a rationale, and black/dark or purple-dominant treatment is not the default. If official branding, an existing product identity, or the user's explicit instruction conflicts with this default, describe the conflict and obtain a decision instead of silently overriding the user's direction.

Avoid overcorrecting into a bland, generic white SaaS template. Professional design is product-specific: choose layout, density, typography, imagery, color, and interaction patterns based on the actual task. A design may be expressive when the domain justifies it, but every prominent visual decision must serve identity, comprehension, accessibility, or task completion.

### C. Require an intentional design system

For interfaces of meaningful complexity, specify before implementation:
- visual direction in plain language and why it fits the target audience;
- color tokens by role (canvas, surface, text, muted text, border, primary action, status, focus) and contrast checks;
- a restrained typography system with a clear hierarchy, readable sizes, line lengths, and consistent weights;
- spacing scale, content width, grid/alignment rules, and responsive breakpoints;
- consistent component behavior for navigation, buttons, forms, tables, dialogs, feedback, and any repeated patterns;
- icon family and usage rules; use one coherent icon style and do not substitute emoji for functional icons;
- a domain-appropriate illustration/photo/data-visualization policy, with licensing/provenance and no invented evidence;
- interaction and content states: loading, empty, error, success, disabled, validation, permission-denied, and offline states where applicable.

Reuse an existing design system and components when they are sound. Do not replace the project's established design language just for novelty. Avoid adding dependencies or building a large component library unless the project needs it.

### D. Functional polish is part of visual quality

A screenshot-only mockup is not a complete interface if the promised deliverable is interactive. Confirm the UI supports the core user workflow, clear navigation, meaningful actions, input validation, useful feedback, predictable behavior, and graceful failure. Use authentic content where available; label demo/mock/sample data honestly. Never create fake metrics or testimonials to make the screen look convincing.

Require responsive behavior for the actual target devices and check overflow, clipping, touch targets, focus visibility, keyboard navigation, semantic structure, readable contrast, and form labels as applicable. Do not merely claim “accessible” or “responsive”; define the checks and evidence needed.

### E. Visual QA and anti-slop audit

Before declaring the UI ready, require evidence from the actual rendered interface when possible: screenshots or a preview at relevant viewport sizes, plus interaction/test evidence for core flows. Inspect:
- hierarchy, alignment, spacing, typography, color roles, and consistency;
- whether each component is useful and whether the page fits the actual domain rather than a generic template;
- visual clutter, repetitive cards, gratuitous decoration, awkward whitespace, placeholder text, or fake data;
- responsive layouts and representative loading/empty/error/success states;
- core interactions, accessibility checks, and regressions against existing functionality.

Record findings with screenshot/route/component reference, severity, consequence, and a concrete fix. Distinguish visually verified from code-reviewed or merely planned. If no rendered screenshot/preview is available, state that visual QA is still unverified and provide the exact review steps; do not claim the UI looks professional based on source code alone.

When drafting an execution prompt for a coding/design agent, include the approved UI brief, specific screens and components in scope, existing design-system constraints, anti-patterns to avoid, responsive/accessibility requirements, acceptance criteria, and a request for rendered screenshots or preview evidence. Do not ask for vague “make it modern/premium/beautiful” changes alone.
