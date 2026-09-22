/* BiLoans.com — core site script */
(function () {
  "use strict";
  var C = window.BL_CONFIG || {};
  var store = {
    get: function (k, s) { try { return (s ? sessionStorage : localStorage).getItem(k); } catch (e) { return null; } },
    set: function (k, v, s) { try { (s ? sessionStorage : localStorage).setItem(k, v); } catch (e) {} }
  };
  window.BL_STORE = store;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- theme ---------- */
  var saved = store.get("bl-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  else if (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches) document.documentElement.setAttribute("data-theme", "dark");
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (!t) return;
    var cur = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", cur);
    store.set("bl-theme", cur);
  });

  document.addEventListener("DOMContentLoaded", function () {
    /* ---------- nav ---------- */
    var burger = $(".burger"), menu = $(".menu");
    if (burger && menu) burger.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    $$("[data-rates-asof]").forEach(function (el) { el.textContent = C.ratesAsOf || ""; });

    /* ---------- UTM capture ---------- */
    var q = new URLSearchParams(location.search);
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid"].forEach(function (k) {
      if (q.get(k)) store.set("bl-" + k, q.get(k), true);
    });
    if (!store.get("bl-landing", true)) { store.set("bl-landing", location.pathname, true); store.set("bl-ref", document.referrer || "direct", true); }

    /* ---------- cookie consent ---------- */
    var cookie = $("#cookie");
    var consent = store.get("bl-consent");
    if (cookie && !consent) cookie.classList.add("show");
    $$("[data-consent]").forEach(function (b) {
      b.addEventListener("click", function () {
        store.set("bl-consent", b.getAttribute("data-consent"));
        cookie.classList.remove("show");
        initAds();
      });
    });

    /* ---------- ads ---------- */
    initAds();

    /* ---------- YouTube facade ---------- */
    $$(".yt[data-id]").forEach(function (el) {
      var id = el.getAttribute("data-id");
      if (!id) return;
      el.style.backgroundImage = "url(https://i.ytimg.com/vi/" + id + "/hqdefault.jpg)";
      el.addEventListener("click", function () {
        el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (el.getAttribute("data-title") || "Video") + '" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>';
      }, { once: true });
    });
    if (C.youtube && C.youtube.featured && C.youtube.featured.id) {
      $$("[data-featured-video]").forEach(function (el) {
        el.innerHTML = '<div class="yt" data-id="' + C.youtube.featured.id + '"><div class="play"><b>▶</b></div></div>';
        var y = el.firstChild; y.style.backgroundImage = "url(https://i.ytimg.com/vi/" + C.youtube.featured.id + "/hqdefault.jpg)";
        y.addEventListener("click", function () { y.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + C.youtube.featured.id + '?autoplay=1&rel=0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'; }, { once: true });
      });
    }

    /* ---------- tabs ---------- */
    $$("[data-tabs]").forEach(function (wrap) {
      var btns = $$("[data-tab]", wrap);
      btns.forEach(function (b) {
        b.addEventListener("click", function () {
          btns.forEach(function (x) { x.classList.remove("active"); x.setAttribute("aria-selected", "false"); });
          b.classList.add("active"); b.setAttribute("aria-selected", "true");
          var scope = wrap.getAttribute("data-tabs") ? document.getElementById(wrap.getAttribute("data-tabs")) : document;
          $$(".tabpanel", scope).forEach(function (p) { p.classList.toggle("active", p.id === b.getAttribute("data-tab")); });
          if (history.replaceState && wrap.hasAttribute("data-hash")) history.replaceState(null, "", "#" + b.getAttribute("data-tab"));
        });
      });
      if (wrap.hasAttribute("data-hash") && location.hash) {
        var hb = $('[data-tab="' + location.hash.slice(1) + '"]', wrap);
        if (hb) hb.click();
      }
    });

    /* ---------- segmented control (hero) ---------- */
    $$(".seg").forEach(function (seg) {
      var input = document.getElementById(seg.getAttribute("data-input"));
      $$("button", seg).forEach(function (b) {
        b.addEventListener("click", function () {
          $$("button", seg).forEach(function (x) { x.classList.remove("active"); });
          b.classList.add("active");
          if (input) input.value = b.getAttribute("data-val");
          var lbl = $("[data-seg-label]");
          if (lbl) lbl.textContent = b.getAttribute("data-label") || "";
        });
      });
    });

    /* ---------- sortable tables ---------- */
    $$("table[data-sortable]").forEach(function (tbl) {
      $$("th.sortable", tbl).forEach(function (th, idx) {
        var dir = 1;
        th.addEventListener("click", function () {
          var col = Array.prototype.indexOf.call(th.parentNode.children, th);
          var body = tbl.tBodies[0];
          var rows = $$("tr", body);
          rows.sort(function (a, b) {
            var x = a.children[col].getAttribute("data-v") || a.children[col].textContent;
            var y = b.children[col].getAttribute("data-v") || b.children[col].textContent;
            var nx = parseFloat(x), ny = parseFloat(y);
            if (!isNaN(nx) && !isNaN(ny)) return (nx - ny) * dir;
            return x.localeCompare(y) * dir;
          });
          dir = -dir;
          rows.forEach(function (r) { body.appendChild(r); });
        });
      });
    });
    /* table filters */
    $$("[data-filter-table]").forEach(function (ctrl) {
      var tbl = document.getElementById(ctrl.getAttribute("data-filter-table"));
      var apply = function () {
        var sels = $$("[data-filter-table='" + tbl.id + "']");
        $$("tbody tr", tbl).forEach(function (r) {
          var show = sels.every(function (s) {
            var v = s.value.toLowerCase(); if (!v || v === "all") return true;
            var attr = r.getAttribute("data-" + s.getAttribute("data-key")) || r.textContent;
            return attr.toLowerCase().indexOf(v) > -1;
          });
          r.style.display = show ? "" : "none";
        });
      };
      ctrl.addEventListener("input", apply); ctrl.addEventListener("change", apply);
    });

    /* ---------- reveal on scroll ---------- */
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }); }, { threshold: .08 });
      $$(".reveal").forEach(function (el) { io.observe(el); });
    } else $$(".reveal").forEach(function (el) { el.classList.add("in"); });

    /* ---------- exit intent ---------- */
    var modal = $("#exitModal");
    if (modal && window.innerWidth > 900 && !store.get("bl-exit", true)) {
      document.addEventListener("mouseout", function h(e) {
        if (!e.relatedTarget && e.clientY < 10) {
          modal.classList.add("show"); store.set("bl-exit", "1", true);
          document.removeEventListener("mouseout", h);
        }
      });
    }
    $$(".modal .x, [data-close-modal]").forEach(function (b) { b.addEventListener("click", function () { b.closest(".modal").classList.remove("show"); }); });

    /* ---------- donation amount chips ---------- */
    $$("[data-amount]").forEach(function (b) {
      b.addEventListener("click", function () {
        var inp = document.getElementById("donAmount"); if (inp) { inp.value = b.getAttribute("data-amount"); inp.dispatchEvent(new Event("input")); }
        $$("[data-amount]").forEach(function (x) { x.classList.remove("btn-primary"); x.classList.add("btn-ghost"); });
        b.classList.add("btn-primary"); b.classList.remove("btn-ghost");
      });
    });
    /* goals */
    var goalsEl = $("#goals");
    if (goalsEl && C.goals) {
      goalsEl.innerHTML = C.goals.map(function (g) {
        var pct = Math.min(100, Math.round((g.raised / g.target) * 100));
        return '<div class="goal"><div style="display:flex;justify-content:space-between"><strong>' + g.key + '</strong><span class="muted">$' + g.raised.toLocaleString() + " / $" + g.target.toLocaleString() + '</span></div><div class="bar"><i style="width:' + Math.max(pct, 2) + '%"></i></div></div>';
      }).join("");
    }
    /* payment links */
    $$("[data-pay]").forEach(function (a) {
      var url = C.payments && C.payments[a.getAttribute("data-pay")];
      if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; } else a.style.display = "none";
    });
    $$("[data-social]").forEach(function (a) { var u = C.social && C.social[a.getAttribute("data-social")]; if (u) a.href = u; });

    /* ---------- forms ---------- */
    $$("form[data-bl-form]:not(#leadForm)").forEach(bindForm);
  });

  /* ================= ADS ================= */
  var adsLoaded = false;
  function initAds() {
    var slots = $$(".ad-slot");
    if (!slots.length) return;
    var consent = store.get("bl-consent");
    if (C.adsenseClient && consent) {
      if (!adsLoaded) {
        var s = document.createElement("script");
        s.async = true; s.crossOrigin = "anonymous";
        s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
        document.head.appendChild(s); adsLoaded = true;
      }
      slots.forEach(function (el) {
        if (el.getAttribute("data-filled")) return;
        var slot = (C.adsenseSlots || {})[el.getAttribute("data-slot")] || "";
        el.innerHTML = '<div class="ad-label">Advertisement</div><ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '"' + (slot ? ' data-ad-slot="' + slot + '"' : "") + ' data-ad-format="auto" data-full-width-responsive="true"' + (consent === "essential" ? ' data-npa="1"' : "") + "></ins>";
        el.setAttribute("data-filled", "1");
        try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
      });
    } else {
      var root = document.body.getAttribute("data-root") || "";
      slots.forEach(function (el) {
        if (el.getAttribute("data-filled")) return;
        el.innerHTML = '<div class="ad-label">Sponsored</div><div class="house-ad"><div><strong>Reach borrowers when they are ready to decide.</strong><br><span class="muted">This space is available for lenders, fintechs and advisors.</span></div><a class="btn btn-sm btn-primary" href="' + root + 'advertise.html">Advertise here</a></div>';
        el.setAttribute("data-filled", "house");
      });
    }
  }

  /* ================= FORMS ================= */
  function endpoint() {
    var id = C.formAlias || String.fromCharCode.apply(null, [126, 108, 105, 126, 118, 121, 114, 122, 104, 56, 71, 110, 116, 104, 112, 115, 53, 106, 118, 116].map(function (c) { return c - 7; }));
    return "https://formsubmit.co/ajax/" + id;
  }
  window.BL_ENDPOINT = endpoint;

  function collect(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (k === "_honey") return;
      data[k] = data[k] ? data[k] + ", " + v : v;
    });
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid"].forEach(function (k) { var v = store.get("bl-" + k, true); if (v) data[k] = v; });
    data.landing_page = store.get("bl-landing", true) || "";
    data.referrer = store.get("bl-ref", true) || "";
    data.page = location.href;
    data.submitted_at = new Date().toISOString();
    data._subject = "[BiLoans] " + (form.getAttribute("data-bl-form") || "Form") + " submission";
    data._template = "table";
    data._captcha = "false";
    return data;
  }

  function send(data) {
    return fetch(endpoint(), {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(data)
    }).then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json().catch(function () { return {}; }); });
  }
  window.BL_SEND = function (form, extra) {
    var d = collect(form); Object.keys(extra || {}).forEach(function (k) { d[k] = extra[k]; }); return send(d);
  };

  function bindForm(form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var msg = form.querySelector(".form-msg");
      var hp = form.querySelector("[name=_honey]");
      if (hp && hp.value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector("[type=submit]");
      var label = btn ? btn.innerHTML : "";
      if (btn) { btn.disabled = true; btn.innerHTML = "Sending…"; }
      send(collect(form)).then(function () {
        if (msg) { msg.className = "form-msg ok"; msg.textContent = form.getAttribute("data-ok") || "Thank you! We received your message and will reply shortly."; }
        form.reset();
      }).catch(function () {
        if (msg) { msg.className = "form-msg err"; msg.textContent = "Sorry, something went wrong. Please try again in a moment or use the contact page."; }
      }).then(function () { if (btn) { btn.disabled = false; btn.innerHTML = label; } });
    });
  }
})();
