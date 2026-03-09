document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (mobileBtn && navMenu) {
        mobileBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            // Toggle icon between bars and times
            const icon = mobileBtn.querySelector('i');
            if(navMenu.classList.contains('active')){
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Sticky Header
    const header = document.getElementById('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Smooth scrolling for Anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if(this.getAttribute('href') !== '#') {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                
                if (target) {
                    // Close mobile menu if open
                    if (navMenu.classList.contains('active')) {
                        navMenu.classList.remove('active');
                        mobileBtn.querySelector('i').classList.remove('fa-xmark');
                        mobileBtn.querySelector('i').classList.add('fa-bars');
                    }

                    // Account for fixed header offset
                    const headerHeight = header.offsetHeight;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerHeight;
            
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: "smooth"
                    });
                }
            }
        });
    });

    // Page Transition In
    setTimeout(() => {
        document.body.classList.add('loaded');
    }, 50); // slight delay to ensure rendering

    // Page Transition Out for internal links
    const internalLinks = document.querySelectorAll('a[href]:not([target="_blank"]):not([href^="#"]):not([href^="mailto:"]):not([href^="tel:"])');
    
    internalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Prevent default rapid navigation
            e.preventDefault();
            
            const targetUrl = this.getAttribute('href');
            
            // Remove the loaded class to trigger fade out
            document.body.classList.remove('loaded');
            
            // Wait for transition to finish before actually changing page
            setTimeout(() => {
                window.location.href = targetUrl;
            }, 400); // 400ms matches the CSS transition time
        });
    });
});
