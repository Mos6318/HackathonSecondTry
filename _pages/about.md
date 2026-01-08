---
permalink: /
title: "Monika Szuban"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<section id="home" class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Monika Szuban</h1>
    <p class="hero-tagline">UX Designer crafting experiences for gaming studios</p>
    <div class="hero-cta">
      <a href="#projects" class="btn btn-primary">View Projects</a>
      <a href="/cv/" class="btn btn-secondary">Download CV</a>
    </div>
  </div>
</section>

<section id="projects" class="projects-section">
  <h2>Projects</h2>
  <div class="projects-grid">
    {% for post in site.portfolio %}
      {% include archive-single.html %}
    {% endfor %}
  </div>
</section>

<section id="about" class="about-section">
  <h2>About Me</h2>
  <div class="about-content">
    <p>Welcome to my portfolio! I'm a UX Designer passionate about creating engaging experiences for the gaming industry.</p>
    
    <h3>What I Do</h3>
    <p>I specialize in user experience design, focusing on creating intuitive and engaging interfaces that enhance player experiences.</p>
    
    <h3>Get In Touch</h3>
    <p>Interested in working together? Feel free to reach out through any of the social links in the sidebar, or check out my full CV for more details about my experience and skills.</p>
  </div>
</section>

<style>
/* Hero Section */
.hero-section {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
}

.hero-title {
  font-size: 4rem;
  font-weight: 900;
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--global-link-color), var(--global-link-color-hover));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-tagline {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 0.75rem 2rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-primary {
  background: var(--global-link-color);
  color: white;
}

.btn-primary:hover {
  background: var(--global-link-color-hover);
  transform: translateY(-2px);
}

.btn-secondary {
  border: 2px solid var(--global-link-color);
  color: var(--global-link-color);
}

.btn-secondary:hover {
  background: var(--global-link-color);
  color: white;
  transform: translateY(-2px);
}

/* Projects Section */
.projects-section {
  padding: 4rem 2rem;
  min-height: 100vh;
}

.projects-section h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-align: center;
}

.projects-grid {
  max-width: 1200px;
  margin: 0 auto;
}

/* About Section */
.about-section {
  padding: 4rem 2rem;
  min-height: 100vh;
}

.about-section h2 {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-align: center;
}

.about-content {
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.8;
}

.about-content h3 {
  margin-top: 2rem;
  margin-bottom: 1rem;
}

/* Smooth Scroll */
html {
  scroll-behavior: smooth;
}

section {
  scroll-margin-top: 70px; /* Account for fixed header */
}
</style>
