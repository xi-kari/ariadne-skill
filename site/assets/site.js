(() => {
  "use strict";

  // 基态即完成态：本文件只做增强，任何失败都不影响内容可读。
  const root = document.documentElement;
  root.classList.add("js-on");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // 复制按钮：仅在 JS 可用时注入；无 JS 时命令仍可手动选中复制。
  document.querySelectorAll("[data-copy-card]").forEach((card) => {
    const code = card.querySelector("pre code");
    const head = card.querySelector(".op-head");
    if (!code || !head) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy-btn";
    button.textContent = "复制";
    const live = document.createElement("span");
    live.className = "visually-hidden";
    live.setAttribute("aria-live", "polite");
    head.appendChild(button);
    head.appendChild(live);
    let timer = 0;
    button.addEventListener("click", async () => {
      try {
        if (!navigator.clipboard || !navigator.clipboard.writeText) {
          throw new Error("clipboard unavailable");
        }
        await navigator.clipboard.writeText(code.textContent.trim());
        button.textContent = "已复制";
        live.textContent = "命令已复制到剪贴板";
      } catch (_error) {
        button.textContent = "请手动复制";
        live.textContent = "复制失败，请手动选中命令复制";
      }
      window.clearTimeout(timer);
      timer = window.setTimeout(() => {
        button.textContent = "复制";
        live.textContent = "";
      }, 1800);
    });
  });

  // 导航位置指示：当前阅读的图纸在顶栏落墨。
  if ("IntersectionObserver" in window) {
    const links = new Map(
      [...document.querySelectorAll(".bar-links a[href^='#']")].map((link) => [
        link.getAttribute("href").slice(1),
        link,
      ])
    );
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((left, right) => right.intersectionRatio - left.intersectionRatio)[0];
        if (!visible) return;
        links.forEach((link) => link.removeAttribute("aria-current"));
        const link = links.get(visible.target.id);
        if (link) link.setAttribute("aria-current", "location");
      },
      { rootMargin: "-18% 0px -58%", threshold: [0, 0.2, 0.5] }
    );
    links.forEach((_link, id) => {
      const section = document.getElementById(id);
      if (section) observer.observe(section);
    });
  }

  // 封面红线描画：reduce 或无 JS 时，线在基态即画满。
  if (!reduceMotion) {
    const thread = document.querySelector(".hero-lattice .thread");
    if (thread && typeof thread.getTotalLength === "function") {
      const length = Math.ceil(thread.getTotalLength());
      thread.style.strokeDasharray = String(length);
      thread.style.strokeDashoffset = String(length);
      window.requestAnimationFrame(() => {
        window.requestAnimationFrame(() => {
          thread.style.strokeDashoffset = "0";
        });
      });
    }
  }
})();
