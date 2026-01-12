---
layout: splash
permalink: /project-grannify/
title: "Grannify"
author_profile: false
---

<style>
/* Immersive Project Header */
.project-hero {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  height: 60vh;
  background-image: url('{{ site.baseurl }}/assets/images/Grannify.png');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
  padding-bottom: 4rem;
  margin-bottom: 4rem;
}

.project-hero::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0,0,0,0.2), rgba(0,0,0,0.8));
}

.hero-text-container {
  position: relative;
  z-index: 2;
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 2rem;
  width: 100%;
  text-align: center;
}

.project-title-large {
  font-size: 4rem;
  font-weight: 900;
  color: #fff;
  text-shadow: 0 4px 10px rgba(0,0,0,0.5);
  margin-bottom: 1rem;
}

.project-meta {
  display: flex;
  justify-content: center;
  gap: 2rem;
  color: rgba(255,255,255,0.9);
  font-size: 1.1rem;
}

/* Case Study Content */
.case-study-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 2rem;
  line-height: 1.8;
  font-size: 1.1rem;
}

.case-study-content h2 {
  font-size: 2rem;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
  color: var(--global-link-color);
}

.back-btn-container {
  text-align: center;
  margin: 4rem 0;
}

.back-btn {
  display: inline-block;
  padding: 12px 30px;
  border: 2px solid var(--global-link-color);
  color: var(--global-link-color);
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  border-radius: 4px;
}

.back-btn:hover {
  background: var(--global-link-color);
  color: var(--global-bg-color);
}
</style>

<div class="project-hero">
  <div class="hero-text-container">
    <h1 class="project-title-large">Grannify</h1>
    <div class="project-meta">
      <span><strong>Role:</strong> Product Designer</span>
      <span>|</span>
      <span><strong>Tools:</strong> Sketch, InVision</span>
      <span>|</span>
      <span><strong>Year:</strong> 2022</span>
    </div>
  </div>
</div>

<div class="case-study-content">
  <h2>The Challenge</h2>
  <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada. Nulla facilisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
  </p>

  <h2>The Solution</h2>
  <p>
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  </p>

  <h2>The Impact</h2>
  <p>
    Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
  </p>

  <div class="back-btn-container">
    <a href="{{ site.baseurl }}/#projects" class="back-btn">← Back to Projects</a>
  </div>
</div>
