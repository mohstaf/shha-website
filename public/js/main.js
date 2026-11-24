/* SHHA website: small enhancements only. Every page works without this file. */

/* Where form submissions go. Paste the endpoint from your form service
   (for example Formspree: https://formspree.io/f/xxxxxxx). Each form can also
   set its own with data-endpoint="...". While this is empty, forms show the
   WhatsApp and email alternatives instead of sending. */
const FORM_ENDPOINT = "";

document.addEventListener("DOMContentLoaded", () => {
  document.documentElement.classList.add("js");
  setupNav();
  setupSelects();
  setupReveal();
  setupHeader();
  setupToc();
  setupShowcase();
  setupRotator();
  setupTheme();
  setupFilters();
  setupForms();
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });
});

function setupNav() {
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.getElementById("site-nav");
  if (!toggle || !nav) return;

  const setOpen = (open) => {
    toggle.setAttribute("aria-expanded", String(open));
    nav.classList.toggle("is-open", open);
  };
  toggle.addEventListener("click", () => setOpen(toggle.getAttribute("aria-expanded") !== "true"));
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && nav.classList.contains("is-open")) {
      setOpen(false);
      toggle.focus();
    }
  });
  nav.addEventListener("click", (e) => {
    if (e.target.closest("a")) setOpen(false);
  });
}

function setupHeader() {
  const header = document.querySelector(".site-header");
  if (!header) return;
  const update = () => header.classList.toggle("is-scrolled", window.scrollY > 8);
  update();
  window.addEventListener("scroll", update, { passive: true });
}

/* Scroll showcase: highlight the condition whose details are in view.
   Without the script every panel simply shows in full. */
function setupShowcase() {
  document.querySelectorAll("[data-showcase]").forEach((root) => {
    const links = [...root.querySelectorAll(".showcase__tab")];
    const panels = [...root.querySelectorAll(".showcase__panel")];
    if (!panels.length || !("IntersectionObserver" in window)) return;
    const activate = (panel) => {
      panels.forEach((p) => p.classList.toggle("is-active", p === panel));
      links.forEach((a) => {
        const on = a.getAttribute("href") === `#${panel.id}`;
        a.classList.toggle("is-active", on);
        if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
      });
    };
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && activate(e.target)),
      { rootMargin: "-40% 0px -55% 0px" }
    );
    panels.forEach((p) => observer.observe(p));
    activate(panels[0]);
    root.classList.add("is-ready");
  });
}

/* Hero: the red word retypes itself through each word once, then rests on the
   first word. Hovering the headline plays it again. The photos change with the
   word and drift slightly with the mouse (not with reduced motion). */
function setupRotator() {
  const hero = document.querySelector("[data-hero]");
  const el = document.querySelector(".rotator");
  if (!el) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const words = el.dataset.words.split("|");
  const box = el.querySelector(".rotator__word");
  const text = el.querySelector(".rotator__text");
  const pics = [...document.querySelectorAll(".word-pic")];
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));

  document.querySelectorAll(".hero h1 .w").forEach((w, i) => w.style.setProperty("--i", i));

  // The box follows each word's width, so the line never has a gap.
  // It glides to the next word's width before typing starts.
  const measure = (w) => {
    const current = text.textContent;
    text.textContent = w;
    const width = Math.ceil(text.getBoundingClientRect().width);
    text.textContent = current;
    return width;
  };
  let target = text.textContent;
  const fit = (w) => { target = w; box.style.width = `${measure(w)}px`; };
  fit(target);
  (document.fonts?.ready || Promise.resolve()).then(() => fit(target));
  window.addEventListener("resize", () => fit(target));

  const swapPhotos = () => pics.forEach((p, k) => setTimeout(() => p.classList.toggle("is-swapped"), k * 220));

  const typeTo = async (next) => {
    el.classList.remove("is-landing");
    el.classList.add("is-typing");
    for (let n = text.textContent.length; n > 0; n--) { text.textContent = text.textContent.slice(0, -1); await wait(45); }
    swapPhotos();
    fit(next);
    await wait(420);
    for (let n = 1; n <= next.length; n++) { text.textContent = next.slice(0, n); await wait(85); }
    el.classList.remove("is-typing");
    void el.offsetWidth;
    el.classList.add("is-landing");
  };

  let running = false;
  const play = async () => {
    if (running) return;
    running = true;
    el.classList.add("is-active");
    for (let k = 1; k <= words.length; k++) {
      await wait(2600);
      await typeTo(words[k % words.length]);
    }
    el.classList.remove("is-active");
    running = false;
  };
  setTimeout(play, 600);
  document.querySelector(".hero h1")?.addEventListener("mouseenter", play);

  if (hero && !reduce && window.matchMedia("(hover: hover)").matches) {
    let frame = 0;
    hero.addEventListener("mousemove", (e) => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const r = hero.getBoundingClientRect();
        hero.style.setProperty("--mx", ((e.clientX - r.left) / r.width - 0.5) * 2);
        hero.style.setProperty("--my", ((e.clientY - r.top) / r.height - 0.5) * 2);
      });
    });
    hero.addEventListener("mouseleave", () => {
      hero.style.setProperty("--mx", 0);
      hero.style.setProperty("--my", 0);
    });
  }
}

