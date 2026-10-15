/**
 * Overlay de resultado final — mostra-se ao acertar/errar todas as perguntas.
 * `restartQuiz` limpa localStorage e re-baralha tudo via init().
 */
const GRADES=[
  [90,"A+","Excelente: estás pronto."],
  [80,"A","Muito bom."],
  [70,"B","Bom trabalho."],
  [60,"C","Razoável: revê os tópicos onde erras mais."],
  [50,"D","Continua a estudar."],
  [0,"F","Volta à matéria e tenta outra vez."],
];

function showResult(){
  const correct=state.results.filter(r=>r?.correct).length;
  const pct=Math.round((correct/ALL.length)*100);
  const [,grade,msg]=GRADES.find(([min])=>pct>=min);
  document.getElementById("rscore").textContent=pct+"%";
  document.getElementById("rgrade").textContent=grade;
  document.getElementById("rsub").textContent=`${correct} / ${ALL.length} certas — ${msg}`;
  document.getElementById("roverlay").classList.add("show");
}

function restartQuiz(){
  document.getElementById("roverlay").classList.remove("show");
  localStorage.removeItem(STORAGE_KEY);
  init();
}
