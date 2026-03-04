const pageLoader = document.getElementById("page-loader");
const MIN_LOADER_MS = 550;
const FADE_OUT_MS = 260;
let shownAt = 0;
let hideTimer = null;

function showLoader() {
    if (!pageLoader) return;

    if (hideTimer) {
        clearTimeout(hideTimer);
        hideTimer = null;
    }

    shownAt = Date.now();
    pageLoader.classList.remove("d-none");
    requestAnimationFrame(() => pageLoader.classList.add("is-visible"));
}

function hideLoader() {
    if (!pageLoader) return;

    const elapsed = Date.now() - shownAt;
    const wait = Math.max(0, MIN_LOADER_MS - elapsed);

    hideTimer = setTimeout(() => {
        pageLoader.classList.remove("is-visible");
        setTimeout(() => {
            pageLoader.classList.add("d-none");
        }, FADE_OUT_MS);
    }, wait);
}

function toggleScrolled() {
    const selectBody = document.querySelector("body");
    const selectHeader = document.querySelector("#header");

    if (!selectHeader) return;

    const isSticky =
        selectHeader.classList.contains("scroll-up-sticky") ||
        selectHeader.classList.contains("sticky-top") ||
        selectHeader.classList.contains("fixed-top");

    if (!isSticky) return;

    if (window.scrollY > 100) {
        selectBody.classList.add("scrolled");
    } else {
        selectBody.classList.remove("scrolled");
    }
}

function initGsapAnimations() {
    if (!window.gsap) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    const cards = document.querySelectorAll(".page-content .card");

    if (cards.length) {
        window.gsap.from(cards, {
            opacity: 0,
            duration: 0.5,
            stagger: 0.08,
            delay: 0.15,
            ease: "power2.out",
        });
    }
}

window.addEventListener("pageshow", hideLoader);
window.addEventListener("load", () => {
    hideLoader();
    toggleScrolled();
});

window.addEventListener("DOMContentLoaded", initGsapAnimations);
document.addEventListener("scroll", toggleScrolled);

// Internal linksda page loader ko'rsatish
// ignore: external links, hash-only anchors, special protocols, blank target
// and modified clicks.
document.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;

    const href = link.getAttribute("href") || "";
    const isExternal = link.origin !== window.location.origin;
    const isHashOnly = href.startsWith("#");
    const isSpecial = href.startsWith("mailto:") || href.startsWith("tel:") || href.startsWith("javascript:");
    const isBlank = link.target === "_blank";
    const isModified = event.ctrlKey || event.metaKey || event.shiftKey || event.altKey;

    if (!isExternal && !isHashOnly && !isSpecial && !isBlank && !isModified) {
        showLoader();
    }
});
