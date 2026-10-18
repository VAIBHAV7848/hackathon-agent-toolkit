# Professional UI Design Brief

> Use only when a digital interface is part of the project's actual deliverable. This brief exists to help produce a product-specific, polished interface—not a generic AI-generated template. Label provisional choices and keep visual QA status evidence-based.

## 1. Product and audience
- Product/project:
- Primary user and context:
- Most important user task:
- Domain, tone, trust needs, and usage frequency:
- Device/viewport priority:
- Official requirements / judging criteria related to the UI:

## 2. Existing context and references
- Existing UI / repository / screenshots inspected:
- Current components or design system to preserve:
- Brand rules or approved references:
- Reference products/screens and the specific qualities to learn from (not copy blindly):
- Missing visual context or assumptions:

## 3. Recommended visual direction
- One-sentence design direction:
- Why this fits the product and audience:
- Content hierarchy / information architecture:
- Layout density and grid:
- Typography approach and hierarchy:
- Palette rationale and color tokens by role:
- Component shape, borders, elevation, and motion rules:
- Icon and imagery policy / provenance:

### Default anti-generic-AI constraints
Unless a user-approved or binding brand requirement explicitly calls for a conflicting treatment, avoid black/dark-mode-first canvases, purple-dominant palettes, purple/blue/pink gradients, gradient text, neon/glows, floating gradient blobs, glassmorphism, generic hero-plus-repeated-card layouts, fake metrics/testimonials, irrelevant stock art, emoji as functional icons, excessive pill shapes, and gratuitous decoration. Do not replace these with a bland generic white SaaS template; choose layout, color, density, and visual character for the actual product.

## 4. Screens and states in scope
| Screen / route | User goal | Key content/actions | States to cover | Acceptance checks |
|---|---|---|---|---|
| | | | loading / empty / error / success / disabled / offline as applicable | |

## 5. Design system and implementation constraints
- Existing components/styles that must remain compatible:
- Needed reusable tokens/components:
- Components to reuse rather than rebuild:
- Dependencies to avoid or justify:
- Responsive breakpoints / target devices:
- Accessibility checks: contrast, keyboard/focus, semantics, labels, touch targets as relevant:

## 6. Functional interaction requirements
- Core workflow from entry to completion:
- Validation and error feedback:
- Loading / empty / success / permission-denied / offline behavior as relevant:
- Real vs mocked/sample content (clearly labeled):
- Performance or browser/device constraints:

## 7. Visual QA plan
| Route/screen | Viewport/device | What to inspect | Evidence required | Status |
|---|---|---|---|---|
| | | hierarchy, alignment, typography, spacing, palette, responsive layout, content fit, component consistency | screenshot/preview and interaction evidence where applicable | not reviewed |

## 8. Anti-pattern checklist
- [ ] No unmotivated dark/black or purple-dominant styling.
- [ ] No generic AI gradient/glow/glassmorphism decoration unless explicitly justified and approved.
- [ ] No repeated feature-card layout where a task-specific layout would be clearer.
- [ ] No fake metrics, fake testimonials, filler copy, or misleading demo data.
- [ ] No inconsistent typography, spacing, radii, shadows, or icon styles.
- [ ] All visible controls have meaningful behavior or are clearly disabled/non-interactive.
- [ ] Loading, empty, error, and success states are handled where relevant.
- [ ] Responsive and accessibility checks are performed at appropriate target sizes.
- [ ] The visual result has been inspected from actual rendered output, or is marked visually unverified.

## 9. Decisions, assumptions, and approval
| Decision | Rationale/evidence | Status (approved/provisional/unresolved) | Owner |
|---|---|---|---|
| | | | |

## 10. Implementation handoff
- Screens/components in scope:
- Scope out:
- Acceptance criteria:
- Required screenshots/preview evidence:
- Validation commands/tests where relevant:
- Stop conditions and decisions requiring human approval:


## 11. Visual quality scorecard (heuristic, not a universal standard)

Score each applicable dimension from 0 to 2 using actual rendered evidence: `0 = clear defect`, `1 = mixed / needs improvement`, `2 = strong for this product and audience`. Mark `N/A` only with a reason. Do not score source code as visual evidence.

| Dimension | 0–2 | Evidence / finding |
|---|---:|---|
| Product-specific visual identity (not a generic template) | | |
| Information hierarchy and task clarity | | |
| Typography, spacing, alignment, and layout consistency | | |
| Purposeful color, contrast, and readable surfaces | | |
| Component consistency and meaningful interaction states | | |
| Responsive behavior at target viewports | | |
| Accessibility basics relevant to the interface | | |
| Content authenticity; no fake claims or filler | | |
| Fit to existing brand/design system and domain | | |
| Rendered-evidence coverage across key screens/states | | |

Use the score to focus fixes, not to claim compliance with a formal design standard. Any critical issue affecting the core workflow, legibility, data integrity, or user safety blocks a “ready” verdict regardless of total score. If no screenshots or live preview were reviewed, leave the visual score unassigned and mark visual QA unverified.
