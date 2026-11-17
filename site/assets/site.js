(() => {
  "use strict";
  // Content and navigation remain complete without JavaScript.
  document.querySelectorAll("[data-copy-card]").forEach((card) => {
    const code = card.querySelector("pre code");
    const head = card.querySelector(".code-head");
    if (!code || !head) return;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy-button";
    button.textContent = "复制命令";
    const status = document.createElement("span");
    status.className = "visually-hidden";
    status.setAttribute("role", "status");
    head.append(button, status);
    let timer;
    button.addEventListener("click", async () => {
      try {
        if (!navigator.clipboard?.writeText) throw new Error("Clipboard unavailable");
        await navigator.clipboard.writeText(code.textContent.trim());
        button.textContent = "已复制";
        status.textContent = "安装命令已复制到剪贴板。";
      } catch (_error) {
        button.textContent = "请手动复制";
        status.textContent = "无法访问剪贴板，请选中下方命令复制。";
      }
      window.clearTimeout(timer);
      timer = window.setTimeout(() => {
        button.textContent = "复制命令";
        status.textContent = "";
      }, 2400);
    });
  });
  if (!("IntersectionObserver" in window)) return;
  const links = [...document.querySelectorAll(".nav-links a[href^='#']")];
  const sections = links.map((link) => document.getElementById(link.hash.slice(1))).filter(Boolean);
  const visible = new Set();
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => entry.isIntersecting ? visible.add(entry.target.id) : visible.delete(entry.target.id));
    const current = sections.filter((section) => visible.has(section.id)).pop();
    links.forEach((link) => {
      if (current && link.hash === `#${current.id}`) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  }, { rootMargin: "-15% 0px -55% 0px", threshold: 0 });
  sections.forEach((section) => observer.observe(section));
})();
