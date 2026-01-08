---
permalink: /
title: "Monika Szuban"
author_profile: false
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
  <h2>Featured Projects</h2>
  
  <!-- Project 1 -->
  <div class="project-card">
    <div class="project-images">
      <img src="/HackathonSecondTry/assets/images/Placeholder.png" alt="Project 1">
    </div>
    <div class="project-content">
      <h3 class="project-title">Project Title One</h3>
      <div class="project-divider"></div>
      <p class="project-description">
        From gravida nisl ut velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris.
      </p>
      <a href="#" class="project-btn">VIEW PROJECT</a>
    </div>
  </div>

  <!-- Project 2 (Reversed) -->
  <div class="project-card project-card-reverse">
    <div class="project-content">
      <h3 class="project-title">Project Title Two</h3>
      <div class="project-divider"></div>
      <p class="project-description">
        From gravida nisl ut velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris.
      </p>
      <a href="#" class="project-btn">VIEW PROJECT</a>
    </div>
    <div class="project-images">
      <img src="/HackathonSecondTry/assets/images/Placeholder.png" alt="Project 2">
    </div>
  </div>

  <!-- Project 3 -->
  <div class="project-card">
    <div class="project-images">
      <img src="/HackathonSecondTry/assets/images/Placeholder.png" alt="Project 3">
    </div>
    <div class="project-content">
      <h3 class="project-title">Project Title Three</h3>
      <div class="project-divider"></div>
      <p class="project-description">
        From gravida nisl ut velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris.
      </p>
      <a href="#" class="project-btn">VIEW PROJECT</a>
    </div>
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
  padding: 4rem 0;
  min-height: auto;
  max-width: 1400px;
  margin: 0 auto;
}

.projects-section h2 {
  font-size: 2.5rem;
  margin-bottom: 4rem;
  text-align: center;
}

/* Project Card - Asymmetric Layout */
.project-card {
  display: grid;
  grid-template-columns: 40% 60%;
  min-height: 500px;
  margin-bottom: 6rem;
  gap: 0;
  align-items: center;
}

.project-card-reverse {
  grid-template-columns: 60% 40%;
}

/* Project Images */
.project-images {
  width: 100%;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.project-images img {
  width: 100%;
  max-width: 500px;
  height: 500px;
  object-fit: cover;
}

/* Project Content */
.project-content {
  padding: 80px 60px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  height: 100%;
}

.project-title {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 20px;
  line-height: 1.2;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.project-divider {
  width: 60px;
  height: 3px;
  background: var(--global-link-color);
  margin-bottom: 40px;
}

.project-description {
  font-size: 1rem;
  line-height: 1.8;
  margin-bottom: 60px;
  opacity: 0.9;
}

.project-btn {
  display: inline-block;
  padding: 12px 30px;
  border: 2px solid var(--global-link-color);
  color: var(--global-link-color);
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  align-self: flex-start;
  white-space: nowrap;
}

.project-btn:hover {
  background: var(--global-link-color);
  color: var(--global-bg-color);
  transform: translateY(-2px);
}

/* Responsive */
@media (max-width: 968px) {
  .project-card,
  .project-card-reverse {
    grid-template-columns: 1fr;
    min-height: auto;
  }
  
  .project-images {
    min-height: 400px;
  }
  
  .project-content {
    padding: 40px 30px;
  }
}

/* About Section */
.about-section {
  padding: 4rem 2rem;
  min-height: 100vh;
  max-width: 1400px;
  margin: 0 auto;
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

/* Floating Social Links */
.floating-social {
  position: fixed;
  right: 2rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  z-index: 100;
}

.floating-social a {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--global-bg-color);
  border: 2px solid var(--global-link-color);
  border-radius: 50%;
  color: var(--global-link-color);
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 1.2rem;
}

.floating-social a:hover {
  background: var(--global-link-color);
  color: var(--global-bg-color);
  transform: scale(1.1);
}

/* Hide floating social on mobile */
@media (max-width: 768px) {
  .floating-social {
    display: none;
  }
}

/* Smooth Scroll */
html {
  scroll-behavior: smooth;
}

section {
  scroll-margin-top: 70px; /* Account for fixed header */
}
</style>

<!-- Floating Social Links -->
<div class="floating-social">
  <a href="https://github.com/academicpages" target="_blank" rel="noopener" title="GitHub">
    <i class="fab fa-github"></i>
  </a>
  <a href="https://orcid.org/yourorcidurl" target="_blank" rel="noopener" title="ORCID">
    <i class="fab fa-orcid"></i>
  </a>
  <a href="mailto:none@example.org" title="Email">
    <i class="fas fa-envelope"></i>
  </a>
  <a href="https://linkedin.com/in/yourprofile" target="_blank" rel="noopener" title="LinkedIn">
    <i class="fab fa-linkedin"></i>
  </a>
  <a href="https://behance.net/yourprofile" target="_blank" rel="noopener" title="Behance">
    <i class="fab fa-behance"></i>
  </a>
</div>
