# Portfolio Website Development Task List

## Phase 2: Setup

### Milestone 1: Initialize Repository ✅
- [x] Create a new public repository on GitHub (HackathonSecondTry)
- [x] Clone the repository to local computer
- [x] Navigate to Hackathon Portal and log in with GitHub
- [x] Register repository URL in the dashboard
- [x] Link Git & Dashboard
- [x] Modify README.md file
- [x] Push with commit message: "Git linked"
- [x] Verify status on dashboard
- [x] Configure Webhooks
  - [x] Go to GitHub repo settings > Webhooks
  - [x] Add Payload URL: https://vc-hackathon-hub.vercel.app/api/webhooks/github
  - [x] Set Content type to application/json
  - [x] Select only the "push event"

## Phase 3: "Vibecoding" Development

### Milestone 2: Clone Template ✅
- [x] Clone "Academic Pages" repository into hackathon folder
- [x] Commit with tag: "Academic cloned"

### Milestone 3: Strategy: Product Requirement Document ✅
- [x] Create PRD using template or AI tools
- [x] Save as markdown document (.md)
- [x] Commit with tag: "PRD done"

### Milestone 4: Design: Custom Theme ✅
- [x] Customize theme (background color, icons, fonts)
- [x] Ensure theme icon hover state offers 3 options (light, dark, custom)
- [x] Update to VS Code inspired colors with custom accents
  - [x] Dark theme: #202334 bg, #747A9C text
  - [x] Light theme: #F5F7FA bg, #3D4466 text
- [x] Add Poppins typography (Black for titles, Light for body)
- [x] Fix light theme activation
- [x] Create third Cyberpunk gaming theme
  - [x] Background: #0a0e27, Text: #e0e6f7
  - [x] Accents: Hot pink #ff2a6d, Electric cyan #05d9e8
  - [x] Pink-to-cyan gradient for site title
  - [x] Neon glow effect on link hovers
- [x] Implement 3-way toggle (light → dark → cyberpunk)
- [x] Add custom 3D geometric PNG icons
  - [x] Icosahedron for light theme
  - [x] Torus Knot for dark theme
  - [x] Torus for cyberpunk theme
- [x] Commit with tag: "Theme done"

### Milestone 5: Implementation: Hero Landing Page
- [ ] Simplify site navigation
  - [ ] Update top navigation menu
    - [ ] Rename "Portfolio" to "Projects"
    - [ ] Keep only: Projects, CV, About
    - [ ] Remove other navigation items
  - [ ] Update social/contact links
    - [ ] Keep: GitHub, ORCID, Email, LinkedIn
    - [ ] Consider adding: Behance
    - [ ] Remove other social links
- [ ] Create personalized landing page
  - [ ] Add tagline and welcome message
  - [ ] Add profile picture or AI-generated hero image
  - [ ] Include quick access links to content
- [ ] Commit with tag: "Hero done"

### Milestone 6: Implementation: Accessible CV
- [ ] Create Mode 1: Text-based CV (Web-optimized)
- [ ] Create Mode 2: Visual-based (timeline, infographic, or storyboard)
- [ ] Create Mode 3: Audio-based (podcast snippet)
- [ ] Commit with tag: "CV done"

### Milestone 7/8: Implementation: Interactive Project or Paper
- [ ] Choose Option A (Interactive Paper) or Option B (Interactive Portfolio)
- [ ] Implement chosen option with interactive elements
- [ ] Include PDF download link
- [ ] Commit with tag: "Paper done" or "Project done"
