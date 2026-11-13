/**
 * MMA-SFI (Mixed Martial Arts Sports Federation of India)
 * Main Interactive Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Header
  const siteHeader = document.querySelector('.site-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      siteHeader.classList.add('scrolled');
    } else {
      siteHeader.classList.remove('scrolled');
    }
  });

  // 2. Mobile Drawer Navigation
  const mobileToggle = document.querySelector('.mobile-toggle-btn');
  const mobileDrawer = document.querySelector('.mobile-drawer');
  const mobileOverlay = document.querySelector('.mobile-drawer-overlay');

  function toggleMobileMenu() {
    mobileToggle.classList.toggle('active');
    mobileDrawer.classList.toggle('open');
    mobileOverlay.classList.toggle('open');
    document.body.style.overflow = mobileDrawer.classList.contains('open') ? 'hidden' : '';
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleMobileMenu);
  }
  if (mobileOverlay) {
    mobileOverlay.addEventListener('click', toggleMobileMenu);
  }

  // Close mobile drawer when clicking a link
  document.querySelectorAll('.mobile-drawer a').forEach(link => {
    link.addEventListener('click', () => {
      if (mobileDrawer.classList.contains('open')) {
        toggleMobileMenu();
      }
    });
  });

  // 3. Hero Carousel Slider
  const heroSlides = document.querySelectorAll('.hero-slide');
  const heroDots = document.querySelectorAll('.slider-dot');
  const prevBtn = document.querySelector('.slider-arrow.prev');
  const nextBtn = document.querySelector('.slider-arrow.next');
  let currentHeroSlide = 0;
  let heroTimer = null;

  function showHeroSlide(index) {
    heroSlides.forEach((slide, i) => {
      slide.classList.toggle('active', i === index);
    });
    heroDots.forEach((dot, i) => {
      dot.classList.toggle('active', i === index);
    });
    currentHeroSlide = index;
  }

  function nextHeroSlide() {
    let nextIndex = (currentHeroSlide + 1) % heroSlides.length;
    showHeroSlide(nextIndex);
  }

  function prevHeroSlide() {
    let prevIndex = (currentHeroSlide - 1 + heroSlides.length) % heroSlides.length;
    showHeroSlide(prevIndex);
  }

  function startHeroTimer() {
    stopHeroTimer();
    heroTimer = setInterval(nextHeroSlide, 5000);
  }

  function stopHeroTimer() {
    if (heroTimer) clearInterval(heroTimer);
  }

  if (heroSlides.length > 0) {
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        nextHeroSlide();
        startHeroTimer();
      });
    }
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        prevHeroSlide();
        startHeroTimer();
      });
    }
    heroDots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        showHeroSlide(idx);
        startHeroTimer();
      });
    });

    const heroContainer = document.querySelector('.hero-slider-container');
    if (heroContainer) {
      heroContainer.addEventListener('mouseenter', stopHeroTimer);
      heroContainer.addEventListener('mouseleave', startHeroTimer);
    }

    startHeroTimer();
  }

  // 4. Stats Counter Animation (Odometer effect)
  const counterElements = document.querySelectorAll('.stat-number');
  let countersAnimated = false;

  function animateCounters() {
    counterElements.forEach(counter => {
      const target = parseInt(counter.getAttribute('data-target'), 10);
      const duration = 1600;
      const startTime = performance.now();

      function updateNumber(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing out cubic
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        const currentVal = Math.floor(easeProgress * target);

        counter.textContent = currentVal.toLocaleString();

        if (progress < 1) {
          requestAnimationFrame(updateNumber);
        } else {
          counter.textContent = target.toLocaleString();
        }
      }

      requestAnimationFrame(updateNumber);
    });
  }

  const statsSection = document.querySelector('.stats-section');
  if (statsSection && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !countersAnimated) {
          countersAnimated = true;
          animateCounters();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.25 });

    observer.observe(statsSection);
  } else {
    animateCounters();
  }

  // 5. About Us Tabs
  const aboutTabs = document.querySelectorAll('.about-tab-btn');
  const aboutPanes = document.querySelectorAll('.about-tab-pane');

  aboutTabs.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-tab');

      aboutTabs.forEach(b => b.classList.remove('active'));
      aboutPanes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const activePane = document.getElementById(targetId);
      if (activePane) {
        activePane.classList.add('active');
      }
    });
  });

  // 6. Testimonials Slider
  const tSlides = document.querySelectorAll('.testimonial-slide');
  const tDots = document.querySelectorAll('.t-dot');
  let currentTSlide = 0;
  let tTimer = null;

  function showTSlide(index) {
    tSlides.forEach((s, i) => s.classList.toggle('active', i === index));
    tDots.forEach((d, i) => d.classList.toggle('active', i === index));
    currentTSlide = index;
  }

  function nextTSlide() {
    let nextIdx = (currentTSlide + 1) % tSlides.length;
    showTSlide(nextIdx);
  }

  function startTTimer() {
    stopTTimer();
    tTimer = setInterval(nextTSlide, 6000);
  }

  function stopTTimer() {
    if (tTimer) clearInterval(tTimer);
  }

  if (tSlides.length > 0) {
    tDots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        showTSlide(idx);
        startTTimer();
      });
    });

    const tBox = document.querySelector('.testimonials-slider-box');
    if (tBox) {
      tBox.addEventListener('mouseenter', stopTTimer);
      tBox.addEventListener('mouseleave', startTTimer);
    }

    startTTimer();
  }

  // 7. Certificate Lightbox Modal
  const certModal = document.querySelector('.cert-modal-backdrop');
  const certModalImg = document.querySelector('.cert-modal-img');
  const certModalCaption = document.querySelector('.cert-modal-caption');
  const certModalClose = document.querySelector('.cert-modal-close');

  document.querySelectorAll('.affiliation-cert-wrapper').forEach(wrapper => {
    wrapper.addEventListener('click', () => {
      const img = wrapper.querySelector('img');
      const title = wrapper.closest('.affiliation-card').querySelector('.affiliation-title');
      if (img && certModal) {
        certModalImg.src = img.src;
        certModalCaption.textContent = title ? title.textContent : 'MMA-SFI Affiliation Certificate';
        certModal.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  function closeCertModal() {
    if (certModal) {
      certModal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  if (certModalClose) {
    certModalClose.addEventListener('click', closeCertModal);
  }
  if (certModal) {
    certModal.addEventListener('click', (e) => {
      if (e.target === certModal) {
        closeCertModal();
      }
    });
  }
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeCertModal();
  });

  // 8. Back to Top Button
  const backToTopBtn = document.querySelector('.back-to-top-btn');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  });

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});

