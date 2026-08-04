(() => {
  "use strict";

  const root = document.documentElement;
  const progress = document.getElementById("reading-progress");
  const progressRegion = progress?.parentElement;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let progressFrame = 0;

  const updateProgress = () => {
    const scrollRange = root.scrollHeight - window.innerHeight;
    const ratio = scrollRange > 0 ? Math.min(Math.max(window.scrollY / scrollRange, 0), 1) : 0;
    if (progress) progress.style.transform = `scaleX(${ratio})`;
    if (progressRegion) progressRegion.setAttribute("aria-valuenow", String(Math.round(ratio * 100)));
    progressFrame = 0;
  };

  const requestProgressUpdate = () => {
    if (!progressFrame) progressFrame = window.requestAnimationFrame(updateProgress);
  };

  window.addEventListener("scroll", requestProgressUpdate, { passive: true });
  window.addEventListener("resize", requestProgressUpdate);
  updateProgress();

  document.querySelectorAll("[data-copy]").forEach((button) => {
    const initialLabel = button.textContent;
    button.addEventListener("click", async () => {
      const value = button.getAttribute("data-copy") || "";
      try {
        if (!navigator.clipboard?.writeText) throw new Error("clipboard unavailable");
        await navigator.clipboard.writeText(value);
        button.textContent = "已复制";
      } catch (_error) {
        button.textContent = "请手动复制";
      }
      window.setTimeout(() => {
        button.textContent = initialLabel;
      }, 1800);
    });
  });

  if (!reduceMotion && "IntersectionObserver" in window) {
    root.classList.add("motion-ok");
    const revealItems = document.querySelectorAll("[data-reveal]");
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove("is-pending");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8%", threshold: 0.08 });

    revealItems.forEach((item) => {
      if (item.getBoundingClientRect().top > window.innerHeight * 0.88) {
        item.classList.add("is-pending");
        revealObserver.observe(item);
      }
    });
  }

  if ("IntersectionObserver" in window) {
    const railLinks = new Map(
      [...document.querySelectorAll(".method-rail a[href^='#']")].map((link) => [link.getAttribute("href")?.slice(1), link])
    );
    const modules = document.querySelectorAll("[data-module]");
    const locationObserver = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];
      if (!visible) return;
      railLinks.forEach((link) => link.removeAttribute("aria-current"));
      railLinks.get(visible.target.id)?.setAttribute("aria-current", "location");
    }, { rootMargin: "-18% 0px -58%", threshold: [0, 0.2, 0.55] });
    modules.forEach((module) => locationObserver.observe(module));
  }
})();
