// Página de disciplina: realça na barra de separadores a secção visível.
(function () {
  var links = [].slice.call(document.querySelectorAll(".seccoes a[href^='#']"));
  var seccoes = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); });
  function marca() {
    var y = window.scrollY + 140, i = 0;
    seccoes.forEach(function (s, k) { if (s && s.getBoundingClientRect().top + window.scrollY <= y) i = k; });
    if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 4) i = seccoes.length - 1;
    links.forEach(function (a, k) {
      if (k === i) {
        a.setAttribute("aria-current", "true");
        var barra = a.parentNode;
        if (a.offsetLeft < barra.scrollLeft || a.offsetLeft + a.offsetWidth > barra.scrollLeft + barra.clientWidth)
          barra.scrollLeft = a.offsetLeft - 16;
      } else a.removeAttribute("aria-current");
    });
  }
  window.addEventListener("scroll", marca, { passive: true });
  marca();
})();
