from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SpotOn — Find Parking Before You Arrive</title>
  <style>
    :root{
      --bg:#0b1220;
      --card:#0f1b33;
      --muted:#9fb0d0;
      --text:#e9efff;
      --accent:#3b82f6;
      --accent2:#22c55e;
      --line:rgba(255,255,255,.12);
      --shadow: 0 10px 35px rgba(0,0,0,.35);
      --radius:16px;
    }
    *{box-sizing:border-box}
    body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial; background: radial-gradient(1200px 600px at 10% 0%, #172a55 0%, transparent 50%), radial-gradient(1200px 600px at 90% 10%, #123a2a 0%, transparent 55%), var(--bg); color:var(--text);}
    a{color:inherit;text-decoration:none}
    .container{max-width:1100px;margin:0 auto;padding:0 18px}
    .pill{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--line);padding:8px 12px;border-radius:999px;color:var(--muted);background:rgba(255,255,255,.04)}
    .btn{border:1px solid var(--line);background:rgba(255,255,255,.06);color:var(--text);padding:10px 14px;border-radius:12px;cursor:pointer;transition:.15s; font-weight:600}
    .btn:hover{transform:translateY(-1px);background:rgba(255,255,255,.10)}
    .btn.primary{background:linear-gradient(135deg,var(--accent),#60a5fa);border-color:transparent}
    .btn.primary:hover{filter:brightness(1.03)}
    .btn.secondary{background:linear-gradient(135deg,var(--accent2),#86efac);border-color:transparent;color:#052010}
    .btn.ghost{background:transparent}
    header{position:sticky;top:0;z-index:30;background:rgba(11,18,32,.75);backdrop-filter: blur(10px);border-bottom:1px solid var(--line)}
    .nav{display:flex;align-items:center;justify-content:space-between;padding:14px 0}
    .brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:.2px}
    .logo{width:36px;height:36px;border-radius:12px;background:conic-gradient(from 180deg, var(--accent), var(--accent2)); box-shadow: var(--shadow)}
    .navlinks{display:flex;gap:14px;align-items:center}
    .navlinks a{color:var(--muted);font-weight:650}
    .navlinks a:hover{color:var(--text)}
    .auth{display:flex;gap:10px;align-items:center}

    /* HERO */
    .hero{padding:44px 0 24px}
    .heroGrid{display:grid;grid-template-columns: 1.2fr .8fr;gap:18px;align-items:stretch}
    .heroCard{background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:22px}
    h1{margin:6px 0 10px;font-size:40px;line-height:1.1}
    .sub{color:var(--muted);font-size:16px;line-height:1.5}
    .formRow{display:grid;grid-template-columns: 1.4fr 1fr 1fr auto;gap:10px;margin-top:16px}
    input, select{width:100%;padding:12px 12px;border-radius:12px;border:1px solid var(--line);background:rgba(255,255,255,.05);color:var(--text);outline:none}
    input::placeholder{color:rgba(233,239,255,.55)}
    .smallNote{margin-top:10px;color:rgba(233,239,255,.65);font-size:13px}
    .miniCard{display:flex;flex-direction:column;gap:12px}
    .stat{padding:14px;border-radius:14px;border:1px solid var(--line);background:rgba(255,255,255,.04)}
    .stat b{font-size:18px}
    .stat span{display:block;color:var(--muted);margin-top:4px;font-size:13px}

    /* MAP + FILTERS */
    section{padding:22px 0}
    .grid2{display:grid;grid-template-columns: 1.2fr .8fr;gap:18px}
    .card{background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow)}
    .cardHd{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;border-bottom:1px solid var(--line)}
    .cardHd h2{margin:0;font-size:16px}
    .cardBody{padding:14px 16px}
    .filters{display:flex;gap:8px;flex-wrap:wrap}
    .chip{padding:8px 10px;border-radius:999px;border:1px solid var(--line);color:var(--muted);cursor:pointer;background:rgba(255,255,255,.03);font-weight:650}
    .chip.active{color:var(--text);border-color:rgba(59,130,246,.65);background:rgba(59,130,246,.16)}
    .mapWrap{height:380px;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#061028}
    .mapWrap iframe{width:100%;height:100%;border:0;filter:saturate(1.05) contrast(1.05)}
    .spotList{display:flex;flex-direction:column;gap:10px}
    .spot{padding:12px;border-radius:14px;border:1px solid var(--line);background:rgba(255,255,255,.03);cursor:pointer;display:grid;grid-template-columns: 1fr auto;gap:8px}
    .spot:hover{background:rgba(255,255,255,.06)}
    .spot.active{outline:2px solid rgba(34,197,94,.6);background:rgba(34,197,94,.08)}
    .spot .meta{color:var(--muted);font-size:13px;margin-top:3px}
    .badge{padding:6px 10px;border-radius:999px;font-weight:800;font-size:12px;background:rgba(255,255,255,.06);border:1px solid var(--line)}
    .badge.ok{border-color:rgba(34,197,94,.55);background:rgba(34,197,94,.14)}
    .badge.no{border-color:rgba(239,68,68,.55);background:rgba(239,68,68,.14)}
    .detail{display:grid;gap:10px}
    .detailRow{display:grid;grid-template-columns:1fr 1fr;gap:10px}
    .kv{padding:12px;border-radius:14px;border:1px solid var(--line);background:rgba(255,255,255,.03)}
    .kv span{display:block;color:var(--muted);font-size:12px}
    .kv b{display:block;margin-top:4px}

    /* SERVICES */
    .cards3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .svc{padding:16px}
    .svc h3{margin:6px 0 6px}
    .svc p{margin:0;color:var(--muted);line-height:1.5}
    .icon{width:40px;height:40px;border-radius:14px;display:grid;place-items:center;border:1px solid var(--line);background:rgba(255,255,255,.05)}

    /* TESTIMONIALS */
    .tgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
    .quote{padding:16px}
    .quote p{margin:0 0 12px;color:rgba(233,239,255,.9);line-height:1.55}
    .quote small{color:var(--muted)}
    .stars{letter-spacing:2px;color:#fbbf24}

    /* CONTACT */
    form{display:grid;gap:10px}
    textarea{width:100%;min-height:110px;resize:vertical;padding:12px;border-radius:12px;border:1px solid var(--line);background:rgba(255,255,255,.05);color:var(--text);outline:none}
    .two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
    .toast{position:fixed;right:18px;bottom:18px;max-width:360px;padding:12px 14px;border-radius:14px;border:1px solid var(--line);background:rgba(15,27,51,.92);box-shadow:var(--shadow);display:none}
    .toast.show{display:block;animation:pop .18s ease-out}
    @keyframes pop{from{transform:translateY(8px);opacity:0}to{transform:translateY(0);opacity:1}}

    footer{padding:22px 0 30px;color:var(--muted);border-top:1px solid var(--line);margin-top:10px}
    .foot{display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
    .foot a{color:var(--muted)}
    .foot a:hover{color:var(--text)}

    @media (max-width: 980px){
      .heroGrid,.grid2{grid-template-columns:1fr}
      .formRow{grid-template-columns:1fr 1fr; }
      .formRow .btn{grid-column:1 / -1}
      .cards3,.tgrid{grid-template-columns:1fr}
      h1{font-size:34px}
      .navlinks{display:none}
    }
  </style>
</head>
<body>

<header>
  <div class="container nav">
    <div class="brand">
      <div class="logo" aria-hidden="true"></div>
      <div>SpotOn</div>
      <span class="pill">Find parking before you arrive</span>
    </div>

    <nav class="navlinks" aria-label="Primary">
      <a href="#services">Services</a>
      <a href="#testimonials">Testimonials</a>
      <a href="#contact">Contact</a>
    </nav>

    <div class="auth">
      <button class="btn ghost" id="loginBtn">Login</button>
      <button class="btn primary" id="signupBtn">Sign Up</button>
    </div>
  </div>
</header>

<!-- HERO (Section 2) -->
<section class="hero">
  <div class="container heroGrid">
    <div class="heroCard">
      <h1>Find Parking Before You Arrive</h1>
      <div class="sub">Real-time availability and guaranteed parking reservations.</div>

      <div class="formRow" role="search" aria-label="Parking Search">
        <input id="qDestination" placeholder="Destination / Location (e.g., Downtown)" />
        <input id="qDateTime" type="datetime-local" />
        <select id="qVehicle">
          <option value="Compact">Vehicle: Compact</option>
          <option value="Sedan">Vehicle: Sedan</option>
          <option value="SUV">Vehicle: SUV</option>
          <option value="Truck">Vehicle: Truck</option>
        </select>
        <button class="btn secondary" id="findBtn">Find Parking</button>
      </div>

      <div class="smallNote">Tip: Try filters below (Available, Cheapest, Closest). This is an MVP demo with sample spots.</div>
    </div>

    <div class="heroCard miniCard">
      <div class="stat">
        <b>Live availability</b>
        <span>See open spots update in real-time (simulated for demo)</span>
      </div>
      <div class="stat">
        <b>No double booking</b>
        <span>Reservation locking prevents two drivers booking the same spot</span>
      </div>
      <div class="stat">
        <b>Vehicle-based pricing</b>
        <span>Compact, Sedan, SUV pricing tiers + future passes</span>
      </div>
    </div>
  </div>
</section>

<!-- MAP + FILTERS (Section 3) -->
<section>
  <div class="container grid2">
    <div class="card">
      <div class="cardHd">
        <h2>Live Map & Availability</h2>
        <div class="filters" aria-label="Filters">
          <span class="chip active" data-filter="all">All Parking</span>
          <span class="chip" data-filter="available">Available Spots</span>
          <span class="chip" data-filter="cheapest">Cheapest Options</span>
          <span class="chip" data-filter="closest">Closest Spots</span>
        </div>
      </div>
      <div class="cardBody">
        <div class="mapWrap" title="Map preview">
          <!-- No API key needed. This is a preview map for the homepage demo. -->
          <iframe
            src="https://www.openstreetmap.org/export/embed.html?bbox=-74.014%2C40.701%2C-73.95%2C40.74&layer=mapnik"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </div>

    <div class="card">
      <div class="cardHd">
        <h2>Spot Selection Preview</h2>
        <span class="pill" id="resultCount">6 spots</span>
      </div>
      <div class="cardBody detail">
        <div class="spotList" id="spotList"></div>

        <div class="detailRow">
          <div class="kv"><span>Selected Spot</span><b id="selName">—</b></div>
          <div class="kv"><span>Price</span><b id="selPrice">—</b></div>
        </div>
        <div class="detailRow">
          <div class="kv"><span>Availability</span><b id="selAvail">—</b></div>
          <div class="kv"><span>Distance</span><b id="selDist">—</b></div>
        </div>

        <button class="btn primary" id="reserveBtn" disabled>Reserve This Spot</button>
      </div>
    </div>
  </div>
</section>

<!-- SERVICES (Section 4) -->
<section id="services">
  <div class="container">
    <div class="card">
      <div class="cardHd">
        <h2>Services</h2>
        <span class="pill">Core MVP capabilities</span>
      </div>
      <div class="cardBody cards3">
        <div class="card svc">
          <div class="icon">🛰️</div>
          <h3>Real-Time Availability</h3>
          <p>View live parking availability based on time and location.</p>
        </div>
        <div class="card svc">
          <div class="icon">💳</div>
          <h3>Reserve and Pay</h3>
          <p>Secure reservations with digital payments and receipts.</p>
        </div>
        <div class="card svc">
          <div class="icon">🚗</div>
          <h3>Vehicle-Based Pricing</h3>
          <p>Pricing optimized by vehicle type (Compact, Sedan, SUV).</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA (Section 5) -->
<section>
  <div class="container">
    <div class="card">
      <div class="cardBody" style="display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap">
        <div>
          <div class="pill">Ready to park smarter?</div>
          <div style="font-size:22px;font-weight:900;margin-top:10px">Reserve in seconds. Stop circling.</div>
          <div class="sub" style="margin-top:6px">Drivers get guaranteed spots; operators can list inventory (MVP onboarding).</div>
        </div>
        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn secondary" href="#top" onclick="window.scrollTo({top:0,behavior:'smooth'}); return false;">Find Parking</a>
          <button class="btn" id="listParkingBtn">List Your Parking</button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS (requested) -->
<section id="testimonials">
  <div class="container">
    <div class="card">
      <div class="cardHd">
        <h2>Testimonials</h2>
        <span class="pill">Prototype feedback</span>
      </div>
      <div class="cardBody tgrid">
        <div class="card quote">
          <div class="stars">★★★★★</div>
          <p>“I found a spot near campus in under a minute. This saves so much time.”</p>
          <small>Driver • Peer Review</small>
        </div>
        <div class="card quote">
          <div class="stars">★★★★★</div>
          <p>“The filter chips + spot preview makes it obvious what to pick. Feels modern.”</p>
          <small>Student Tester • Demo</small>
        </div>
        <div class="card quote">
          <div class="stars">★★★★☆</div>
          <p>“Reservation flow looks clean. Add navigation to the garage later.”</p>
          <small>Parking Operator (MVP) • Feedback</small>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT (requested) -->
<section id="contact">
  <div class="container">
    <div class="card">
      <div class="cardHd">
        <h2>Contact</h2>
        <span class="pill">Questions / feedback</span>
      </div>
      <div class="cardBody">
        <form id="contactForm">
          <div class="two">
            <input id="cName" placeholder="Your name" required />
            <input id="cEmail" type="email" placeholder="Your email" required />
          </div>
          <textarea id="cMsg" placeholder="Message (feature request, issue, suggestion)..." required></textarea>
          <button class="btn primary" type="submit">Send Message</button>
          <div class="smallNote">For class demos, this form shows a confirmation toast (no backend email yet).</div>
        </form>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="container foot">
    <div>© 2026 SpotOn • Parking Management System</div>
    <div style="display:flex;gap:14px;flex-wrap:wrap">
      <a href="#services">Services</a>
      <a href="#testimonials">Testimonials</a>
      <a href="#contact">Contact</a>
      <a href="#" onclick="showToast('Legal pages are placeholders for MVP.'); return false;">Terms</a>
    </div>
  </div>
</footer>

<div class="toast" id="toast"></div>

<script>
  // Sample data for MVP demo (no backend yet)
  const spots = [
    {id:1, name:"Park @ Main St", price:12, avail:true,  dist:0.6},
    {id:2, name:"City Garage B2", price:9,  avail:true,  dist:1.3},
    {id:3, name:"Lot 7 — Visitor", price:7,  avail:false, dist:0.9},
    {id:4, name:"Riverside Deck", price:15, avail:true,  dist:2.1},
    {id:5, name:"North Lot",      price:6,  avail:true,  dist:2.7},
    {id:6, name:"Event Zone P1",  price:22, avail:false, dist:0.4},
  ];

  let activeFilter = "all";
  let selectedId = null;

  const $ = (id)=>document.getElementById(id);
  const spotList = $("spotList");
  const chips = document.querySelectorAll(".chip");

  function showToast(msg){
    const t = $("toast");
    t.textContent = msg;
    t.classList.add("show");
    clearTimeout(window.__toastTimer);
    window.__toastTimer = setTimeout(()=>t.classList.remove("show"), 2600);
  }

  function applyFilter(list){
    if(activeFilter==="available") return list.filter(s=>s.avail);
    if(activeFilter==="cheapest")  return [...list].sort((a,b)=>a.price-b.price);
    if(activeFilter==="closest")   return [...list].sort((a,b)=>a.dist-b.dist);
    return list;
  }

  function render(){
    const filtered = applyFilter(spots);
    $("resultCount").textContent = filtered.length + " spots";
    spotList.innerHTML = filtered.map(s => {
      const badge = s.avail ? '<span class="badge ok">Available</span>' : '<span class="badge no">Full</span>';
      const active = (s.id===selectedId) ? "active" : "";
      return `
        <div class="spot ${active}" data-id="${s.id}">
          <div>
            <b>${s.name}</b>
            <div class="meta">$${s.price}/hr • ${s.dist} mi</div>
          </div>
          <div>${badge}</div>
        </div>
      `;
    }).join("");

    // attach click handlers
    document.querySelectorAll(".spot").forEach(el=>{
      el.addEventListener("click", ()=>{
        const id = Number(el.dataset.id);
        selectSpot(id);
      });
    });

    // refresh details
    const sel = spots.find(s=>s.id===selectedId);
    $("reserveBtn").disabled = !(sel && sel.avail);
    $("selName").textContent = sel ? sel.name : "—";
    $("selPrice").textContent = sel ? `$${sel.price}/hr` : "—";
    $("selAvail").textContent = sel ? (sel.avail ? "Available" : "Full") : "—";
    $("selDist").textContent = sel ? `${sel.dist} mi` : "—";
  }

  function selectSpot(id){
    selectedId = id;
    const sel = spots.find(s=>s.id===selectedId);
    if(sel){
      showToast(sel.avail ? `Selected: ${sel.name}` : `Selected: ${sel.name} (currently full)`);
    }
    render();
  }

  chips.forEach(c=>{
    c.addEventListener("click", ()=>{
      chips.forEach(x=>x.classList.remove("active"));
      c.classList.add("active");
      activeFilter = c.dataset.filter;
      selectedId = null;
      render();
      showToast("Filter: " + c.textContent);
    });
  });

  $("findBtn").addEventListener("click", ()=>{
    const dest = $("qDestination").value.trim() || "your destination";
    showToast(`Searching spots near ${dest}... (demo data)`);
    document.querySelector("section").scrollIntoView({behavior:"smooth"});
  });

  $("reserveBtn").addEventListener("click", ()=>{
    const sel = spots.find(s=>s.id===selectedId);
    if(!sel) return;
    showToast(`Reserved: ${sel.name} — receipt generated (demo)`);
  });

  $("listParkingBtn").addEventListener("click", ()=>{
    showToast("Operator onboarding is MVP scope — form coming next.");
  });

  $("contactForm").addEventListener("submit", (e)=>{
    e.preventDefault();
    showToast("Message sent! (demo) We'll contact you soon.");
    e.target.reset();
  });

  $("loginBtn").addEventListener("click", ()=>showToast("Login screen is next sprint."));
  $("signupBtn").addEventListener("click", ()=>showToast("Sign up screen is next sprint."));

  render();
</script>

</body>
</html>
"""
import os
if __name__ == "__main__":
    # Use a non-conflicting port
    app.run(debug=True, host="0.0.0.0", port=5055)                    
 
