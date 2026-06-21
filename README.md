# 오늘의 체크리스트 📅

날짜별 할 일을 관리하는 캘린더 기반 체크리스트 웹앱입니다.

## 기능
- 월간 캘린더에서 날짜 선택
- 날짜별 체크리스트 항목 추가 / 완료 / 삭제
- 진행률 표시 (진행 바 + 완료 개수)
- 캘린더 날짜에 완료율 점 표시 (🟢 전부 완료 / 🟡 일부 완료)
- localStorage 저장으로 새로고침 후에도 데이터 유지
- PC / 모바일 반응형 UI

## 파일 구조
```
Checklist_App/
├── index.html        # 앱 본체 (HTML + CSS + JS 단일 파일)
├── app.py            # Streamlit 배포용 래퍼
├── requirements.txt  # Streamlit Cloud 의존성
└── .gitignore
```

## 실행 방법

### 로컬 실행 (HTML 직접)
`index.html` 파일을 브라우저로 열면 됩니다.

### Streamlit으로 실행
```bash
pip install streamlit
streamlit run app.py
```

## 배포 (Streamlit Cloud)
1. 이 저장소를 GitHub에 올립니다.
2. [share.streamlit.io](https://share.streamlit.io) 접속 → GitHub 계정 연동
3. **Create app** → 저장소 선택 → Main file: `app.py` → **Deploy**
