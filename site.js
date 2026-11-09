// Shared: mobile menu
(function(){const nav=document.querySelector('nav'),t=nav&&nav.querySelector('.menu-toggle');if(!t)return;
const set=o=>{nav.classList.toggle('open',o);t.setAttribute('aria-expanded',o)};
t.addEventListener('click',()=>set(!nav.classList.contains('open')));
nav.querySelectorAll('.links a, .menu-cta').forEach(el=>el.addEventListener('click',()=>set(false)));
document.addEventListener('keydown',e=>{if(e.key==='Escape')set(false)});
matchMedia('(min-width:801px)').addEventListener('change',e=>{if(e.matches)set(false)})})();
