# Professional UI Engineering and Visual QA

Load this reference before building or modifying a real user-facing interface. Do not apply it to projects that have no UI deliverable.

## Design from the product, not from a template

Before implementation, identify the audience, primary user task, product domain, content hierarchy, brand constraints, references, and target devices. Inspect the existing UI and design system first. If the brief is incomplete, make a compact, explicit design proposal rather than silently choosing a generic SaaS template.

For this skill's user's preferred default, choose a professional light-first, product-specific visual direction and avoid dark/black-first, purple-dominant, neon-gradient, glassmorphism, glowing, or generic AI-SaaS styling unless explicitly requested. More broadly, no color theme is inherently professional; the choice must fit the product, content, and audience.

## Visual design rules

- Establish intentional typography, scale, line lengths, spacing, grid, alignment, hierarchy, and contrast.
- Use a restrained palette with named design tokens. Choose colors for meaning, hierarchy, and accessibility, not decoration.
- Use one or two type families unless the brand requires otherwise. Avoid decorative typography that harms legibility.
- Use cards only when the content needs grouping. Do not wrap every section in identical rounded cards.
- Avoid default AI landing-page tropes: gradient hero washes, glowing orbs, glass panels, identical feature-card grids, excessive pills, floating blobs, fake analytics, fake reviews, invented customer logos, random bento grids, and decorative motion without a user purpose.
- Use realistic, domain-specific content. Mark demo data honestly. Never imply real users, results, approvals, integrations, or metrics that do not exist.
- Use consistent, meaningful icons. Do not replace functional icons with random emoji.
- Define interaction states: hover, focus, active, disabled, loading, empty, error, success, and destructive confirmation where relevant.
- Ensure buttons and links perform the action their label promises. No dead controls, fake forms, inert filters, or placeholder links in a finished flow.
- Use semantic HTML and appropriate labels, keyboard interactions, focus visibility, accessible names, sufficient contrast, reduced-motion support, and accessible validation/error feedback.
- Design responsive behavior rather than merely shrinking desktop layouts. Check narrow mobile, common laptop, and wider screens as appropriate.
- Do not introduce animation unless it improves state comprehension or the product identity. Respect reduced-motion preferences.
- Use the existing design system if one exists; don't replace it wholesale to show off.

## Required two-pass workflow

### Pass A — Design brief before coding

Produce a short UI plan covering:
1. user and primary task;
2. visual direction and why it fits this product;
3. palette tokens and semantic usage;
4. typography and scale;
5. layout composition and responsive breakpoints;
6. component/state inventory;
7. accessibility requirements;
8. content/assets required and anything that is a mock/demo.

Reject directions that could be copied unchanged into almost any unrelated AI SaaS product. Revise generic choices before implementation.

### Pass B — Build and critique

Implement using the actual app architecture and content. Run the app if possible. Review rendered screenshots/previews at relevant viewports, interact with primary controls, inspect browser console/network errors where tools support it, and fix visible defects. Do not assert visual quality from source inspection alone.

## Screenshot critique rubric (score each 0–4)

- Product specificity and visual identity.
- Information hierarchy and readability.
- Layout consistency and deliberate spacing.
- Typography and contrast.
- Functional completeness and interaction feedback.
- Responsive behavior.
- Accessibility and keyboard usability.
- Authenticity of copy/data/assets.

Score 0 = absent/broken, 1 = weak, 2 = adequate but flawed, 3 = strong, 4 = excellent for the brief. Record evidence for every score below 3. Any broken primary flow, fake success, inaccessible essential action, severe responsive break, or fabricated trust/metrics is a release blocker regardless of average score.

If screenshot/browser access is unavailable, give an explicit “visual QA not performed” status and exact steps for the developer to capture/inspect the screens. Do not claim a professional result based on a screenshot-free review.
