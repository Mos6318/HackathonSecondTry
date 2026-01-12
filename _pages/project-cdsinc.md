---
layout: splash
permalink: /project-cdsinc/
title: "CDSInc"
author_profile: false
---

<style>
/* --- Page Container & Layout --- */
.page__content {
  max-width: 100% !important;
  margin: 0;
  padding: 0;
}

/* --- Hero Gallery Section --- */
.project-hero {
  width: 100vw;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  height: 70vh; /* Taller hero for impact */
  background-color: #000;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  align-items: flex-end;
  padding-bottom: 4rem;
  margin-bottom: 3rem;
  cursor: pointer; /* Indicate interactivity */
  /* simple transition on the property itself */
  transition: background-image 0.5s ease-in-out;
  overflow: hidden;
}

/* Overlay gradient for text readability */
.project-hero::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0,0,0,0.1) 50%, rgba(0,0,0,0.9) 100%);
  pointer-events: none;
  z-index: 1;
}

/* Hint for interactivity */
.gallery-hint {
  position: absolute;
  top: 20px;
  right: 20px;
  background: rgba(0,0,0,0.6);
  color: #fff;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  pointer-events: none;
  opacity: 0.8;
  border: 1px solid rgba(255,255,255,0.3);
  z-index: 2;
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
  font-size: 5rem;
  font-weight: 900;
  color: #fff;
  text-shadow: 0 4px 10px rgba(0,0,0,0.8);
  margin-bottom: 0.5rem;
  line-height: 1;
}

.project-creators {
  font-size: 1.2rem;
  color: #fff;
  opacity: 0.95;
  text-shadow: 0 2px 6px rgba(0,0,0,0.6);
  font-weight: 400;
}

/* --- Metadata Section --- */
.project-meta-detailed {
  max-width: 900px;
  margin: 0 auto 3rem auto;
  text-align: center;
  padding: 2rem;
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--global-border-color);
  border-radius: 8px;
}

.meta-block {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.meta-label {
  font-weight: 700;
  color: var(--global-link-color);
  text-transform: uppercase;
  font-size: 0.9rem;
  letter-spacing: 1px;
}

/* --- Collapsible Content Sections --- */
.content-wrapper {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 2rem;
}

.collapsible-section {
  margin-bottom: 2rem;
  border-bottom: 1px solid var(--global-border-color);
  padding-bottom: 2rem;
}

.collapsible-section h3 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: var(--global-text-color);
}

.collapsible-content {
  font-size: 1.1rem;
  line-height: 1.8;
  position: relative;
}

.full-text {
  display: none;
  margin-top: 1rem;
  opacity: 0;
  transition: opacity 0.5s ease;
}

/* Expanded state */
.collapsible-content.expanded .full-text {
  display: block;
  opacity: 1;
}

.collapsible-content.expanded .preview-text::after {
  display: none; /* Hide ellipsis/fade if used */
}

/* Read More Button */
.expand-btn {
  display: inline-block;
  margin-top: 1rem;
  background: transparent;
  border: none;
  color: var(--global-link-color);
  font-weight: 700;
  text-transform: uppercase;
  cursor: pointer;
  padding: 0;
  font-size: 0.9rem;
  letter-spacing: 0.5px;
  transition: color 0.3s;
}

.expand-btn:hover {
  text-decoration: underline;
}

/* --- Video Section --- */
.video-section {
  max-width: 800px;
  margin: 4rem auto;
  padding: 0 2rem;
  text-align: center;
}

.video-section h3 {
  margin-bottom: 1.5rem;
}

