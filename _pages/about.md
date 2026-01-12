---
permalink: /
title: ""
layout: splash
author_profile: false
redirect_from: 
  - /about/
  - /about.html
---

<section id="home" class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Lily</h1>
    <p class="hero-tagline">Where creativity meets purpose and impact.</p>
    <p class="hero-welcome">
      Welcome to my digital portfolio. Here you'll find a collection of my latest projects, demonstrating my passion for building immersive and user-centric digital experiences. Explore my work and get to know the person behind the code.
    </p>
    <div class="hero-cta">
      <a href="#projects" class="hero-btn">View Projects</a>
      <a href="{{ site.baseurl }}/assets/images/monika_szuban_cv.pdf" class="hero-btn" download>Download CV</a>
    </div>
    <!-- Placeholder for future AI Hero Image -->
    <div class="hero-image-placeholder"></div>
  </div>
</section>

<section id="projects" class="projects-section">
  <h2>Featured Projects</h2>
  
  <!-- Project 1 -->
  <div id="project-1" class="project-card">
    <div class="project-images">
      <img src="/HackathonSecondTry/assets/images/CDSInc.png" alt="CDSInc">
    </div>
    <div class="project-content">
      <h3 class="project-title">CDSInc</h3>
      <div class="project-divider"></div>
      <p class="project-description">
        From gravida nisl ut velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris.
      </p>
      <a href="{{ site.baseurl }}/project-cdsinc/" class="project-btn">VIEW PROJECT</a>
    </div>
  </div>

  <!-- Project 2 (Reversed) -->
  <div id="project-2" class="project-card project-card-reverse">
    <div class="project-content">
      <h3 class="project-title">Echo Drive</h3>
      <div class="project-divider"></div>
      <p class="project-description">
        From gravida nisl ut velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris.
      </p>
      <a href="{{ site.baseurl }}/project-echodrive/" class="project-btn">VIEW PROJECT</a>
    </div>
    <div class="project-images">
      <img src="/HackathonSecondTry/assets/images/Echo_drive.png" alt="Echo Drive">
    </div>
  </div>

  <!-- Project 3 -->
  <div id="project-3" class="project-card">
    <div class="project-images">
      <img src="/HackathonSecondTry/assets/images/Grannify.png" alt="Grannify">
    </div>
    <div class="project-content">
      <h3 class="project-title">Grannify</h3>
      <div class="project-divider"></div>
      <p class="project-description">
        From gravida nisl ut velit auctor aliquet. Aenean sollicitudin, lorem quis bibendum auctor, nisi elit consequat ipsum, nec sagittis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris.
      </p>
      <a href="{{ site.baseurl }}/project-grannify/" class="project-btn">VIEW PROJECT</a>
    </div>
  </div>
</section>

<section id="about" class="about-section">
  <h2>About Me</h2>
  <div class="about-content">
    <p>I’m Monika, a passionate Creative Designer with a background in industrial and user experience design. I focus on crafting intuitive, user-centered digital experiences that are visually engaging and purpose-driven, with the goal of solving real problems and creating lasting impact.</p>
    
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
  margin-bottom: 1.5rem;
  opacity: 0.9;
}

.hero-welcome {
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto 2rem auto;
  line-height: 1.6;
  opacity: 0.8;
}

.hero-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.hero-btn {
  display: inline-block;
  padding: 12px 30px;
  border: 2px solid var(--global-link-color);
  color: var(--global-link-color);
  background: transparent;
  text-decoration: none;
  font-weight: 600;
  letter-spacing: 1px;
  transition: all 0.3s ease;
  white-space: nowrap;
  text-transform: uppercase;
}

.hero-btn:hover {
  background: var(--global-link-color);
  color: var(--global-bg-color);
  transform: translateY(-2px);
}

/* Projects Section */
.projects-section {
  padding: 4rem 0;
  min-height: auto;
  max-width: 100%;
  margin: 0 auto;
}

.projects-section h2 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  text-align: center;
}

/* Project Card - Asymmetric Layout */
.project-card {
  display: grid;
  grid-template-columns: 698px 482px;
  column-gap: 124px;
  
  /* Force Full Viewport Width */
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  
  padding: 62px 0;
  justify-content: center;
  align-items: start;
}

.project-card-reverse {
  grid-template-columns: 482px 698px;
  column-gap: 124px;
  padding: 62px 0;
}

/* Project Images */
.project-images {
  width: 698px;
  height: 608.53px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.project-images img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
  transition: transform 0.3s ease; /* Smooth zoom transition */
}

/* Hover Effects */
.project-card, .project-card-reverse {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.project-card:hover, .project-card-reverse:hover {
  transform: translateY(-5px) scale(1.01);
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.project-card:hover .project-images img, 
.project-card-reverse:hover .project-images img {
  transform: scale(1.02);
}

/* Project Content */
.project-content {
  width: 482px;
  min-height: 482px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding-top: 84px;
}

.project-card-reverse .project-content {
  order: -1;
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
  overflow-x: hidden; /* Prevent horizontal scroll from full-width elements */
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

<style>
/* Custom Navigation Layout */
.greedy-nav .visible-links {
  display: flex !important;
  align-items: center;
  width: 100%;
}

.greedy-nav .visible-links li {
  display: inline-block !important;
  vertical-align: middle;
}

.greedy-nav .visible-links li:first-child {
  margin-right: auto;
}

.greedy-nav .visible-links li:not(:first-child):not(#theme-toggle) {
  margin: 0 1rem;
  font-size: 0.75rem;
}

.greedy-nav .visible-links #theme-toggle {
  margin-left: auto;
}

/* Restore navigation bar padding */
.masthead__inner-wrap {
  padding: 0.5em 1em !important;
}

/* Hide burger menu button */
.greedy-nav button {
  display: none !important;
}

/* Ensure hidden-links don't interfere */
.greedy-nav .hidden-links {
  display: none !important;
}

/* Force all navigation items to stay visible */
.greedy-nav .visible-links li[style*="display: none"] {
  display: inline-block !important;
}
</style>

<script>
// Disable greedy navigation behavior - keep all items visible
document.addEventListener('DOMContentLoaded', function() {
  // Remove any inline styles that hide navigation items
  const navItems = document.querySelectorAll('.greedy-nav .visible-links li');
  navItems.forEach(item => {
    item.style.display = 'inline-block';
  });
  
  // Disable the greedy nav resize observer if it exists
  if (window.ResizeObserver) {
    const originalResizeObserver = window.ResizeObserver;
    window.ResizeObserver = function(callback) {
      return new originalResizeObserver(function(entries, observer) {
        // Don't call the callback for greedy-nav elements
        const filteredEntries = entries.filter(entry => {
          return !entry.target.classList.contains('greedy-nav');
        });
        if (filteredEntries.length > 0) {
          callback(filteredEntries, observer);
        }
      });
    };
  }
});
</script>
