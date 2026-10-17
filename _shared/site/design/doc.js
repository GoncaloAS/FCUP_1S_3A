// Documento: índice aberto em ecrãs largos, secção atual realçada no índice,
// índice fecha-se ao escolher uma secção no telemóvel, botão para o topo.
(function () {
  var det = document.getElementById("doc-indice-det");
  var largo = matchMedia("(min-width: 1040px)");
  function ajusta() { if (det) det.open = largo.matches; }
  ajusta();
  largo.addEventListener("change", ajusta);

  var links = [].slice.call(document.querySelectorAll(".doc-indice a[href^='#']"));
  var porId = {};
  links.forEach(function (a) {
    porId[decodeURIComponent(a.getAttribute("href").slice(1))] = a;
    a.addEventListener("click", function () { if (!largo.matches && det) det.open = false; });
  });
  var alvos = links.map(function (a) {
    return document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
  }).filter(Boolean);

  var atual = null;
  function marca() {
    var y = window.scrollY + 120, escolhido = null;
    for (var i = 0; i < alvos.length; i++) {
      if (alvos[i].getBoundingClientRect().top + window.scrollY <= y) escolhido = alvos[i];
      else break;
    }
    var a = escolhido && porId[escolhido.id];
    if (a === atual) return;
    if (atual) atual.classList.remove("ativo");
    if (a) {
      a.classList.add("ativo");
      if (largo.matches) {
        var nav = a.closest(".doc-indice"), r = a.getBoundingClientRect(), rn = nav.getBoundingClientRect();
        if (r.top < rn.top || r.bottom > rn.bottom) nav.scrollTop += r.top - rn.top - rn.height / 3;
      }
    }
    atual = a;
    topo.classList.toggle("visivel", window.scrollY > 900);
  }

  var topo = document.createElement("a");
  topo.href = "#"; topo.className = "topo-doc"; topo.textContent = "↑ Topo";
  document.body.appendChild(topo);

  var pendente = false;
  window.addEventListener("scroll", function () {
    if (pendente) return;
    pendente = true;
    requestAnimationFrame(function () { pendente = false; marca(); });
  }, { passive: true });
  marca();
})();
