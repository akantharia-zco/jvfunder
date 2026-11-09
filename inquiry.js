// Investor inquiry form (shared by the dialog on the home page and the Investor access page).
// Before launch, set INQUIRY_ENDPOINT to a form-handling URL (it receives a JSON POST).
// While it is empty, the form opens the visitor's email app addressed to INQUIRY_EMAIL.
const INQUIRY_EMAIL='investors@jvfunder.com';
const INQUIRY_ENDPOINT='';
(function(){
const dlg=document.getElementById('inquiry');
document.querySelectorAll('[data-inquiry]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('dialog[open]').forEach(x=>x.close());if(dlg){const f=dlg.querySelector('.status');if(f)f.textContent='';dlg.showModal()}}));
if(dlg)dlg.addEventListener('click',e=>{if(e.target===dlg){const r=dlg.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dlg.close()}});
document.querySelectorAll('.inquiry-form').forEach(form=>{
form.addEventListener('submit',async e=>{
e.preventDefault();
const status=form.querySelector('.status');
if(!form.checkValidity()){form.reportValidity();return}
const d=Object.fromEntries(new FormData(form).entries());
d.accredited=!!d.accredited;
const lines=[['Name',d.name],['Firm or entity',d.firm||'-'],['Email',d.email],['Phone',d.phone||'-'],['Inquiring as',d.type],['Indicative interest',d.amount],['Area of interest',d.area],['Eligibility confirmed',d.accredited?'Yes':'No'],['Message',d.message||'-']];
const text='JVFUNDER INVESTOR INQUIRY\n\n'+lines.map(l=>l[0]+': '+l[1]).join('\n')+'\n\nThis inquiry is not a subscription, investment commitment, or reservation.';
if(INQUIRY_ENDPOINT){
 try{const r=await fetch(INQUIRY_ENDPOINT,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});
  if(!r.ok)throw new Error(r.status);
  form.reset();location.href='thank-you.html';return}
 catch(err){status.textContent='Sorry, we could not send your request. Please email '+INQUIRY_EMAIL+'.';return}
}
const a=document.createElement('a');a.href='mailto:'+INQUIRY_EMAIL+'?subject='+encodeURIComponent('Investor packet request')+'&body='+encodeURIComponent(text);document.body.appendChild(a);a.click();a.remove();
form.reset();setTimeout(()=>{location.href='thank-you.html'},700);
});});
})();
