/**
 * Persistência do progresso em localStorage.
 *
 * Chave: "osQuizState" por omissão. Uma página pode definir
 * `window.QUIZ_STORAGE_KEY` (antes deste script) para isolar o progresso —
 * é assim que o Teste 2 (teste2.html) guarda a sessão em separado.
 * Robustez: try/catch silencioso — falha no localStorage não bloqueia a app.
 */
const STORAGE_KEY = (typeof window !== "undefined" && window.QUIZ_STORAGE_KEY) || "osQuizState";

function saveState(){
  try{
    localStorage.setItem(STORAGE_KEY,JSON.stringify({
      ids:ALL.map(q=>q[1]),
      questionOrder:state.questionOrder,
      optionOrder:state.optionOrder,
      results:state.results,
      index:state.index,
      topicErrors:state.topicErrors,
      streak:state.streak,
      revealed:state.revealed,
      drafts:state.drafts,
    }));
  }catch(e){}
}

function loadState(){
  try{
    const raw=localStorage.getItem(STORAGE_KEY);
    if(!raw) return false;
    const s=JSON.parse(raw);
    // QUIZ_SHUFFLE=false: o progresso segue o id de cada pergunta, por isso pode haver perguntas novas a meio.
    // Um guardado antigo não tem ids: usa QUIZ_OLD_IDS (a ordem de então).
    const ids=s.ids||(typeof window !== "undefined" && window.QUIZ_OLD_IDS);
    if(typeof window !== "undefined" && window.QUIZ_SHUFFLE===false && ids && ids.length===s.results.length){
      const de={}; ids.forEach((id,i)=>{de[id]=i;});
      const para={}; ALL.forEach((q,i)=>{if(q[1] in de) para[de[q[1]]]=i;});
      const mover=o=>{const r={}; Object.keys(o||{}).forEach(k=>{if(k in para) r[para[k]]=o[k];}); return r;};
      s.index=para[s.questionOrder[s.index]]||0;
      s.results=ALL.map(q=>q[1] in de?s.results[de[q[1]]]:null);
      s.revealed=mover(s.revealed); s.drafts=mover(s.drafts);
      s.questionOrder=ALL.map((_,i)=>i);
      delete s.ids;
    }
    if(s.questionOrder.length!==ALL.length) return false;
    Object.assign(state,{revealed:{},drafts:{}},s,{filter:null,filteredOrder:[...Array(ALL.length).keys()]});
    // Force unshuffled option order — explanations reference (A)/(B)/(C)/(D) by source order
    state.optionOrder = ALL.map(()=>[0,1,2,3]);
    if(typeof window !== "undefined" && window.QUIZ_SHUFFLE === false && s.questionOrder && s.questionOrder.some((v,i)=>v!==i)){
      state.questionOrder = [...Array(ALL.length).keys()];
    }
    return true;
  }catch(e){return false;}
}
