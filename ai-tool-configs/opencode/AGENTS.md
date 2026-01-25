# Global Agent Instructions

## 1) Atomic Commits

Every distinct logical update must be committed individually and automatically after every change completion. Batching multiple changes into a single commit is strictly prohibited.

## 2) Merge Restrictions

Never merge with other branches without explicit, prior consent or instruction.

## 3) Aesthetics And Creativity

You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight.

Focus on:

- Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color and theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:

- Overused font families (Inter, Roboto, Arial, system fonts)
- Cliched color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box. To follow consistent design, you can create a `design-guide.md` file in the docs folder.

## 4) Strict Syntax And Linting

Act as a strict linter to prevent build errors and smart quote corruption.

React/JSX text handling (critical):

- Always wrap text containing apostrophes (single quotes) or double quotes in JSX within a JavaScript expression.
- Bad: `<p>User's Profile</p>` (causes `react/no-unescaped-entities`)
- Bad: `<p>User&amp;apos;s Profile</p>` (valid but reduces readability)
- Good: `<p>{"User's Profile"}</p>`

Quote standardization:

- Never use typographical (curly) quotes. Use only standard ASCII straight quotes (`'` and `"`).
- Strictly use double quotes (`"`) for all JSX attributes.
- Strictly use single quotes (`'`) for standard JavaScript/TypeScript string literals.
- Exception: If a string contains a single quote, switch to double quotes to avoid backslash escaping (e.g., use `"Don't do this"` instead of `'Don\'t do this'`).
