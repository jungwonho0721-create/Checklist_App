import hmac
from textwrap import dedent

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="금복이 성장소",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)


APP_CSS = """
<style>
    [data-testid="stHeader"], [data-testid="stToolbar"],
    [data-testid="stDecoration"], #MainMenu, footer { display: none !important; }
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(145deg, #fff 0%, #fff8fb 48%, #ffeaf2 100%);
    }
    [data-testid="stMainBlockContainer"] {
        max-width: 1240px;
        padding: 1.4rem 1rem 0;
    }
    iframe { border: 0; }
    .login-wrap {
        min-height: 78vh;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .login-card {
        width: min(440px, 92vw);
        margin: 9vh auto 1.4rem;
        padding: 2.4rem 2rem 1.5rem;
        text-align: center;
        border: 1px solid #ffe1ec;
        border-radius: 30px;
        background: rgba(255,255,255,.94);
        box-shadow: 0 22px 70px rgba(229, 91, 142, .16);
    }
    .login-flower { font-size: 3.2rem; margin-bottom: .45rem; }
    .login-title { color: #d94f83; font-size: 2rem; font-weight: 800; margin: 0; }
    .login-copy { color: #8d6d79; margin: .65rem 0 0; }
    div[data-testid="stForm"] {
        width: min(440px, 92vw);
        margin: 0 auto;
        padding: 0 2rem 2.2rem;
        border: 1px solid #ffe1ec;
        border-top: 0;
        border-radius: 0 0 30px 30px;
        background: rgba(255,255,255,.94);
        box-shadow: 0 30px 70px rgba(229, 91, 142, .13);
    }
    div[data-testid="stTextInput"] input {
        border: 1px solid #f5c6d7;
        border-radius: 14px;
        text-align: center;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #ed7fa7;
        box-shadow: 0 0 0 2px rgba(237,127,167,.15);
    }
    div[data-testid="stFormSubmitButton"] button {
        width: 100%; border: 0; border-radius: 14px;
        color: white; font-weight: 700;
        background: linear-gradient(135deg, #f08bb1, #df5f90);
    }
    div[data-testid="stAlert"] { width: min(440px, 92vw); margin: .7rem auto; }
</style>
"""

st.markdown(APP_CSS, unsafe_allow_html=True)