.project-video {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* --- Download Button --- */
.download-section {
  text-align: center;
  margin: 4rem 0 6rem 0;
}

.download-btn {
  display: inline-block;
  padding: 15px 40px;
  background: var(--global-link-color);
  color: var(--global-bg-color) !important;
  text-decoration: none;
  font-weight: 700;
  border-radius: 50px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  font-size: 1.1rem;
}

.download-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

/* --- Back Link --- */
.back-link-wrapper {
  text-align: center;
  margin-bottom: 4rem;
}
</style>

<!-- Hero Gallery -->
<div id="hero-gallery" class="project-hero" style="background-image: url({{ site.baseurl }}/assets/projects/Picture01.png);">
  <div class="gallery-hint">
    <i class="fas fa-camera"></i> Click image to view next
  </div>
  <div class="hero-text-container">
    <h1 class="project-title-large">CDSInc</h1>
    <p class="project-creators">Monika Szuban, Vanessa Scherer, Hannah Müller</p>
  </div>
</div>

<!-- Metadata -->
<div class="project-meta-detailed">
  <div class="meta-block">
    <span class="meta-label">Institution:</span><br>
    Technische Hochschule Ingolstadt
  </div>
  <div class="meta-block" style="margin-top: 1rem;">
    <span class="meta-label">Subject:</span><br>
    Augmented and Virtual Reality Applications
  </div>
</div>

<!-- Main Content -->
<div class="content-wrapper">

  <!-- Problem Statement -->
  <div class="collapsible-section">
    <h3>Problem Statement</h3>
    <div id="problem-content" class="collapsible-content">
      <p class="preview-text">
        This project was developed as part of a semester assignment requiring three mini-games: one in 2D and two using AR technology with image recognition, obscured objects, and interactive actions. The challenge was transforming these broad requirements into a cohesive, engaging product.
      </p>
      <div class="full-text">
        <p>Our team decided to frame the project around virtual cat care, blending playfulness with educational elements teaching responsibility in pet ownership. The goal was to create an experience where players could learn about caring for pets while having fun.</p>
        <p>We named it <strong>Cat Distribution System Inc.</strong>, inspired by the idea that "cats adopt us, not the other way around." The concept balanced humor with purpose, giving the game both character and educational direction.</p>
      </div>
    </div>
    <button class="expand-btn" data-section="problem-content">Read More</button>
  </div>

  <!-- Method -->
  <div class="collapsible-section">
    <h3>Method</h3>
    <div id="method-content" class="collapsible-content">
      <p class="preview-text">
        We structured the game around three distinct mini-games connected by theme. Development used Unity and AR Foundation, with Figma for UI design and Blender for 3D assets. Agile sprints and two rounds of usability testing shaped the final experience through iterative improvement.
      </p>
      <div class="full-text">
        <p><strong>Three Mini-Games</strong><br>
        <em>Memory Game (2D):</em> Classical matching of cat-related items under time and move limits.<br>
        <em>Toy Hunt (AR):</em> Scan environment to find hidden boxes containing cat toys with interactive feedback.<br>
        <em>Flappy Cat (AR):</em> Tilt-controlled obstacle avoidance game featuring the virtual cat.</p>
        
        <p><strong>Testing & Iteration</strong><br>
        After the first usability round, we identified struggles with AR onboarding and progress visibility. We responded with tutorials, help overlays, and progress counters. By the second round, HARUS scores improved significantly.</p>
        
        <p><strong>Tools Used</strong><br>
        Unity & AR Foundation for development, Figma for UI design, Blender for 3D models, and AI tools (ChatGPT, Claude) for rapid prototyping and debugging support.</p>
      </div>
    </div>
    <button class="expand-btn" data-section="method-content">Read More</button>
  </div>

  <!-- Outcomes -->
  <div class="collapsible-section">
    <h3>Outcomes</h3>
    <div id="outcomes-content" class="collapsible-content">
      <p class="preview-text">
        The final game featured three fully integrated mini-games with measurably improved usability between test rounds. We made the game available on GitHub and were invited to showcase it at GG Bavaria Convention (March 2025), validating its educational and entertainment value.
      </p>
      <div class="full-text">
        <p><strong>Key Achievements:</strong></p>
        <ul>
          <li><strong>Functional AR Integration:</strong> Successfully implemented image recognition, object tracking, and interactive AR experiences across two mini-games.</li>
          <li><strong>Improved Usability:</strong> HARUS survey scores showed significant improvement in onboarding clarity and progress tracking between testing rounds.</li>
          <li><strong>Educational Impact:</strong> Balanced playful design with subtle lessons on pet care responsibility, achieving the project's dual purpose.</li>
          <li><strong>External Recognition:</strong> Selected for showcase at GG Bavaria Convention, demonstrating the game's polish and appeal beyond the classroom.</li>
        </ul>
        <p>The project received top marks in the "Augmented and Virtual Reality Applications" course and is <a href="https://github.com/Mos6318/HackathonSecondTry" target="_blank">available on GitHub</a> for download.</p>
      </div>
    </div>
    <button class="expand-btn" data-section="outcomes-content">Read More</button>
  </div>

</div>

<!-- Video Section -->
<div class="video-section">
  <h3>Project Trailer</h3>
  <video controls class="project-video">
    <source src="{{ site.baseurl }}/assets/projects/CDSIncTrailer.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

<!-- Download -->
<div class="download-section">
  <a href="#" class="download-btn">Download PDF Report</a>
</div>

<!-- Back Link -->
<div class="back-link-wrapper">
  <a href="{{ site.baseurl }}/#projects" style="color: var(--global-text-color-light); border-bottom: 1px solid;">&larr; Back to all projects</a>
</div>


<script>
(function() {
  /* Safely define vars in IIFE but expose functions to window */
  
  var images = [
    "{{ site.baseurl }}/assets/projects/Picture01.png",
    "{{ site.baseurl }}/assets/projects/Pictur02.png",
    "{{ site.baseurl }}/assets/projects/Picture03.png",
    "{{ site.baseurl }}/assets/projects/Picture04.png"
  ];
  
  var currentIndex = 0;
  
  function initGallery() {
    console.log("CDSInc: Initializing gallery and interactive elements");
    
    var heroElement = document.getElementById('hero-gallery');
    
    /* Preload images */
    images.forEach(function(src) {
      var img = new Image();
      img.src = src;
    });

    /* Attach click handler to hero for gallery cycling */
    if(heroElement) {
      heroElement.addEventListener('click', function() {
        currentIndex = (currentIndex + 1) % images.length;
        heroElement.style.backgroundImage = 'url(' + images[currentIndex] + ')';
      });
      
      /* Set initial image if not already set */
      if(!heroElement.style.backgroundImage || heroElement.style.backgroundImage === 'none') {
        heroElement.style.backgroundImage = 'url(' + images[0] + ')';
      }
    }
    
    /* Attach click handlers to all Read More buttons */
    var expandButtons = document.querySelectorAll('.expand-btn');
    expandButtons.forEach(function(btn) {
      btn.addEventListener('click', function() {
        var sectionId = btn.getAttribute('data-section');
        var content = document.getElementById(sectionId);
        
        if (!content) return;
        
        var isExpanded = content.classList.contains('expanded');
        if (isExpanded) {
          content.classList.remove('expanded');
          btn.innerText = "Read More";
        } else {
          content.classList.add('expanded');
          btn.innerText = "Read Less";
        }
      });
    });
    
    console.log("CDSInc: Gallery and buttons initialized successfully");
  }

  /* Robust Execution Trigger */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGallery);
  } else {
    initGallery();
  }
})();
</script>
