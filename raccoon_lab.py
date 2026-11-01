import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    # GameN '두더지를 잡아라 (game10)' 원작 규칙 및 다이아몬드 광산 테마 완벽 재현 버전
    game = mo.iframe(r"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
      <meta charset="utf-8">
      <title>두더지를 잡아라 - 다이아몬드 광산 대소동</title>
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

        * {
          box-sizing: border-box;
          user-select: none;
          -webkit-user-select: none;
        }

        body {
          margin: 0;
          padding: 10px;
          display: flex;
          justify-content: center;
          align-items: center;
          background: transparent;
          font-family: 'Jua', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* 다이아몬드 광산 아케이드 보드 */
        #mine-stage {
          width: 600px;
          background: 
            radial-gradient(circle at 20% 20%, rgba(52, 152, 219, 0.22) 0%, transparent 40%),
            radial-gradient(circle at 80% 35%, rgba(155, 89, 182, 0.22) 0%, transparent 45%),
            linear-gradient(180deg, #1b2631 0%, #2c3e50 45%, #3e2723 80%, #271815 100%);
          border-radius: 30px;
          padding: 18px 22px 24px;
          box-shadow: 0 18px 40px rgba(0,0,0,0.5), inset 0 2px 6px rgba(255,255,255,0.2);
          text-align: center;
          position: relative;
          border: 4px solid #5d4037;
          overflow: hidden;
          color: #ecf0f1;
        }

        /* 피버 모드 활성화 시 화려한 배경 광원 효과 */
        #mine-stage.fever-step-1 {
          box-shadow: 0 0 30px rgba(46, 204, 113, 0.5), inset 0 0 25px rgba(46, 204, 113, 0.25);
          border-color: #2ecc71;
        }
        #mine-stage.fever-step-2 {
          box-shadow: 0 0 35px rgba(52, 152, 219, 0.6), inset 0 0 30px rgba(52, 152, 219, 0.3);
          border-color: #3498db;
        }
        #mine-stage.fever-step-3 {
          box-shadow: 0 0 40px rgba(231, 76, 60, 0.7), inset 0 0 35px rgba(231, 76, 60, 0.35);
          border-color: #e74c3c;
        }
        #mine-stage.fever-boss {
          box-shadow: 0 0 50px rgba(241, 196, 15, 0.9), inset 0 0 45px rgba(241, 196, 15, 0.45);
          border-color: #f1c40f;
        }

        /* 커스텀 망치 커서 3종 */
        .cursor-wood {
          cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 50 50'><g transform='rotate(-25 25 25)'><rect x='22' y='18' width='6' height='26' rx='2' fill='%23a0522d'/><rect x='10' y='8' width='30' height='15' rx='4' fill='%23cd853f' stroke='%235c2e0b' stroke-width='2'/></g></svg>") 12 12, auto !important;
        }
        .cursor-wood:active {
          cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 50 50'><g transform='rotate(-65 25 25)'><rect x='22' y='18' width='6' height='26' rx='2' fill='%23a0522d'/><rect x='10' y='8' width='30' height='15' rx='4' fill='%23cd853f' stroke='%235c2e0b' stroke-width='2'/></g></svg>") 12 12, auto !important;
        }
        .cursor-iron {
          cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 50 50'><g transform='rotate(-25 25 25)'><rect x='22' y='18' width='6' height='26' rx='2' fill='%2334495e'/><rect x='8' y='7' width='34' height='16' rx='3' fill='%23bdc3c7' stroke='%232c3e50' stroke-width='2.5'/></g></svg>") 12 12, auto !important;
        }
        .cursor-iron:active {
          cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 50 50'><g transform='rotate(-65 25 25)'><rect x='22' y='18' width='6' height='26' rx='2' fill='%2334495e'/><rect x='8' y='7' width='34' height='16' rx='3' fill='%23bdc3c7' stroke='%232c3e50' stroke-width='2.5'/></g></svg>") 12 12, auto !important;
        }
        .cursor-golden {
          cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 50 50'><g transform='rotate(-25 25 25)'><rect x='22' y='18' width='6' height='26' rx='2' fill='%23c0392b'/><rect x='7' y='6' width='36' height='18' rx='4' fill='%23f1c40f' stroke='%23b7950b' stroke-width='2.5'/></g></svg>") 12 12, auto !important;
        }
        .cursor-golden:active {
          cursor: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='52' height='52' viewBox='0 0 50 50'><g transform='rotate(-65 25 25)'><rect x='22' y='18' width='6' height='26' rx='2' fill='%23c0392b'/><rect x='7' y='6' width='36' height='18' rx='4' fill='%23f1c40f' stroke='%23b7950b' stroke-width='2.5'/></g></svg>") 12 12, auto !important;
        }

        /* 상단 헤더 & 캐릭터 가이드 버튼 */
        .top-row {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 10px;
        }

        .game-title {
          margin: 0;
          font-size: 28px;
          color: #f1c40f;
          text-shadow: 2px 3px 0 #000, 0 0 12px rgba(241, 196, 15, 0.5);
          display: flex;
          align-items: center;
          gap: 8px;
        }

        .guide-btn {
          font-family: inherit;
          background: #34495e;
          color: #ecf0f1;
          border: 2px solid #7f8c8d;
          padding: 5px 12px;
          border-radius: 20px;
          font-size: 14px;
          cursor: pointer;
        }
        .guide-btn:hover { background: #4a6583; }

        /* 망치 선택 탭 */
        .hammer-bar {
          display: flex;
          justify-content: center;
          gap: 10px;
          margin-bottom: 10px;
        }

        .hammer-btn {
          padding: 5px 14px;
          border-radius: 20px;
          background: rgba(255,255,255,0.12);
          border: 2px solid rgba(255,255,255,0.25);
          color: #bdc3c7;
          font-size: 13px;
          cursor: pointer;
          transition: all 0.15s;
        }
        .hammer-btn.active {
          background: linear-gradient(180deg, #f39c12 0%, #d35400 100%);
          border-color: #f1c40f;
          color: #fff;
          transform: scale(1.05);
          box-shadow: 0 3px 10px rgba(243, 156, 18, 0.4);
        }

        /* 스코어 & 게이지 대시보드 (GameN 스타일) */
        .hud-panel {
          background: rgba(15, 22, 30, 0.85);
          border: 2px solid #4a6583;
          border-radius: 16px;
          padding: 10px 16px;
          margin-bottom: 14px;
        }

        .hud-stats {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 8px;
        }

        .score-box {
          font-size: 26px;
          color: #f1c40f;
          text-shadow: 2px 2px 0 #000;
        }

        .fever-stars {
          display: flex;
          align-items: center;
          gap: 6px;
          font-size: 16px;
          background: rgba(255,255,255,0.08);
          padding: 4px 12px;
          border-radius: 20px;
        }

        .star-icon {
          font-size: 20px;
          filter: grayscale(100%) opacity(0.35);
          transition: all 0.25s;
        }
        .star-icon.on {
          filter: grayscale(0%) opacity(1);
          transform: scale(1.2);
        }

        /* 타임 바 & 피버 게이지 바 */
        .bar-wrap {
          display: flex;
          align-items: center;
          gap: 8px;
          margin-bottom: 6px;
        }
        .bar-label {
          width: 65px;
          font-size: 13px;
          text-align: left;
          color: #bdc3c7;
        }
        .bar-track {
          flex: 1;
          height: 14px;
          background: #1a252f;
          border-radius: 10px;
          overflow: hidden;
          border: 1px solid #34495e;
          position: relative;
        }
        .time-fill {
          height: 100%;
          width: 100%;
          background: linear-gradient(90deg, #3498db, #2ecc71);
          transition: width 0.1s linear;
        }
        .time-fill.danger {
          background: linear-gradient(90deg, #c0392b, #e74c3c);
        }
        .fever-fill {
          height: 100%;
          width: 0%;
          background: linear-gradient(90deg, #f39c12, #e74c3c, #9b59b6);
          transition: width 0.15s ease-out;
        }

        /* 3x3 광산 구멍 그리드 + 중앙 대형 홀(BigHole) */
        .stage-wrapper {
          position: relative;
          margin-bottom: 16px;
        }

        .mine-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 14px;
          padding: 4px;
        }

        /* 깊게 파인 광산 구멍 (Crater Pit) */
        .crater-pit {
          position: relative;
          height: 118px;
          background: radial-gradient(ellipse at 50% 30%, #0d0704 0%, #261409 65%, #3e2211 100%);
          border-radius: 50% / 34%;
          box-shadow: 
            inset 0 18px 22px rgba(0,0,0,0.95),
            inset 0 -3px 8px rgba(255,255,255,0.1),
            0 7px 0 #1b100c,
            0 12px 16px rgba(0,0,0,0.6);
          overflow: hidden;
          border: 4px solid #5d4037;
        }

        /* 광산 돌/흙 앞턱 가림막 */
        .crater-pit::after {
          content: '';
          position: absolute;
          bottom: -2px;
          left: -4px;
          right: -4px;
          height: 40px;
          background: radial-gradient(ellipse at 50% 90%, #5d4037 0%, #3e2723 75%, #271815 100%);
          border-radius: 0 0 50% 50% / 0 0 45% 45%;
          border-bottom: 4px solid #8d6e63;
          box-shadow: inset 0 3px 6px rgba(255,255,255,0.18);
          z-index: 10;
          pointer-events: none;
        }

        /* 구멍 속 캐릭터 래퍼 */
        .mole-slot {
          position: absolute;
          left: 50%;
          bottom: 10px;
          transform: translate(-50%, 125%);
          width: 88px;
          height: 98px;
          transition: transform 0.14s cubic-bezier(0.18, 0.89, 0.32, 1.28);
          z-index: 5;
        }

        .mole-slot.up {
          transform: translate(-50%, 0%);
        }

        /* 다회 타격 배지 (헬멧/시계 두더지 남은 타격 수) */
        .hp-badge {
          position: absolute;
          top: 2px;
          right: 4px;
          background: #e74c3c;
          color: #fff;
          font-size: 12px;
          padding: 2px 6px;
          border-radius: 10px;
          border: 1.5px solid #fff;
          z-index: 15;
          font-weight: bold;
        }

        /* 중앙 빅 홀 (BigHole: 갓파더 보스 두더지 & 토끼 경관 출동 레이어) */
        #big-hole-overlay {
          position: absolute;
          inset: 0;
          background: rgba(0, 0, 0, 0.72);
          border-radius: 20px;
          display: none;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          z-index: 35;
          backdrop-filter: blur(3px);
          animation: popIn 0.25s cubic-bezier(0.18, 0.89, 0.32, 1.28);
        }

        @keyframes popIn {
          0% { transform: scale(0.7); opacity: 0; }
          100% { transform: scale(1); opacity: 1; }
        }

        .big-crater {
          width: 260px;
          height: 240px;
          background: radial-gradient(ellipse at 50% 70%, #1a0d06 0%, #3e2723 80%);
          border-radius: 50% / 30%;
          border: 6px solid #f1c40f;
          box-shadow: 0 0 35px rgba(241, 196, 15, 0.6), inset 0 20px 30px #000;
          display: flex;
          justify-content: center;
          align-items: center;
          position: relative;
          cursor: pointer;
        }

        /* 점수/시간 팝업 텍스트 */
        .floating-pop {
          position: absolute;
          top: 5px;
          left: 50%;
          transform: translateX(-50%);
          font-size: 22px;
          font-weight: 900;
          color: #f1c40f;
          text-shadow: 2px 2px 0 #000, -1px -1px 0 #000;
          z-index: 40;
          animation: floatAnim 0.65s ease-out forwards;
          pointer-events: none;
          white-space: nowrap;
        }

        @keyframes floatAnim {
          0% { opacity: 0; transform: translate(-50%, 15px) scale(0.6); }
          40% { opacity: 1; transform: translate(-50%, -15px) scale(1.25); }
          100% { opacity: 0; transform: translate(-50%, -42px) scale(1); }
        }

        /* 스테이지 진동 애니메이션 */
        .shake {
          animation: stageShake 0.35s ease-in-out;
        }
        @keyframes stageShake {
          0%, 100% { transform: translate(0, 0); }
          20% { transform: translate(-10px, 5px); }
          40% { transform: translate(10px, -5px); }
          60% { transform: translate(-8px, -4px); }
          80% { transform: translate(8px, 4px); }
        }

        /* 하단 버튼 */
        .action-btn {
          font-family: inherit;
          padding: 12px 42px;
          font-size: 22px;
          color: #fff;
          background: linear-gradient(180deg, #f39c12 0%, #d35400 100%);
          border: 2px solid #f1c40f;
          border-radius: 50px;
          box-shadow: 0 6px 0 #873600, 0 10px 20px rgba(0,0,0,0.4);
          cursor: pointer;
          transition: all 0.1s;
        }
        .action-btn:hover {
          filter: brightness(1.1);
          transform: translateY(-2px);
        }
        .action-btn:active {
          transform: translateY(4px);
          box-shadow: 0 2px 0 #873600;
        }

        /* 모달 (게임오버 & 캐릭터 도감) */
        .modal-layer {
          position: absolute;
          inset: 0;
          background: rgba(0, 0, 0, 0.84);
          display: none;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          border-radius: 26px;
          z-index: 60;
          padding: 20px;
        }

        .modal-card {
          background: #2c3e50;
          border: 3px solid #f1c40f;
          padding: 24px 32px;
          border-radius: 22px;
          max-width: 500px;
          width: 100%;
          text-align: center;
          color: #ecf0f1;
          box-shadow: 0 14px 36px rgba(0,0,0,0.6);
        }

        .guide-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 8px;
          text-align: left;
          font-size: 13px;
          margin: 14px 0 18px;
          background: rgba(0,0,0,0.3);
          padding: 12px;
          border-radius: 12px;
        }
        .guide-item {
          display: flex;
          align-items: center;
          gap: 6px;
        }
      </style>
    </head>
    <body>
      <div id="mine-stage" class="cursor-wood">
        <!-- 타이틀 & 도감 버튼 -->
        <div class="top-row">
          <h1 class="game-title">💎 두더지를 잡아라 <small style="font-size: 15px; color: #bdc3c7;">(GameN 광산 에디션)</small></h1>
          <button class="guide-btn" onclick="toggleGuide(true)">📖 등장 캐릭터 도감</button>
        </div>

        <!-- 망치 선택 바 -->
        <div class="hammer-bar">
          <button class="hammer-btn active" data-h="wood" onclick="setHammer('wood')">🪵 나무 망치 (기본)</button>
          <button class="hammer-btn" data-h="iron" onclick="setHammer('iron')">⛓️ 강철 망치 (헬멧 1타 격파!)</button>
          <button class="hammer-btn" data-h="golden" onclick="setHammer('golden')">✨ 황금 해머 (보석 점수 1.5배!)</button>
        </div>

        <!-- 스코어보드 & 타임/피버 게이지 -->
        <div class="hud-panel">
          <div class="hud-stats">
            <div class="score-box">SCORE: <span id="ui-score">0</span></div>
            <div class="fever-stars">
              <span id="ui-fever-txt" style="color:#f39c12;">콤보: 0</span>
              <span id="star-1" class="star-icon">💎</span>
              <span id="star-2" class="star-icon">💠</span>
              <span id="star-3" class="star-icon">👑</span>
            </div>
          </div>

          <div class="bar-wrap">
            <span class="bar-label">⏳ <span id="ui-time">01:00</span></span>
            <div class="bar-track">
              <div id="bar-time" class="time-fill"></div>
            </div>
          </div>

          <div class="bar-wrap" style="margin-bottom:0;">
            <span class="bar-label">🔥 피버게이지</span>
            <div class="bar-track">
              <div id="bar-fever" class="fever-fill"></div>
            </div>
          </div>
        </div>

        <!-- 3x3 광산 구멍 & 중앙 빅 홀(갓파더 보스/토끼 경관) -->
        <div class="stage-wrapper">
          <div class="mine-grid">
            <div class="crater-pit"><div class="mole-slot" id="hole-0"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-1"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-2"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-3"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-4"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-5"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-6"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-7"></div></div>
            <div class="crater-pit"><div class="mole-slot" id="hole-8"></div></div>
          </div>

          <!-- 중앙 대형 이벤트 홀 (갓파더 두더지 / 토끼 경관) -->
          <div id="big-hole-overlay">
            <div id="big-title" style="font-size: 26px; color: #f1c40f; margin-bottom: 10px; text-shadow: 2px 2px 0 #000;">
              👑 갓파더 보스 두더지 등장! 연타하세요!!
            </div>
            <div class="big-crater" id="big-target" onpointerdown="hitBigHole(event)">
              <div id="big-svg-box" style="width: 190px; height: 190px;"></div>
            </div>
          </div>
        </div>

        <button id="btn-play" class="action-btn" onclick="startGame()">🚀 광산 출동 (게임 시작!)</button>

        <!-- 캐릭터 도감 모달 -->
        <div id="modal-guide" class="modal-layer">
          <div class="modal-card">
            <h2 style="margin: 0; color: #f1c40f;">📖 다이아몬드 광산 가이드</h2>
            <div class="guide-grid">
              <div class="guide-item">🐹 <b>일반 두더지:</b> +555점</div>
              <div class="guide-item">💎 <b>보석 두더지:</b> +1,500~4,500점</div>
              <div class="guide-item">🪖 <b>안전모 두더지:</b> 2회 타격 (+1,000점)</div>
              <div class="guide-item">⏰ <b>시계 두더지:</b> 3회 타격 (+5,000점 & +5초)</div>
              <div class="guide-item">💣 <b>다이너마이트:</b> +2,000점 & 전체 올클리어!</div>
              <div class="guide-item">👑 <b>갓파더 보스:</b> 피버 4단계 광클 보너스!</div>
              <div class="guide-item" style="grid-column: span 2; color: #ff7675;">
                🐰 <b>토끼 경관 (주의!):</b> 때리면 <b>-10,000점 감점 + 피버 초기화 + 2초간 체포(조작불능)!</b>
              </div>
            </div>
            <button class="action-btn" style="padding: 8px 30px; font-size: 18px;" onclick="toggleGuide(false)">확인</button>
          </div>
        </div>

        <!-- 게임오버 모달 -->
        <div id="modal-over" class="modal-layer">
          <div class="modal-card">
            <h2 style="margin: 0 0 10px 0; font-size: 32px; color: #f1c40f;">🏁 TIME OVER!</h2>
            <p id="over-score" style="font-size: 26px; margin: 0 0 8px 0; color: #2ecc71;">최종 점수: 0점</p>
            <p id="over-high" style="font-size: 16px; margin: 0 0 22px 0; color: #bdc3c7;">최고 기록: 0점</p>
            <button class="action-btn" onclick="startGame()">🔄 다시 도전하기</button>
          </div>
        </div>
      </div>

      <script>
        // ==========================================
        // GameN '두더지를 잡아라' 캐릭터 SVG 아트워크
        // ==========================================

        // 0. 일반 도둑 두더지 (+555점)
        function svgNormalMole(hit) {
          if (hit) return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <path d="M16 105 C16 42, 25 22, 50 22 C75 22, 84 42, 84 105 Z" fill="#6d4224"/>
            <ellipse cx="50" cy="64" rx="22" ry="15" fill="#d9b189"/>
            <ellipse cx="50" cy="56" rx="8" ry="6" fill="#c0392b"/>
            <path d="M32 42 L42 50 M42 42 L32 50 M58 42 L68 50 M68 42 L58 50" stroke="#1a252f" stroke-width="3.5" stroke-linecap="round"/>
            <ellipse cx="66" cy="22" rx="10" ry="7" fill="#e74c3c"/>
            <ellipse cx="50" cy="68" rx="6" ry="4" fill="#922b21"/>
          </svg>`;
          return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <path d="M16 105 C16 42, 25 22, 50 22 C75 22, 84 42, 84 105 Z" fill="#8c5837"/>
            <!-- 도둑 복면 안대 -->
            <rect x="23" y="37" width="54" height="16" rx="6" fill="#2c3e50"/>
            <ellipse cx="37" cy="45" rx="4" ry="5" fill="#ffffff"/>
            <circle cx="37" cy="45" r="2.2" fill="#000"/>
            <ellipse cx="63" cy="45" rx="4" ry="5" fill="#ffffff"/>
            <circle cx="63" cy="45" r="2.2" fill="#000"/>
            <ellipse cx="50" cy="64" rx="22" ry="15" fill="#e8c29b"/>
            <ellipse cx="50" cy="56" rx="8" ry="6" fill="#e74c3c"/>
            <rect x="46" y="66" width="4" height="6" rx="1" fill="#fff"/>
            <rect x="50" y="66" width="4" height="6" rx="1" fill="#fff"/>
          </svg>`;
        }

        // 1. 보석(다이아몬드) 두더지 (피버 단계별 에메랄드/사파이어/루비: +1,500 / +3,000 / +4,500)
        function svgGemMole(step, hit) {
          const colors = ["#2ecc71", "#2ecc71", "#3498db", "#e74c3c", "#f1c40f"];
          const gemColor = colors[step] || "#3498db";
          return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <path d="M16 105 C16 42, 25 22, 50 22 C75 22, 84 42, 84 105 Z" fill="#7f5032"/>
            <ellipse cx="50" cy="60" rx="21" ry="14" fill="#e8c29b"/>
            ${hit ? `<path d="M32 38 L42 46 M42 38 L32 46 M58 38 L68 46 M68 38 L58 46" stroke="#1a252f" stroke-width="3.5"/>` : `
            <circle cx="37" cy="42" r="4.5" fill="#f1c40f"/>
            <circle cx="63" cy="42" r="4.5" fill="#f1c40f"/>`}
            <ellipse cx="50" cy="53" rx="7" ry="5" fill="#e74c3c"/>
            <!-- 품에 안고 있는 대형 보석 다이아몬드 -->
            <polygon points="36,70 64,70 72,82 50,104 28,82" fill="${gemColor}" stroke="#ffffff" stroke-width="2"/>
            <polygon points="36,70 64,70 58,82 42,82" fill="rgba(255,255,255,0.45)"/>
          </svg>`;
        }

        // 2. 안전모(헬멧) 광부 두더지 (2회 타격, +1,000점)
        function svgHelmetMole(hp) {
          return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <path d="M16 105 C16 45, 25 25, 50 25 C75 25, 84 45, 84 105 Z" fill="#8c5837"/>
            <!-- 철제 광부 헬멧 (hp==1 이면 금이 감) -->
            <path d="M18 36 C18 8, 82 8, 82 36 Z" fill="${hp === 2 ? '#f1c40f' : '#d4ac0d'}" stroke="#b7950b" stroke-width="2"/>
            <ellipse cx="50" cy="36" rx="35" ry="6" fill="#b7950b"/>
            <circle cx="50" cy="21" r="8" fill="#ecf0f1" stroke="#7f8c8d" stroke-width="2"/>
            <circle cx="50" cy="21" r="4" fill="#fff59d"/>
            ${hp === 1 ? `<path d="M40 12 L46 22 L38 28" stroke="#2c3e50" stroke-width="2.5" fill="none"/>` : ''}
            <ellipse cx="50" cy="64" rx="21" ry="15" fill="#e8c29b"/>
            <ellipse cx="50" cy="56" rx="8" ry="5.5" fill="#e74c3c"/>
            <circle cx="37" cy="46" r="4" fill="#2c3e50"/>
            <circle cx="63" cy="46" r="4" fill="#2c3e50"/>
          </svg>`;
        }

        // 3. 광산 다이너마이트 폭탄 두더지 (+2,000점 & 화면의 모든 두더지 동시 폭파 보너스!)
        function svgDynamite(boom) {
          if (boom) return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <polygon points="50,10 64,35 94,30 76,54 96,78 66,80 65,105 48,86 24,102 30,76 6,72 26,52 10,30 38,35" fill="#e74c3c"/>
            <polygon points="50,24 60,42 80,38 68,55 82,72 62,74 60,90 48,76 34,86 38,68 20,66 34,52 24,38 42,42" fill="#f1c40f"/>
            <text x="50" y="66" font-size="16" text-anchor="middle" fill="#000" font-weight="900">ALL BOOM!</text>
          </svg>`;
          return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <!-- 빨간 다이너마이트 묶음 -->
            <rect x="28" y="38" width="14" height="62" rx="4" fill="#e74c3c" stroke="#922b21" stroke-width="2"/>
            <rect x="43" y="34" width="14" height="66" rx="4" fill="#c0392b" stroke="#922b21" stroke-width="2"/>
            <rect x="58" y="38" width="14" height="62" rx="4" fill="#e74c3c" stroke="#922b21" stroke-width="2"/>
            <rect x="26" y="55" width="48" height="10" fill="#2c3e50"/>
            <rect x="26" y="78" width="48" height="10" fill="#2c3e50"/>
            <!-- 심지 & 스파크 -->
            <path d="M50 34 Q50 18 66 14" stroke="#f39c12" stroke-width="4" fill="none"/>
            <polygon points="66,14 73,7 71,14 78,13 73,18 79,22 71,22 68,28 66,20 59,18" fill="#f1c40f"/>
            <text x="50" y="74" font-size="13" text-anchor="middle" fill="#fff" font-weight="bold">TNT</text>
          </svg>`;
        }

        // 4. 토끼 경관 (절대 때리면 안 되는 경찰 캐릭터! -10,000점 & 체포)
        function svgPoliceRabbit(hit) {
          return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <!-- 긴 토끼 귀 -->
            <ellipse cx="34" cy="24" rx="8" ry="22" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="2"/>
            <ellipse cx="34" cy="24" rx="4" ry="15" fill="#ffb4a2"/>
            <ellipse cx="66" cy="24" rx="8" ry="22" fill="#ecf0f1" stroke="#bdc3c7" stroke-width="2"/>
            <ellipse cx="66" cy="24" rx="4" ry="15" fill="#ffb4a2"/>
            <!-- 얼굴/몸통 -->
            <path d="M20 105 C20 50, 28 36, 50 36 C72 36, 80 50, 80 105 Z" fill="#ffffff" stroke="#bdc3c7" stroke-width="2"/>
            <!-- 경찰 정모 (파란 모자 + 황금 배지) -->
            <path d="M24 42 C24 25, 76 25, 76 42 Z" fill="#2980b9" stroke="#1b4f72" stroke-width="2"/>
            <rect x="20" y="40" width="60" height="6" rx="3" fill="#1a252f"/>
            <polygon points="50,29 53,34 50,39 47,34" fill="#f1c40f"/>
            <!-- 표정 -->
            ${hit ? `
            <path d="M32 50 L43 56 M43 50 L32 56 M57 50 L68 56 M68 50 L57 56" stroke="#c0392b" stroke-width="3.5"/>
            <circle cx="50" cy="70" r="7" fill="#c0392b"/>` : `
            <circle cx="37" cy="54" r="4" fill="#2c3e50"/>
            <circle cx="63" cy="54" r="4" fill="#2c3e50"/>
            <ellipse cx="50" cy="60" rx="5" ry="3.5" fill="#ff7675"/>
            <!-- 호루라기/경광봉 -->
            <rect x="68" y="72" width="8" height="24" rx="3" fill="#e74c3c"/>`}
          </svg>`;
        }

        // 9. 황금 시계 두더지 (3회 타격 시 +5,000점 & 제한시간 +5초 연장!)
        function svgClockMole(hp) {
          return `
          <svg viewBox="0 0 100 110" width="100%" height="100%">
            <path d="M16 105 C16 42, 25 22, 50 22 C75 22, 84 42, 84 105 Z" fill="#d4ac0d"/>
            <ellipse cx="50" cy="58" rx="20" ry="13" fill="#fff9c4"/>
            <circle cx="37" cy="42" r="4" fill="#2c3e50"/>
            <circle cx="63" cy="42" r="4" fill="#2c3e50"/>
            <ellipse cx="50" cy="52" rx="7" ry="5" fill="#e67e22"/>
            <!-- 대형 자명종 시계 -->
            <circle cx="50" cy="82" r="20" fill="#ffffff" stroke="#e67e22" stroke-width="4"/>
            <line x1="50" y1="82" x2="50" y2="70" stroke="#2c3e50" stroke-width="3" stroke-linecap="round"/>
            <line x1="50" y1="82" x2="60" y2="82" stroke="#e74c3c" stroke-width="2.5" stroke-linecap="round"/>
          </svg>`;
        }

        // 5. 빅 홀 보스: '갓파더 두더지' (선글라스 + 중절모 + 황금 지팡이, 연타 시 타당 +777점)
        function svgGodfatherBoss(hit) {
          return `
          <svg viewBox="0 0 120 120" width="100%" height="100%">
            <!-- 보스 거대 몸집 & 정장 -->
            <path d="M12 115 C12 45, 25 26, 60 26 C95 26, 108 45, 108 115 Z" fill="#5c3818"/>
            <path d="M20 115 L40 82 L80 82 L100 115 Z" fill="#1a252f"/>
            <!-- 빨간 나비넥타이 -->
            <polygon points="48,84 72,96 72,84 48,96" fill="#e74c3c"/>
            <!-- 마피아 중절모 페도라 -->
            <ellipse cx="60" cy="30" rx="46" ry="8" fill="#1a252f"/>
            <path d="M26 30 C26 8, 94 8, 94 30 Z" fill="#2c3e50"/>
            <rect x="27" y="23" width="66" height="5" fill="#e74c3c"/>
            <!-- 선글라스 -->
            <rect x="28" y="42" width="26" height="14" rx="3" fill="#000" stroke="#f1c40f" stroke-width="2"/>
            <rect x="66" y="42" width="26" height="14" rx="3" fill="#000" stroke="#f1c40f" stroke-width="2"/>
            <line x1="54" y1="48" x2="66" y2="48" stroke="#f1c40f" stroke-width="3"/>
            <!-- 주둥이 & 시가 -->
            <ellipse cx="60" cy="68" rx="26" ry="15" fill="#e8c29b"/>
            <ellipse cx="60" cy="60" rx="10" ry="7" fill="#c0392b"/>
            <rect x="68" y="72" width="24" height="6" rx="2" fill="#784212" transform="rotate(12 68 72)"/>
            <circle cx="92" cy="77" r="3" fill="#e74c3c"/>
            ${hit ? `<text x="60" y="22" font-size="20" text-anchor="middle" fill="#f1c40f">💥 +777!</text>` : ''}
          </svg>`;
        }

        // ==========================================
        // 사운드 엔진 (Web Audio API)
        // ==========================================
        let actx = null;
        function getAudio() {
          if (!actx) actx = new (window.AudioContext || window.webkitAudioContext)();
          if (actx.state === 'suspended') actx.resume();
          return actx;
        }

        function playTone(freqStart, freqEnd, dur, type = 'triangle', vol = 0.5) {
          try {
            const c = getAudio();
            const osc = c.createOscillator();
            const g = c.createGain();
            osc.connect(g);
            g.connect(c.destination);
            osc.type = type;
            osc.frequency.setValueAtTime(freqStart, c.currentTime);
            osc.frequency.exponentialRampToValueAtTime(freqEnd, c.currentTime + dur);
            g.gain.setValueAtTime(vol, c.currentTime);
            g.gain.exponentialRampToValueAtTime(0.01, c.currentTime + dur);
            osc.start();
            osc.stop(c.currentTime + dur + 0.01);
          } catch(e) {}
        }

        function sfxSiren() {
          // 토끼 경관 사이렌 소리
          playTone(800, 1200, 0.2, 'sawtooth', 0.5);
          setTimeout(() => playTone(1200, 800, 0.25, 'sawtooth', 0.5), 200);
        }

        // ==========================================
        // GameN 원작 밸런스 & 게임 상태 관리
        // ==========================================
        const TOTAL_TIME_MS = 60000;      // 원작과 동일한 60초(1분)
        const COMBO_TARGET = 12;          // 피버 단계 업에 필요한 콤보 수
        const COMBO_TIMEOUT_MS = 1800;    // 콤보 유지 제한 시간
        const BOSS_DURATION_MS = 3500;    // 갓파더 보스 난타 시간

        // 원작 GameBoard.ts의 mole_point_arr 그대로 반영
        const MOLE_POINTS = {
          0: 555,     // 일반 도둑 두더지
          1: 1500,    // 보석 1단계 (에메랄드)
          2: 1000,    // 안전모 두더지 (2타)
          3: 2000,    // 다이너마이트 (전체 폭파)
          4: -10000,  // 토끼 경관 (감점!)
          5: 777,     // 갓파더 보스 타당 점수
          6: 1500,    // 보석 1단계
          7: 3000,    // 보석 2단계 (사파이어)
          8: 4500,    // 보석 3단계 (루비)
          9: 5000     // 시계 두더지 (3타 + 5초 추가)
        };

        // 스폰 확률 테이블 (원작 appearRandom_arr 기반)
        const SPAWN_POOL = [0,0,0,0,0, 1,1,1,1,1,1, 2,2,2, 3, 4,4, 9];

        let hammerType = 'wood';
        let isPlaying = false;
        let isPoliceFrozen = false;
        let isBossActive = false;

        let score = 0;
        let highScore = 0;
        let remainMs = TOTAL_TIME_MS;
        let comboCount = 0;
        let feverStep = 0; // 0: 일반, 1: 에메랄드, 2: 사파이어, 3: 루비, 4: 갓파더 보스 출현!
        let lastHitTime = 0;

        let mainLoopId = null;
        let spawnLoopId = null;
        let lastHoleIdx = -1;

        const stageEl = document.getElementById('mine-stage');
        const scoreEl = document.getElementById('ui-score');
        const timeTxtEl = document.getElementById('ui-time');
        const timeBarEl = document.getElementById('bar-time');
        const feverBarEl = document.getElementById('bar-fever');
        const feverTxtEl = document.getElementById('ui-fever-txt');
        const bigOverlay = document.getElementById('big-hole-overlay');
        const bigTitle = document.getElementById('big-title');
        const bigSvgBox = document.getElementById('big-svg-box');
        const playBtn = document.getElementById('btn-play');

        // 9개 홀 슬롯 초기화
        const holes = [];
        for (let i = 0; i < 9; i++) {
          const el = document.getElementById('hole-' + i);
          const slot = {
            idx: i,
            el: el,
            type: -1,
            hp: 0,
            isUp: false,
            timer: null
          };
          el.addEventListener('pointerdown', (e) => {
            e.stopPropagation();
            onHoleClick(slot);
          });
          holes.push(slot);
        }

        window.toggleGuide = function(show) {
          document.getElementById('modal-guide').style.display = show ? 'flex' : 'none';
        };

        window.setHammer = function(type) {
          hammerType = type;
          document.querySelectorAll('.hammer-btn').forEach(b => {
            b.classList.toggle('active', b.dataset.h === type);
          });
          stageEl.classList.remove('cursor-wood', 'cursor-iron', 'cursor-golden');
          stageEl.classList.add('cursor-' + type);
        };

        function formatComma(n) {
          return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }

        function spawnPopup(parentEl, text, color = '#f1c40f') {
          const pop = document.createElement('div');
          pop.className = 'floating-pop';
          pop.style.color = color;
          pop.textContent = text;
          parentEl.appendChild(pop);
          setTimeout(() => pop.remove(), 650);
        }

        function addScore(type, parentEl) {
          let pts = MOLE_POINTS[type] || 555;
          // 황금 해머 장착 시 보석 두더지 점수 1.5배!
          if (hammerType === 'golden' && (type === 1 || type === 6 || type === 7 || type === 8)) {
            pts = Math.round(pts * 1.5);
          }
          score = Math.max(0, score + pts);
          scoreEl.textContent = formatComma(score);

          if (parentEl) {
            const sign = pts >= 0 ? `+${formatComma(pts)}` : `${formatComma(pts)}`;
            const col = pts >= 0 ? '#f1c40f' : '#ff5252';
            spawnPopup(parentEl, sign, col);
          }
        }

        function updateFeverUI() {
          const pct = Math.min(100, Math.round((comboCount / COMBO_TARGET) * 100));
          feverBarEl.style.width = pct + '%';
          feverTxtEl.textContent = feverStep > 0 ? `FEVER ${feverStep}단 (${comboCount}/${COMBO_TARGET})` : `콤보: ${comboCount}/${COMBO_TARGET}`;

          document.getElementById('star-1').classList.toggle('on', feverStep >= 1);
          document.getElementById('star-2').classList.toggle('on', feverStep >= 2);
          document.getElementById('star-3').classList.toggle('on', feverStep >= 3);

          stageEl.classList.remove('fever-step-1', 'fever-step-2', 'fever-step-3', 'fever-boss');
          if (feverStep === 1) stageEl.classList.add('fever-step-1');
          else if (feverStep === 2) stageEl.classList.add('fever-step-2');
          else if (feverStep === 3) stageEl.classList.add('fever-step-3');
          else if (feverStep === 4) stageEl.classList.add('fever-boss');
        }

        function registerCombo() {
          const now = Date.now();
          if (lastHitTime > 0 && (now - lastHitTime > COMBO_TIMEOUT_MS)) {
            comboCount = 1;
          } else {
            comboCount++;
          }
          lastHitTime = now;

          if (comboCount >= COMBO_TARGET) {
            comboCount = 0;
            if (feverStep < 4) {
              feverStep++;
              playTone(400, 900, 0.25, 'sine', 0.6);
              if (feverStep === 4) {
                startBossTime();
              }
            }
          }
          updateFeverUI();
        }

        function resetFever() {
          comboCount = 0;
          feverStep = 0;
          lastHitTime = 0;
          updateFeverUI();
        }

        // 구멍에서 캐릭터 올라오기
        function popUpHole(slot, type) {
          slot.type = type;
          slot.isUp = true;

          // 체력 설정 (안전모=2, 시계=3, 단 강철망치면 안전모 1타)
          if (type === 2) {
            slot.hp = (hammerType === 'iron') ? 1 : 2;
          } else if (type === 9) {
            slot.hp = 3;
          } else {
            slot.hp = 1;
          }

          renderSlotGraphic(slot, false);
          slot.el.classList.add('up');
          playTone(250, 500, 0.07, 'sine', 0.15);

          const stayTime = feverStep > 0 ? 900 : 1050;
          slot.timer = setTimeout(() => {
            if (slot.isUp) hideSlot(slot);
          }, stayTime);
        }

        function renderSlotGraphic(slot, isHit) {
          const t = slot.type;
          let html = '';
          if (t === 0) html = svgNormalMole(isHit);
          else if (t === 1 || t === 6) html = svgGemMole(1, isHit);
          else if (t === 7) html = svgGemMole(2, isHit);
          else if (t === 8) html = svgGemMole(3, isHit);
          else if (t === 2) html = svgHelmetMole(slot.hp);
          else if (t === 3) html = svgDynamite(isHit);
          else if (t === 4) html = svgPoliceRabbit(isHit);
          else if (t === 9) html = svgClockMole(slot.hp);

          if (!isHit && slot.hp > 1) {
            html += `<div class="hp-badge">${slot.hp}타</div>`;
          }
          slot.el.innerHTML = html;
        }

        function hideSlot(slot) {
          slot.isUp = false;
          slot.type = -1;
          slot.el.classList.remove('up');
          if (slot.timer) {
            clearTimeout(slot.timer);
            slot.timer = null;
          }
        }

        // 두더지 클릭 판정 (GameN GameBoard.ts holeClick 로직 그대로)
        function onHoleClick(slot) {
          if (!isPlaying || isPoliceFrozen || isBossActive || !slot.isUp) return;

          const t = slot.type;
          const parentPit = slot.el.parentElement;

          // 1) 토끼 경관(4)을 잘못 때린 경우 -> 사이렌 + -10,000점 + 피버 리셋 + 1.8초간 경찰 체포 연출!
          if (t === 4) {
            sfxSiren();
            renderSlotGraphic(slot, true);
            addScore(4, parentPit);
            resetFever();
            triggerPoliceArrest();
            setTimeout(() => hideSlot(slot), 300);
            return;
          }

          // 2) 다이너마이트(3)를 터뜨린 경우 -> 스테이지 진동 + 현재 나와 있는 모든 두더지 동시 폭파 올클리어!
          if (t === 3) {
            playTone(180, 45, 0.35, 'sawtooth', 0.8);
            stageEl.classList.add('shake');
            setTimeout(() => stageEl.classList.remove('shake'), 360);

            renderSlotGraphic(slot, true);
            addScore(3, parentPit);
            registerCombo();

            // 다른 모든 구멍의 두더지(토끼 경관 제외) 동시 획득 처리!
            holes.forEach(other => {
              if (other !== slot && other.isUp && other.type !== 4) {
                addScore(other.type, other.el.parentElement);
                renderSlotGraphic(other, true);
                setTimeout(() => hideSlot(other), 220);
              }
            });

            setTimeout(() => hideSlot(slot), 260);
            return;
          }

          // 3) 일반 / 보석 / 안전모 / 시계 두더지 타격
          slot.hp--;
          if (slot.hp > 0) {
            // 아직 체력이 남은 경우 (깡! 헬멧 타격음)
            playTone(750, 300, 0.08, 'square', 0.5);
            renderSlotGraphic(slot, false);
            spawnPopup(parentPit, `깡! (${slot.hp}타 남음)`, '#ecf0f1');
          } else {
            // 격파 완료!
            playTone(620, 120, 0.12, 'triangle', 0.6);
            renderSlotGraphic(slot, true);
            addScore(t, parentPit);
            registerCombo();

            // 시계 두더지(9) 격파 시 제한시간 +5초 보너스!
            if (t === 9) {
              remainMs = Math.min(TOTAL_TIME_MS, remainMs + 5000);
              spawnPopup(parentPit, '⏰ +5초 시간연장!', '#2ecc71');
            }

            if (slot.timer) clearTimeout(slot.timer);
            slot.timer = setTimeout(() => hideSlot(slot), 200);
          }
        }

        // 토끼 경관 체포 패널티 연출 (BigHole.ts rabbitStart 재현)
        function triggerPoliceArrest() {
          isPoliceFrozen = true;
          bigOverlay.style.display = 'flex';
          bigTitle.innerHTML = '🚨 삐용삐용! 토끼 경관을 공격하여 잠시 체포됩니다! (-10,000점)';
          bigTitle.style.color = '#ff7675';
          bigSvgBox.innerHTML = svgPoliceRabbit(false);

          setTimeout(() => {
            if (!isBossActive) bigOverlay.style.display = 'none';
            isPoliceFrozen = false;
          }, 1600);
        }

        // 피버 4단계: 갓파더 보스 두더지 등장! (BigHole.ts bossUp 재현)
        function startBossTime() {
          isBossActive = true;
          holes.forEach(h => hideSlot(h));

          bigOverlay.style.display = 'flex';
          bigTitle.innerHTML = '👑 갓파더 보스 두더지 출현!! 제한시간 내 마구 연타하세요!!';
          bigTitle.style.color = '#f1c40f';
          bigSvgBox.innerHTML = svgGodfatherBoss(false);

          setTimeout(() => {
            isBossActive = false;
            bigOverlay.style.display = 'none';
            resetFever();
          }, BOSS_DURATION_MS);
        }

        window.hitBigHole = function(e) {
          e.preventDefault();
          if (!isPlaying || !isBossActive) return;

          playTone(720, 150, 0.09, 'square', 0.65);
          addScore(5, document.getElementById('big-target'));
          bigSvgBox.innerHTML = svgGodfatherBoss(true);
          setTimeout(() => {
            if (isBossActive) bigSvgBox.innerHTML = svgGodfatherBoss(false);
          }, 100);
        };

        // 스폰 스케줄러
        function scheduleNextSpawn() {
          if (!isPlaying) return;

          if (!isBossActive && !isPoliceFrozen) {
            const emptyHoles = holes.filter(h => !h.isUp && h.idx !== lastHoleIdx);
            if (emptyHoles.length > 0) {
              const target = emptyHoles[Math.floor(Math.random() * emptyHoles.length)];
              lastHoleIdx = target.idx;

              let rawType = SPAWN_POOL[Math.floor(Math.random() * SPAWN_POOL.length)];
              // 원작 규칙: 보석 두더지(1)는 피버 단계에 따라 고득점 보석(6,7,8)으로 진화!
              if (rawType === 1) {
                if (feverStep === 0) rawType = 0; // 비피버 시 일반 두더지 혹은 1단계 보석
                else rawType = 5 + Math.min(3, feverStep); // 6(1500), 7(3000), 8(4500)
              }
              popUpHole(target, rawType);
            }
          }

          const delay = feverStep > 0 ? 340 : 460;
          spawnLoopId = setTimeout(scheduleNextSpawn, delay);
        }

        window.startGame = function() {
          getAudio();
          document.getElementById('modal-over').style.display = 'none';
          bigOverlay.style.display = 'none';

          isPlaying = true;
          isPoliceFrozen = false;
          isBossActive = false;
          score = 0;
          remainMs = TOTAL_TIME_MS;
          scoreEl.textContent = '0';
          resetFever();
          holes.forEach(h => hideSlot(h));

          playBtn.disabled = true;
          playBtn.style.opacity = '0.5';
          playBtn.textContent = '⛏️ 다이아몬드 광산 소탕 작전 진행 중...';

          if (mainLoopId) clearInterval(mainLoopId);
          if (spawnLoopId) clearTimeout(spawnLoopId);

          mainLoopId = setInterval(() => {
            // 보스 타임 중에는 원작처럼 타이머가 흐르지 않음
            if (!isBossActive) {
              remainMs -= 100;
            }
            if (remainMs <= 0) {
              remainMs = 0;
              endGame();
            }

            // 시간 텍스트 & 게이지 업데이트
            const sec = Math.ceil(remainMs / 1000);
            const m = Math.floor(sec / 60);
            const s = sec % 60;
            timeTxtEl.textContent = `0${m}:${s < 10 ? '0'+s : s}`;

            const pct = (remainMs / TOTAL_TIME_MS) * 100;
            timeBarEl.style.width = pct + '%';
            timeBarEl.classList.toggle('danger', pct <= 20);
          }, 100);

          scheduleNextSpawn();
        };

        function endGame() {
          isPlaying = false;
          clearInterval(mainLoopId);
          clearTimeout(spawnLoopId);
          holes.forEach(h => hideSlot(h));
          bigOverlay.style.display = 'none';

          playBtn.disabled = false;
          playBtn.style.opacity = '1';
          playBtn.textContent = '🚀 광산 출동 (게임 시작!)';

          if (score > highScore) highScore = score;

          document.getElementById('over-score').textContent = `최종 점수: ${formatComma(score)}점`;
          document.getElementById('over-high').textContent = `최고 기록: ${formatComma(highScore)}점`;
          document.getElementById('modal-over').style.display = 'flex';
        }
      </script>
    </body>
    </html>
    """, width="100%", height="730px")

    game
    return (game,)


if __name__ == "__main__":
    app.run()