/* Filter pills: show only list items whose data-topic matches. */
function setupFilters() {
  document.querySelectorAll("[data-filter-list]").forEach((bar) => {
    const list = document.getElementById(bar.dataset.filterList);
    if (!list) return;
    const items = [...list.children];
    const buttons = [...bar.querySelectorAll("[data-filter]")];
    buttons.forEach((btn) => {
      const topic = btn.dataset.filter;
      const count = topic === "all" ? items.length : items.filter((li) => li.dataset.topic === topic).length;
      const badge = document.createElement("span");
      badge.textContent = count;
      btn.appendChild(badge);
      btn.addEventListener("click", () => {
        buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
        items.forEach((li) => { li.hidden = topic !== "all" && li.dataset.topic !== topic; });
      });
    });
    bar.hidden = false;
  });
}

function setupToc() {
  const links = [...document.querySelectorAll(".toc a[href^='#']")];
  if (!links.length || !("IntersectionObserver" in window)) return;
  const byId = new Map(links.map((a) => [a.getAttribute("href").slice(1), a]));
  const sections = [...byId.keys()].map((id) => document.getElementById(id)).filter(Boolean);

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((a) => a.classList.remove("is-active"));
        byId.get(entry.target.id)?.classList.add("is-active");
      });
    },
    { rootMargin: "-20% 0px -70% 0px" }
  );
  sections.forEach((s) => observer.observe(s));
}

/* Custom dropdowns. The real <select> stays in the form (hidden) so values
   submit and validate as normal; the button and list are only the look. */
function setupSelects() {
  document.querySelectorAll("form select").forEach((sel) => {
    const wrap = document.createElement("div");
    wrap.className = "select";
    sel.parentNode.insertBefore(wrap, sel);
    wrap.appendChild(sel);
    sel.classList.add("select__native");
    sel.tabIndex = -1;
    sel.setAttribute("aria-hidden", "true");

    const label = document.querySelector(`label[for="${sel.id}"]`);
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "select__button";
    btn.id = `${sel.id}-button`;
    btn.setAttribute("aria-haspopup", "listbox");
    btn.setAttribute("aria-expanded", "false");
    const list = document.createElement("ul");
    list.className = "select__list";
    list.id = `${sel.id}-list`;
    list.setAttribute("role", "listbox");
    list.tabIndex = -1;
    list.hidden = true;
    btn.setAttribute("aria-controls", list.id);
    if (label) {
      label.id ||= `${sel.id}-label`;
      label.htmlFor = btn.id;
      btn.setAttribute("aria-labelledby", `${label.id} ${btn.id}`);
      list.setAttribute("aria-labelledby", label.id);
    }

    [...sel.options].forEach((o, i) => {
      if (o.value === "") return;
      const li = document.createElement("li");
      li.className = "select__option";
      li.setAttribute("role", "option");
      li.id = `${sel.id}-opt-${i}`;
      li.dataset.index = i;
      li.textContent = o.textContent;
      list.appendChild(li);
    });
    wrap.append(btn, list);
    const items = [...list.children];
    let active = -1;

    const render = () => {
      const o = sel.options[sel.selectedIndex];
      btn.textContent = o ? o.textContent : "";
      btn.classList.toggle("is-placeholder", !sel.value);
      items.forEach((li) => li.setAttribute("aria-selected", String(+li.dataset.index === sel.selectedIndex)));
    };
    const setActive = (i) => {
      active = i;
      items.forEach((li, k) => li.classList.toggle("is-active", k === i));
      if (items[i]) {
        list.setAttribute("aria-activedescendant", items[i].id);
        items[i].scrollIntoView({ block: "nearest" });
      }
    };
    const open = () => {
      list.hidden = false;
      wrap.classList.add("is-open");
      btn.setAttribute("aria-expanded", "true");
      const cur = items.findIndex((li) => +li.dataset.index === sel.selectedIndex);
      setActive(cur >= 0 ? cur : 0);
      list.focus();
    };
    const close = (focus = true) => {
      list.hidden = true;
      wrap.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
      if (focus) btn.focus();
    };
    const choose = (i) => {
      if (!items[i]) return;
      sel.selectedIndex = +items[i].dataset.index;
      sel.dispatchEvent(new Event("change", { bubbles: true }));
      close();
    };

    btn.addEventListener("click", () => (list.hidden ? open() : close()));
    btn.addEventListener("keydown", (e) => {
      if (["ArrowDown", "ArrowUp", "Enter", " "].includes(e.key)) { e.preventDefault(); open(); }
    });
    list.addEventListener("keydown", (e) => {
      if (e.key === "ArrowDown") { e.preventDefault(); setActive(Math.min(active + 1, items.length - 1)); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive(Math.max(active - 1, 0)); }
      else if (e.key === "Home") { e.preventDefault(); setActive(0); }
      else if (e.key === "End") { e.preventDefault(); setActive(items.length - 1); }
      else if (e.key === "Enter" || e.key === " ") { e.preventDefault(); choose(active); }
      else if (e.key === "Escape") { e.preventDefault(); close(); }
      else if (e.key === "Tab") { close(false); }
      else if (e.key.length === 1) {
        const k = items.findIndex((li) => li.textContent.toLowerCase().startsWith(e.key.toLowerCase()));
        if (k >= 0) setActive(k);
      }
    });
    list.addEventListener("click", (e) => {
      const li = e.target.closest(".select__option");
      if (li) choose(items.indexOf(li));
    });
    list.addEventListener("mousemove", (e) => {
      const li = e.target.closest(".select__option");
      if (li && items.indexOf(li) !== active) setActive(items.indexOf(li));
    });
    document.addEventListener("click", (e) => { if (!wrap.contains(e.target) && !list.hidden) close(false); });
    sel.addEventListener("change", render);
    sel.form?.addEventListener("reset", () => setTimeout(render));
    render();
  });
}

