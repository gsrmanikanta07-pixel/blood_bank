const API = "http://127.0.0.1:5000";

/* DONORS */
async function loadDonors(){
let res = await fetch(API+"/donors");
let data = await res.json();
let rows="";
data.forEach(d=>{
rows+=`<tr>
<td>${d.donor_id}</td>
<td>${d.name}</td>
<td>${d.blood_type}</td>
<td>${d.contact}</td>
<td>${d.last_donation}</td>
</tr>`;
});
document.getElementById("donorTable").innerHTML=rows;
}

async function addDonor(){

const payload = {
name: document.getElementById("name").value,
blood_type: document.getElementById("blood").value,
contact: document.getElementById("contact").value,
last_donation: document.getElementById("date").value
};

console.log(payload);

await fetch(API + "/donors", {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify(payload)
});

loadDonors();
}

/* HOSPITALS */
async function loadHospitals(){
let res = await fetch(API+"/hospitals");
let data = await res.json();
let rows="";
data.forEach(h=>{
rows+=`<tr>
<td>${h.hospital_id}</td>
<td>${h.name}</td>
<td>${h.location}</td>
<td>${h.contact}</td>
</tr>`;
});
hospitalTable.innerHTML=rows;
}

async function addHospital(){
await fetch(API+"/hospitals",{method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
name:hname.value,
location:location.value,
contact:hcontact.value
})});
loadHospitals();
}

/* STOCK */
async function loadStock(){
let res = await fetch(API+"/stock");
let data = await res.json();
let rows="";
data.forEach(s=>{
rows+=`<tr>
<td>${s.stock_id}</td>
<td>${s.blood_type}</td>
<td>${s.quantity}</td>
</tr>`;
});
stockTable.innerHTML=rows;
}

async function addStock(){
await fetch(API+"/stock",{method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
blood_type:stype.value,
quantity:qty.value
})});
loadStock();
}

/* REQUESTS */
async function loadRequests(){
let res = await fetch(API+"/requests");
let data = await res.json();
let rows="";
data.forEach(r=>{
rows+=`<tr>
<td>${r.request_id}</td>
<td>${r.hospital_id}</td>
<td>${r.blood_type}</td>
<td>${r.quantity}</td>
<td>${r.request_date}</td>
<td>${r.status}</td>
</tr>`;
});
requestTable.innerHTML=rows;
}

async function addRequest(){
await fetch(API+"/requests",{method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
hospital_id:hospital_id.value,
blood_type:rblood.value,
quantity:rqty.value,
request_date:rdate.value
})});
loadRequests();
}

/* ISSUES */
async function loadIssues(){
let res = await fetch(API+"/issues");
let data = await res.json();
let rows="";
data.forEach(i=>{
rows+=`<tr>
<td>${i.issue_id}</td>
<td>${i.request_id}</td>
<td>${i.issue_date}</td>
<td>${i.units_issued}</td>
</tr>`;
});
issueTable.innerHTML=rows;
}

async function issueBlood(){
await fetch(API+"/issues",{method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
request_id:req_id.value,
issue_date:issue_date.value,
units_issued:units.value
})});
loadIssues();
}