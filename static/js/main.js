const pageLoader = document.getElementById("page-loader");
const MIN_LOADER_MS = 500;
const FADE_OUT_MS = 260;
const LOADER_TS_KEY = "page_loader_shown_at";
let shownAt = 0;
let hideTimer = null;

function getStoredShownAt() {
    const raw = sessionStorage.getItem(LOADER_TS_KEY);
    const value = Number(raw);
    return Number.isFinite(value) && value > 0 ? value : 0;
}

function clearLoaderState() {
    shownAt = 0;
    sessionStorage.removeItem(LOADER_TS_KEY);
}

function ensureVisibleLoader() {
    if (!pageLoader) return;
    pageLoader.classList.remove("d-none");
    requestAnimationFrame(() => pageLoader.classList.add("is-visible"));
}

function showLoader() {
    if (!pageLoader) return;

    if (hideTimer) {
        clearTimeout(hideTimer);
        hideTimer = null;
    }

    shownAt = Date.now();
    sessionStorage.setItem(LOADER_TS_KEY, String(shownAt));
    ensureVisibleLoader();
}

function hideLoader() {
    if (!pageLoader) return;

    const startAt = shownAt || getStoredShownAt();
    if (!startAt) {
        pageLoader.classList.remove("is-visible");
        pageLoader.classList.add("d-none");
        return;
    }

    shownAt = startAt;
    ensureVisibleLoader();

    const elapsed = Date.now() - startAt;
    const wait = Math.max(0, MIN_LOADER_MS - elapsed);

    hideTimer = setTimeout(() => {
        pageLoader.classList.remove("is-visible");
        setTimeout(() => {
            pageLoader.classList.add("d-none");
            clearLoaderState();
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

function initLoadMoreLists() {
    const buttons = document.querySelectorAll(".js-load-more-btn");

    buttons.forEach((button) => {
        const section = button.closest("section") || document;
        const target = button.dataset.target || ".js-load-more-list";
        const list = section.querySelector(target);

        if (!list) return;

        const items = Array.from(list.querySelectorAll(".js-load-item"));
        const batchSize = Number(list.dataset.batchSize) || 10;
        let visibleCount = Math.min(batchSize, items.length);

        const sync = () => {
            items.forEach((item, index) => {
                item.hidden = index >= visibleCount;
            });

            button.hidden = visibleCount >= items.length;
        };

        sync();

        button.addEventListener("click", () => {
            visibleCount = Math.min(visibleCount + batchSize, items.length);
            sync();
        });
    });
}

window.addEventListener("pageshow", hideLoader);
window.addEventListener("load", () => {
    hideLoader();
    toggleScrolled();
});

window.addEventListener("DOMContentLoaded", () => {
    initGsapAnimations();
    initLoadMoreLists();
});
document.addEventListener("scroll", toggleScrolled);

// Internal linksda page loader ko'rsatish
// ignore: external links, hash-only anchors, special protocols, blank target
// and modified clicks.
document.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;

    const href = link.getAttribute("href") || "";
    const isExternal = link.origin !== window.location.origin;
    const hasHash = href.includes("#");
    const isSamePageHash = hasHash && link.origin === window.location.origin && link.pathname === window.location.pathname;
    const isSpecial = href.startsWith("mailto:") || href.startsWith("tel:") || href.startsWith("javascript:");
    const isBlank = link.target === "_blank";
    const isModified = event.ctrlKey || event.metaKey || event.shiftKey || event.altKey;

    // Hash (#...) linklar bo'limga sakrash uchun ishlatiladi.
    // Ayniqsa bir xil sahifada (/partners/#...) bo'lsa page loader qotib qolishi mumkin,
    // chunki sahifa qayta yuklanmaydi va `hideLoader()` chaqirilmaydi.
    if (!isExternal && !hasHash && !isSamePageHash && !isSpecial && !isBlank && !isModified) {
        showLoader();
    }
});