/* Content fades gently into place as it scrolls into view
   (a plain fade, without movement, when the visitor prefers less motion). */
function setupReveal() {
  if (!("IntersectionObserver" in window)) return;
  const targets = document.querySelectorAll(
    ".section-head, .prog__item, .feature, .zig, .news-card, .facts li, .steps li, .days li, .topic, .channel, .faq details, .route, .bento__photo, .res li, .dl-rows div, .alert-list li, .pubs li, .prose > section, .closing__inner"
  );
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("is-in");
      io.unobserve(entry.target);
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  targets.forEach((el) => {
    if (el.getBoundingClientRect().top < window.innerHeight * 0.92) return;
    const siblings = [...el.parentElement.children];
    el.style.setProperty("--d", `${(siblings.indexOf(el) % 4) * 70}ms`);
    el.classList.add("reveal");
    io.observe(el);
  });
}

function setupForms() {
  document.querySelectorAll("form[data-form]").forEach((form) => {
    const status = form.querySelector(".form__status");

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (!validate(form)) return;

      const endpoint = form.dataset.endpoint || FORM_ENDPOINT;
      if (!endpoint) {
        show(status, "info",
          "Online forms are not connected yet. Please send the same details on WhatsApp to " +
          "+252 61 855 6681 or email info@shha.so, and we will reply.");
        return;
      }

      const button = form.querySelector("[type=submit]");
      button.disabled = true;
      try {
        const res = await fetch(endpoint, {
          method: "POST",
          body: new FormData(form),
          headers: { Accept: "application/json" },
        });
        if (!res.ok) throw new Error(res.status);
        form.reset();
        show(status, "ok", form.dataset.success || "Thank you. Your message has reached SHHA and we will reply soon.");
      } catch {
        show(status, "info",
          "Your message could not be sent. Please try again, or contact us on WhatsApp +252 61 855 6681.");
      } finally {
        button.disabled = false;
      }
    });
  });
}

function validate(form) {
  let firstBad = null;
  form.querySelectorAll("[required]").forEach((input) => {
    const field = input.closest(".field") || input.closest(".check")?.parentElement;
    const ok = input.type === "checkbox" ? input.checked : input.value.trim() !== "" && input.checkValidity();
    input.setAttribute("aria-invalid", String(!ok));
    const custom = input.closest(".select")?.querySelector(".select__button");
    if (custom) custom.setAttribute("aria-invalid", String(!ok));
    let err = field?.querySelector(".field__error");
    if (!ok) {
      if (!err && field) {
        err = document.createElement("span");
        err.className = "field__error";
        err.id = `${input.id || input.name}-error`;
        field.appendChild(err);
        input.setAttribute("aria-describedby", [input.getAttribute("aria-describedby"), err.id].filter(Boolean).join(" "));
        if (custom) custom.setAttribute("aria-describedby", err.id);
      }
      if (err) err.textContent = input.dataset.error || "Please fill this in.";
      firstBad ||= custom || input;
    } else if (err) {
      err.textContent = "";
    }
  });
  if (firstBad) firstBad.focus();
  return !firstBad;
}

function show(el, kind, message) {
  if (!el) return;
  el.className = `form__status form__status--${kind}`;
  el.textContent = message;
  el.hidden = false;
  el.setAttribute("role", "status");
  el.scrollIntoView({ block: "nearest", behavior: "smooth" });
}

// Light and dark theme. The choice is remembered on this device.
function setupTheme() {
  const btn = document.querySelector("[data-theme-toggle]");
  if (!btn) return;
  const root = document.documentElement;
  // Each illustration has a dark version (name-dark.svg); swap to match the theme.
  const art = () => document.querySelectorAll('img[src*="img/art/"]').forEach((img) => {
    const src = img.getAttribute("src");
    const next = root.dataset.theme === "dark" ? src.replace(/(-dark)?\.svg/, "-dark.svg") : src.replace("-dark.svg", ".svg");
    if (next !== src) img.setAttribute("src", next);
  });
  art();
  const label = () => btn.setAttribute("aria-label", root.dataset.theme === "dark" ? "Switch to light theme" : "Switch to dark theme");
  label();
  btn.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
    try { localStorage.setItem("shha-theme", root.dataset.theme); } catch (e) {}
    label();
    art();
  });
}
