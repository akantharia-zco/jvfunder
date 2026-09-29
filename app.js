const modal=document.getElementById('modal'),content=document.getElementById('modalContent');
const login=`<span class="eyebrow dark">Investor Portal</span><h2>Investor Login</h2><p>This button is ready to connect to your selected investor-management / white-label platform.</p><input placeholder="Email address"><input type="password" placeholder="Password"><button class="btn primary" style="width:100%;margin-top:8px">Continue</button><p style="font-size:11px;color:#69737c">Developer note: replace this modal with the secure portal SSO or hosted login URL.</p>`;
const interest=`<span class="eyebrow dark">Investor Interest</span><h2>Stay informed.</h2><p>Join the JvFunder interest list for platform updates and notices of future opportunities.</p><input placeholder="Full name"><input type="email" placeholder="Email address"><button class="btn primary" style="width:100%;margin-top:8px">Join List</button><p style="font-size:11px;color:#69737c">Joining the list does not constitute an investment commitment.</p>`;
document.querySelectorAll('[data-modal]').forEach(b=>b.onclick=()=>{content.innerHTML=b.dataset.modal==='login'?login:interest;modal.classList.add('open')});
document.querySelector('.close').onclick=()=>modal.classList.remove('open');modal.onclick=e=>{if(e.target===modal)modal.classList.remove('open')};
document.querySelector('.menu').onclick=()=>document.querySelector('.nav').classList.toggle('open');
document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('active'));b.classList.add('active');document.querySelectorAll('.opps article').forEach(c=>c.style.display=(b.dataset.filter==='all'||c.dataset.category===b.dataset.filter)?'block':'none')});
document.getElementById('interestForm').onsubmit=e=>{e.preventDefault();document.getElementById('formMsg').textContent='Thank you. Connect this form to your CRM/email provider before launch.';e.target.reset()};

// Finished-site interactions
window.addEventListener('scroll',()=>document.querySelector('header')?.classList.toggle('scrolled',scrollY>10));
const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.12});
document.querySelectorAll('.section,.project-spotlight,.dashboard-preview').forEach(el=>{el.classList.add('reveal');observer.observe(el)});