def login() -> bool:
    if st.session_state.get("authenticated"):
        return True

    st.markdown(
        """
        <div class="login-card">
            <div class="login-flower">🌸</div>
            <h1 class="login-title">금복이 성장소</h1>
            <p class="login-copy">금복이의 소중한 성장 기록을 만나보세요.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.form("login_form"):
        password = st.text_input(
            "비밀번호",
            type="password",
            placeholder="비밀번호를 입력해주세요",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button("들어가기")

    if submitted:
        if hmac.compare_digest(password, "0326"):
            st.session_state.authenticated = True
            st.rerun()
        st.error("비밀번호가 맞지 않아요. 다시 확인해주세요.", icon="🌷")
    return False


if not login():
    st.stop()


html = dedent(r"""
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box} body{margin:0;font-family:Arial,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;color:#392b31;background:transparent}
button,input{font:inherit} button{cursor:pointer}.app{max-width:1180px;margin:0 auto;padding:16px 8px 30px}
.hero{text-align:center;margin:4px 0 30px}.hero h1{margin:0;color:#df5f90;font-size:40px;letter-spacing:-2px}.hero p{margin:10px 0 0;color:#8d6d79;font-size:16px}.heart{color:#f188ad}
.grid{display:grid;grid-template-columns:minmax(400px,.88fr) minmax(500px,1.12fr);gap:26px;align-items:start}
.card{background:rgba(255,255,255,.96);border:1px solid #ffe1ec;border-radius:28px;box-shadow:0 18px 48px rgba(222,87,139,.12)}
.calendar{padding:28px 32px 34px}.cal-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:25px}.cal-head h2{font-size:24px;margin:0;color:#4a3540}
.nav{width:44px;height:44px;border:1px solid #f7d3df;border-radius:50%;background:#fff;color:#d95b8a;font-size:25px;box-shadow:0 5px 13px rgba(215,91,137,.1)}
.week,.days{display:grid;grid-template-columns:repeat(7,1fr);text-align:center}.week{margin-bottom:10px;color:#8e7a82;font-size:13px;font-weight:700}.week span:first-child{color:#ea728f}.week span:last-child{color:#7191bb}
.day{position:relative;aspect-ratio:1;border:0;background:transparent;border-radius:50%;color:#40353a;font-weight:650}.day.muted{color:#d8ccd1}.day:hover:not(.muted){background:#fff0f5;color:#d94f83}.day.selected{color:white;background:linear-gradient(145deg,#f48fb5,#df5f90);box-shadow:0 7px 18px rgba(223,95,144,.28)}
.day.has-items:after{content:"";position:absolute;bottom:8px;left:50%;width:4px;height:4px;border-radius:50%;background:#eb77a1;transform:translateX(-50%)}.day.selected:after{background:white}
.tasks{padding:30px 34px}.date-row{display:flex;align-items:center;gap:10px;flex-wrap:wrap}.date-row h2{margin:0;font-size:24px}.today{padding:5px 11px;border-radius:999px;background:#ffe4ee;color:#d84f82;font-size:12px;font-weight:800}
.progress-card{margin:26px 0 22px;padding:18px;border-radius:18px;background:#fff9fb;box-shadow:0 7px 18px rgba(211,107,147,.09)}.progress-label{display:flex;justify-content:space-between;color:#8b6c78;font-size:14px;font-weight:700}.progress-count{color:#d95787}.track{height:8px;margin-top:12px;border-radius:20px;background:#f5e8ed;overflow:hidden}.bar{height:100%;width:0;background:linear-gradient(90deg,#f3a0be,#df5f90);transition:width .25s}
.add-form{display:flex;gap:12px;margin-bottom:18px}.add-form input{min-width:0;flex:1;padding:15px 17px;border:1px solid #f4d4df;border-radius:15px;background:#fffafb;outline:none}.add-form input:focus{border-color:#eb85aa;box-shadow:0 0 0 3px #fff0f5}.add{flex:none;width:54px;border:0;border-radius:16px;color:white;background:linear-gradient(145deg,#f28db2,#dc5c8d);font-size:28px;box-shadow:0 8px 18px rgba(220,92,141,.25)}
.list{display:flex;flex-direction:column;gap:9px;max-height:450px;overflow:auto;padding-right:6px}.item{display:flex;align-items:center;gap:13px;min-height:58px;padding:10px 12px;border:1px solid #fff0f5;border-radius:15px;background:white}.check{flex:none;width:24px;height:24px;border:2px solid #e8a2bb;border-radius:50%;background:white;color:white;display:grid;place-items:center}.item.done .check{border-color:#e26392;background:#e26392}.item.done .check:after{content:"✓"}.item.done .text{text-decoration:line-through;color:#bba5ad}.text{flex:1}.delete{border:0;background:transparent;color:#c8a6b2;font-size:18px;padding:8px}.delete:hover{color:#dc527f}
.empty{text-align:center;padding:35px;color:#b69aa5}
@media(max-width:860px){.app{padding:8px 4px 24px}.hero{margin-bottom:20px}.hero h1{font-size:30px}.hero p{font-size:14px}.grid{grid-template-columns:1fr;gap:18px}.calendar,.tasks{padding:22px 20px}.card{border-radius:22px}.cal-head h2,.date-row h2{font-size:21px}.list{max-height:none}.day.has-items:after{bottom:4px}}
@media(max-width:430px){.calendar,.tasks{padding:19px 15px}.day{font-size:13px}.hero h1{font-size:27px}.hero p{padding:0 15px}.add-form input{font-size:14px}.tasks{padding-bottom:28px}}
</style>
</head>
<body>
<div class="app">
  <header class="hero"><h1>🌸 오늘의 금복이 성장케어</h1><p>건강한 유진이와 금복이를 위한 영양소 보충<span class="heart">♡</span></p></header>
  <main class="grid">
    <section class="card calendar" aria-label="월간 캘린더">
      <div class="cal-head"><button class="nav" id="prev" aria-label="이전 달로 이동">‹</button><h2 id="monthTitle"></h2><button class="nav" id="next" aria-label="다음 달로 이동">›</button></div>
      <div class="week"><span>일</span><span>월</span><span>화</span><span>수</span><span>목</span><span>금</span><span>토</span></div><div class="days" id="days"></div>
    </section>
    <section class="card tasks" aria-label="할 일 체크리스트">
      <div class="date-row"><h2 id="dateTitle"></h2><span class="today" id="todayBadge">TODAY</span></div>
      <div class="progress-card"><div class="progress-label"><span>오늘의 성장도</span><span class="progress-count" id="progressText">0 / 0 (0%)</span></div><div class="track"><div class="bar" id="bar"></div></div></div>
      <form class="add-form" id="addForm"><input id="newItem" required maxlength="80" placeholder="새로운 성장케어 항목을 입력하세요..." aria-label="새로운 성장케어 항목"><button class="add" type="submit" aria-label="체크리스트 항목 추가">+</button></form>
      <div class="list" id="list"></div>
    </section>
  </main>
</div>
<script>
const DEFAULTS=['아침 스트레칭 10분','물 2L 마시기','오늘 업무 목표 3가지 정리','점심 후 산책 20분','집중 업무 블록 2시간','독서 또는 학습 30분','하루 일기 & 내일 계획 작성'];
const pad=n=>String(n).padStart(2,'0'); const key=d=>`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
const today=new Date(); today.setHours(0,0,0,0); let selected=new Date(today); let view=new Date(today.getFullYear(),today.getMonth(),1);
let data={}; try{data=JSON.parse(localStorage.getItem('geumboki-growth-care')||'{}')}catch(e){data={}}
function save(){localStorage.setItem('geumboki-growth-care',JSON.stringify(data))}
function itemsFor(d){const k=key(d); if(!data[k]) data[k]=(k===key(today)?DEFAULTS:[]).map((text,i)=>({id:Date.now()+i,text,done:false})); return data[k]}
function renderCalendar(){document.getElementById('monthTitle').textContent=`${view.getFullYear()}년 ${pad(view.getMonth()+1)}월`; const root=document.getElementById('days');root.innerHTML='';const first=new Date(view.getFullYear(),view.getMonth(),1);const start=new Date(first);start.setDate(1-first.getDay());for(let i=0;i<42;i++){const d=new Date(start);d.setDate(start.getDate()+i);const b=document.createElement('button');b.type='button';b.className='day';b.textContent=d.getDate();b.setAttribute('aria-label',`${d.getFullYear()}년 ${d.getMonth()+1}월 ${d.getDate()}일`);if(d.getMonth()!==view.getMonth())b.classList.add('muted');if(key(d)===key(selected))b.classList.add('selected');if(data[key(d)]?.length)b.classList.add('has-items');b.onclick=()=>{selected=d;view=new Date(d.getFullYear(),d.getMonth(),1);render()};root.appendChild(b)}}
function renderTasks(){const items=itemsFor(selected);document.getElementById('dateTitle').textContent=`${selected.getFullYear()}년 ${pad(selected.getMonth()+1)}월 ${pad(selected.getDate())}일`;document.getElementById('todayBadge').style.display=key(selected)===key(today)?'inline-block':'none';const done=items.filter(x=>x.done).length,pct=items.length?Math.round(done/items.length*100):0;document.getElementById('progressText').textContent=`${done} / ${items.length} (${pct}%)`;document.getElementById('bar').style.width=pct+'%';const root=document.getElementById('list');root.innerHTML='';if(!items.length){root.innerHTML='<div class="empty">성장케어 항목을 추가해보세요 🌷</div>';return}items.forEach(item=>{const row=document.createElement('div');row.className='item'+(item.done?' done':'');const check=document.createElement('button');check.type='button';check.className='check';check.setAttribute('aria-label',item.done?'완료 취소':'완료 표시');check.onclick=()=>{item.done=!item.done;save();renderTasks()};const text=document.createElement('span');text.className='text';text.textContent=item.text;const del=document.createElement('button');del.type='button';del.className='delete';del.textContent='♲';del.setAttribute('aria-label',`${item.text} 삭제`);del.onclick=()=>{data[key(selected)]=items.filter(x=>x.id!==item.id);save();render()};row.append(check,text,del);root.appendChild(row)})}
function render(){renderCalendar();renderTasks()}
document.getElementById('prev').onclick=()=>{view=new Date(view.getFullYear(),view.getMonth()-1,1);renderCalendar()};document.getElementById('next').onclick=()=>{view=new Date(view.getFullYear(),view.getMonth()+1,1);renderCalendar()};document.getElementById('addForm').onsubmit=e=>{e.preventDefault();const input=document.getElementById('newItem'),text=input.value.trim();if(!text)return;itemsFor(selected).push({id:Date.now(),text,done:false});input.value='';save();render()};render();save();
</script>
</body></html>
""")

components.html(html, height=960, scrolling=False)
