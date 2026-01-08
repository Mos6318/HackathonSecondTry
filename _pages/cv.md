---
layout: archive
title: "CV"
permalink: /cv/
author_profile: false
redirect_from:
  - /resume
---

{% include base_path %}

<div class="floating-social">
  <div class="vertical-line"></div>
  <a href="https://github.com/Mos6318" target="_blank" rel="noopener" title="GitHub">
    <i class="fab fa-github"></i>
  </a>
  <a href="https://orcid.org/0009-0007-1678-2947" target="_blank" rel="noopener" title="ORCID">
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

Education
======
* Ph.D in Version Control Theory, GitHub University, 2018 (expected)
* M.S. in Jekyll, GitHub University, 2014
* B.S. in GitHub, GitHub University, 2012

Work experience
======
* Spring 2024: Academic Pages Collaborator
  * GitHub University
  * Duties includes: Updates and improvements to template
  * Supervisor: The Users

* Fall 2015: Research Assistant
  * GitHub University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub

* Summer 2015: Research Assistant
  * GitHub University
  * Duties included: Tagging issues
  * Supervisor: Professor Git
  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams

<style>
/* Floating Social Links */
.floating-social {
  position: fixed;
  right: 40px;
  bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  z-index: 100;
  padding-bottom: 40px;
}

.floating-social a {
  color: var(--global-text-color);
  font-size: 20px;
  transition: all 0.3s ease;
  opacity: 0.6;
}

.floating-social a:hover {
  color: var(--global-link-color);
  transform: translateY(-3px);
  opacity: 1;
}

.floating-social .vertical-line {
  width: 1px;
  height: 100px;
  background-color: var(--global-text-color);
  opacity: 0.3;
  margin-bottom: 20px;
}

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

@media (max-width: 768px) {
  .floating-social {
    display: none;
  }
}

/* Page Layout Fixes */
.sidebar {
  display: none !important;
}

.page__content {
  width: 100% !important;
  max-width: 100% !important;
  margin-right: 0 !important;
  padding-right: 0 !important;
}

.archive {
  width: 100% !important;
  margin-right: 0 !important;
  padding-right: 0 !important;
  max-width: 1200px; /* Limit readability width */
  margin: 0 auto;
}

/* Ensure FontAwesome icons work and are visible */
.floating-social i {
  font-family: "Font Awesome 5 Brands", "Font Awesome 5 Free" !important;
  font-weight: 900;
  display: inline-block;
  font-style: normal;
  font-variant: normal;
  text-rendering: auto;
  line-height: 1;
}

.floating-social .fab {
  font-family: "Font Awesome 5 Brands" !important;
}

.floating-social .fas {
  font-family: "Font Awesome 5 Free" !important;
  font-weight: 900;
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
