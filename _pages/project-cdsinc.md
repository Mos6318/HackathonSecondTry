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
<div id="hero-gallery" class="project-hero" onclick="cycleImage()">
  <div class="gallery-hint">
    <i class="fas fa-camera"></i> Click image to view next
  </div>
  <div class="hero-text-container">
    <h1 class="project-title-large">CDSInc</h1>
    <p style="font-size: 1.2rem; opacity: 0.9;">Project Portfolio</p>
  </div>
</div>

<!-- Metadata -->
<div class="project-meta-detailed">
  <div class="meta-block">
    <span class="meta-label">Authors:</span><br>
    Monika Szuban, Vanessa Scherer, Hannah Müller
  </div>
  <div class="meta-block" style="margin-top: 1rem;">
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
        In the rapidly evolving landscape of retail and interior design, customers often struggle to visualize how furniture and decor will fit into their personal spaces. Traditional static images or 2D floor plans fail to convey the true spatial relationships and aesthetic impact of products.
      </p>
      <div class="full-text">
        <p>This "imagination gap" leads to hesitation in purchasing, higher return rates, and overall customer dissatisfaction. Furthermore, checking compatibility with existing furniture and lighting conditions is nearly impossible without physically having the product in the room.</p>
        <p>Our challenge was to bridge this gap by creating an intuitive, immersive solution that empowers users to place, rotate, and interact with 3D product models in their own environment in real-time context.</p>
      </div>
    </div>
    <button class="expand-btn" onclick="toggleSection('problem-content', this)">Read More</button>
  </div>

  <!-- Method -->
  <div class="collapsible-section">
    <h3>Method</h3>
    <div id="method-content" class="collapsible-content">
      <p class="preview-text">
        We adopted a user-centered design approach, starting with extensive user research to identify key pain points in the furniture buying process. The development phase utilized Unity 3D for its robust rendering engine and AR Foundation for cross-platform Augmented Reality capabilities.
      </p>
      <div class="full-text">
        <p><strong>Phase 1: Research & Prototyping</strong><br>
        Conducted interviews and surveys (N=50) to understand user needs. Created low-fidelity wireframes in Figma to map out the user journey and core interface elements.</p>
        
        <p><strong>Phase 2: Development</strong><br>
        Implement markerless AR tracking using ARKit/ARCore. optimized 3D assets for mobile performance using Blender. programmed interactive gestures (pinch-to-scale, rotate) in C#.</p>
        
        <p><strong>Phase 3: Testing</strong><br>
        Performed usability testing sessions where users were tasked with furnishing a virtual room. Iterated on UI feedback to improve button placement and instructional cues.</p>
      </div>
    </div>
    <button class="expand-btn" onclick="toggleSection('method-content', this)">Read More</button>
  </div>

  <!-- Outcomes -->
  <div class="collapsible-section">
    <h3>Outcomes</h3>
    <div id="outcomes-content" class="collapsible-content">
      <p class="preview-text">
        The final CDSInc application successfully demonstrated a seamless AR experience. User testing revealed a 40% increase in purchase confidence compared to viewing static images alone. The application runs smoothly on standard mid-range mobile devices with stable tracking.
      </p>
      <div class="full-text">
        <p>Key achievements include:</p>
        <ul>
          <li><strong>High Fidelity Rendering:</strong> Realistic lighting and material estimation.</li>
          <li><strong>Intuitive UI:</strong> Users could place an object within 5 seconds of launching the AR session.</li>
          <li><strong>Scalability:</strong> The backend architecture allows for easy addition of new catalog items without app updates.</li>
        </ul>
        <p>The project received top marks in the "Augmented and Virtual Reality Applications" course for its technical implementation and polished user experience.</p>
      </div>
    </div>
    <button class="expand-btn" onclick="toggleSection('outcomes-content', this)">Read More</button>
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


<!-- Scripts for Interactivity -->
<script>
const images = [
  "{{ site.baseurl }}/assets/projects/Picture01.png",
  "{{ site.baseurl }}/assets/projects/Pictur02.png",
  "{{ site.baseurl }}/assets/projects/Picture03.png",
  "{{ site.baseurl }}/assets/projects/Picture04.png"
];

let currentIndex = 0;
const heroElement = document.getElementById('hero-gallery');

images.forEach(src => {
  const img = new Image();
  img.src = src;
});

if(heroElement) {
    heroElement.style.backgroundImage = `url('${images[0]}')`;
}

function cycleImage() {
  currentIndex = (currentIndex + 1) % images.length;
  if(heroElement) {
    heroElement.style.backgroundImage = `url('${images[currentIndex]}')`;
  }
}

function toggleSection(id, btn) {
  const content = document.getElementById(id);
  const isExpanded = content.classList.contains('expanded');
  
  if (isExpanded) {
    content.classList.remove('expanded');
    btn.innerText = "Read More";
  } else {
    content.classList.add('expanded');
    btn.innerText = "Read Less";
  }
}
</script>
