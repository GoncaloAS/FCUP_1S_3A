/**
 * Render principal — desenha a pergunta actual, opções, explicação,
 * e dispara updateStats / updateHeatmap.
 *
 * Lê de `state` e `ALL`; escreve no DOM.
 *
 * `currFP()` devolve a posição actual dentro de `filteredOrder`
 * (quando há filtro activo). Usado também por next()/prev() em quiz.js.
 */
function currFP(){return state.filteredOrder.indexOf(state.index);}

function render(){
  const pos=state.index;
  const qIdx=state.questionOrder[pos];
  const q=ALL[qIdx];
  const order=state.optionOrder[qIdx];
  const opts=q[3];
  const correct=parseInt(q[4]);
  const newCorrect=order.indexOf(correct);
  const res=state.results[qIdx];
  const cat=q[0];

  // badge
  const badge=document.getElementById("catBadge");
  badge.textContent=cat;
  badge.style.color=tc(cat);
  badge.style.borderColor=tc(cat)+"55";
  badge.style.background=tb(cat);

  // meta
  const fp=currFP();
  const ftot=state.filteredOrder.length;
  document.getElementById("qnumBadge").textContent="#"+q[1];
  document.getElementById("tIdx").textContent=fp+1;
  document.getElementById("tTot").textContent=ftot;

  // progress — within current filter (or overall when no filter)
  const answeredInFilter=state.filteredOrder.filter(p=>state.results[state.questionOrder[p]]).length;
  const totalInFilter=state.filteredOrder.length;
  document.getElementById("pfill").style.width=(totalInFilter?(answeredInFilter/totalInFilter*100):0)+"%";

  // question
  document.getElementById("qtext").innerHTML=q[2];

  // pergunta de resposta aberta (desenvolvimento): sem opções
  const aberta=!Array.isArray(opts);
  const visto=aberta&&(res||state.revealed[qIdx]);
  if(aberta){
    const rasc=(state.drafts[qIdx]||"").replace(/&/g,"&amp;").replace(/</g,"&lt;");
    let a=`<textarea class="rascunho" id="rascunho" rows="5" placeholder="Resolve aqui ou no papel (fica só neste browser)…" oninput="state.drafts[${qIdx}]=this.value">${rasc}</textarea>`;
    if(!visto) a+=`<div class="aberta-acoes"><button class="btn primary" onclick="revelar()">Ver resolução <span class="kbd">V</span></button></div>`;
    else if(!res) a+=`<div class="aberta-acoes"><span class="aberta-q">Compara com a resolução. Acertaste?</span>
      <button class="btn ok" onclick="autoavaliar(true)">Acertei</button><button class="btn mal" onclick="autoavaliar(false)">Errei</button></div>`;
    else a+=`<div class="aberta-acoes"><span class="aberta-marca ${res.correct?"ok":"mal"}">${res.correct?"Marcaste como certa":"Marcaste como errada"}</span></div>`;
    document.getElementById("options").innerHTML=a;
  }

  // options
  const letters=["A","B","C","D"];
  let html="";
  if(!aberta) order.forEach((optIdx,i)=>{
    let cls="",dim="";
    if(res){
      if(i===newCorrect) cls="correct";
      else if(i===res.selected) cls="incorrect";
      else dim="dimmed";
    }
    html+=`<div class="option ${cls} ${dim} ${res?"locked":""}" onclick="${res?"":"select("+i+")"}">
      <div class="oletter">${letters[i]}</div>
      <div class="otext">${opts[optIdx]}</div>
    </div>`;
  });
  if(!aberta) document.getElementById("options").innerHTML=html;

  // explainer
  const exp=document.getElementById("explainer");
  if(res||visto){
    exp.style.display="block";
    document.getElementById("expText").innerHTML=q[5]||"The highlighted answer is correct.";
    document.getElementById("expNote").innerHTML=q[6]?`📌 ${q[6]}`:"";
  } else {
    exp.style.display="none";
  }

  updateStats();
  updateHeatmap();
  document.getElementById("streakBadge").style.opacity=state.streak>0?"1":".4";
  document.getElementById("streakNum").textContent=state.streak;
  saveState();
}
