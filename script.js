// Header scroll effect
const header = document.getElementById('main-header');
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// Smooth scroll for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 70,
                behavior: 'smooth'
            });
        }
    });
});

// Animation on scroll observer (Simple version)
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('appear');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('section').forEach(section => {
    section.style.opacity = "0";
    section.style.transform = "translateY(30px)";
    section.style.transition = "all 0.8s ease-out";
});

const observerForAnim = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = "1";
            entry.target.style.transform = "translateY(0)";
        }
    });
}, { threshold: 0.1 });

document.querySelectorAll('section').forEach(section => {
    observerForAnim.observe(section);
});

// Form submission (Mockup)
const contactForm = document.querySelector('.contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('문의가 성공적으로 접수되었습니다. 곧 연락드리겠습니다!');
        contactForm.reset();
    });
}

// Floor Plan Tab 전환
const fpTabs = document.querySelectorAll('.fp-tab');
const fpPanels = document.querySelectorAll('.fp-panel');

fpTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = tab.dataset.tab;

        // 탭 active 전환
        fpTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        // 패널 active 전환
        fpPanels.forEach(panel => {
            panel.classList.remove('active');
            if (panel.id === 'fp-' + target) {
                panel.classList.add('active');
            }
        });
    });
});
