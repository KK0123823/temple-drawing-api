import os
from uuid import uuid4
from datetime import datetime
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== 上傳資料夾 =====
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ===== 靜態檔掛載 =====
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

PUBLIC_BASE_URL = "https://eloquent-footprint-applaud.ngrok-free.dev"


@app.get("/", response_class=HTMLResponse)
async def homepage():
    hero_image = "/uploads/廟宇logo.png"

    html = f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>臺灣廟宇文化虛實互動平台</title>
        <style>
            body {{
                margin: 0;
                font-family: "Microsoft JhengHei", "Noto Sans TC", sans-serif;
                background: linear-gradient(180deg, #f6e9d8 0%, #f0dcc4 100%);
                color: #3E2C23;
            }}

            .container {{
                max-width: 1100px;
                margin: 0 auto;
                padding: 24px 18px 40px;
            }}

            .hero {{
                background: linear-gradient(135deg, #fff9f2 0%, #fff4e8 100%);
                border: 3px solid #D4AF37;
                border-radius: 28px;
                box-shadow: 0 14px 32px rgba(0,0,0,0.12);
                padding: 32px 26px;
                display: grid;
                grid-template-columns: 1.1fr 1fr;
                gap: 28px;
                align-items: center;
            }}

            .hero-text {{
                display: flex;
                flex-direction: column;
                gap: 16px;
            }}

            .badge {{
                display: inline-block;
                width: fit-content;
                background: #8B0000;
                color: white;
                padding: 7px 14px;
                border-radius: 999px;
                font-size: 0.95rem;
                font-weight: 700;
            }}

            .title {{
                font-size: 3rem;
                line-height: 1.2;
                font-weight: 900;
                color: #6f1d1b;
                margin: 0;
            }}

            .subtitle {{
                font-size: 1.2rem;
                line-height: 1.9;
                color: #5c4033;
                margin: 0;
            }}

            .hero-actions {{
                display: flex;
                gap: 14px;
                flex-wrap: wrap;
                margin-top: 8px;
            }}

            .btn {{
                text-decoration: none;
                padding: 14px 22px;
                border-radius: 14px;
                font-weight: 800;
                transition: 0.2s ease;
                display: inline-block;
                font-size: 1rem;
            }}

            .btn-primary {{
                background: #8B0000;
                color: white;
            }}

            .btn-primary:hover {{
                background: #6f0000;
            }}

            .btn-secondary {{
                background: #D4AF37;
                color: #3E2C23;
            }}

            .btn-secondary:hover {{
                background: #c59b19;
            }}

            .hero-image-wrap {{
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .hero-image {{
                width: 100%;
                max-width: 460px;
                border-radius: 20px;
                border: 3px solid rgba(212,175,55,0.55);
                box-shadow: 0 10px 24px rgba(0,0,0,0.18);
                background: #10202b;
            }}

            .section {{
                margin-top: 28px;
                background: #fffaf3;
                border-radius: 24px;
                padding: 26px 22px;
                border: 2px solid #ead1a8;
                box-shadow: 0 10px 24px rgba(0,0,0,0.06);
            }}

            .section-title {{
                font-size: 1.8rem;
                font-weight: 900;
                color: #8B0000;
                margin-bottom: 16px;
            }}

            .grid-3 {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
            }}

            .feature-card {{
                background: #fff4e6;
                border-radius: 18px;
                padding: 20px 18px;
                border-left: 6px solid #D4AF37;
                box-shadow: 0 6px 14px rgba(0,0,0,0.05);
            }}

            .feature-card h3 {{
                margin: 0 0 10px;
                color: #6f1d1b;
                font-size: 1.15rem;
            }}

            .feature-card p {{
                margin: 0;
                line-height: 1.85;
                color: #4a3426;
            }}

            .learning-box {{
                background: #fff3e0;
                border-radius: 18px;
                padding: 18px 20px;
                line-height: 1.95;
                border-left: 6px solid #8B0000;
                color: #4a3426;
            }}

            .footer {{
                text-align: center;
                margin-top: 26px;
                color: #8a6a52;
                font-size: 1rem;
            }}

            @media (max-width: 900px) {{
                .hero {{
                    grid-template-columns: 1fr;
                    text-align: center;
                }}

                .hero-text {{
                    align-items: center;
                }}

                .grid-3 {{
                    grid-template-columns: 1fr;
                }}

                .title {{
                    font-size: 2.3rem;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">

            <section class="hero">
                <div class="hero-text">
                    <div class="badge">AI × XR × 廟宇文化 × 玩中學</div>
                    <h1 class="title">臺灣廟宇文化<br>虛實互動平台</h1>
                    <p class="subtitle">
                        結合 VR、RAG、LLM 與互動任務設計，將臺灣廟宇文化轉化為可探索、可創作、可分享的學習體驗。
                        使用者不只是在看文化，而是在沉浸式場景中透過問答、描繪與互動任務主動理解文化。
                    </p>
                    <div class="hero-actions">
                        <a class="btn btn-primary" href="#features">查看功能亮點</a>
                        <a class="btn btn-secondary" href="#learning">了解玩中學理念</a>
                    </div>
                </div>

                <div class="hero-image-wrap">
                    <img class="hero-image" src="{hero_image}" alt="臺灣廟宇文化虛實互動平台主視覺">
                </div>
            </section>

            <section class="section" id="features">
                <div class="section-title">平台功能亮點</div>
                <div class="grid-3">
                    <div class="feature-card">
                        <h3>◆ VR 沉浸式文化互動</h3>
                        <p>
                            學習者可在虛擬廟宇場景中進行探索、觀察與互動，
                            透過第一人稱視角提升參與感與文化臨場感。
                        </p>
                    </div>

                    <div class="feature-card">
                        <h3>◆ AI 智慧導覽與問答</h3>
                        <p>
                            結合 RAG 與 LLM 技術，讓系統能針對廟宇建築、
                            神明文化與場景知識提供即時回應與教學式解說。
                        </p>
                    </div>

                    <div class="feature-card">
                        <h3>◆ VR 創作成果展示</h3>
                        <p>
                            使用者可於 VR 中進行描繪與創作，完成作品後透過 QR Code
                            將成果延伸至手機端，實現保存、展示與分享。
                        </p>
                    </div>
                </div>
            </section>

            <section class="section" id="learning">
                <div class="section-title">為什麼把廟宇專題和畫畫結合？</div>
                <div class="learning-box">
                    本系統以「玩中學」為核心，透過繪畫互動引導學習者觀察文昌帝君的造型特徵，
                    將文化知識轉化為主動學習體驗，提升理解與記憶效果。
                    文昌帝君作為與學業、智慧與文章相關的重要神祇，
                    與學生學習情境高度連結，因此特別適合作為互動創作與文化認識的主題。
                </div>
            </section>

            <div class="footer">
                文化學習 × VR 互動 × AI 問答 × 跨裝置分享
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.post("/upload_drawing")
async def upload_drawing(file: UploadFile = File(...)):
    original_name = file.filename or "drawing.png"
    ext = os.path.splitext(original_name)[1].lower()

    if ext == "":
        ext = ".png"

    filename = f"{uuid4().hex}{ext}"
    save_path = os.path.join(UPLOAD_DIR, filename)

    content = await file.read()
    with open(save_path, "wb") as f:
        f.write(content)

    page_url = f"{PUBLIC_BASE_URL}/view/{filename}"

    return {
        "success": True,
        "filename": filename,
        "url": page_url,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }


@app.get("/view/{filename}", response_class=HTMLResponse)
async def view_drawing(filename: str):
    image_url = f"/uploads/{filename}"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    html = f"""
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VR 創作成果展示</title>
        <style>
            body {{
                margin: 0;
                font-family: "Microsoft JhengHei", "Noto Sans TC", sans-serif;
                background: linear-gradient(180deg, #f5e6d3 0%, #f0dcc4 100%);
                color: #3E2C23;
            }}

            .container {{
                max-width: 900px;
                margin: 0 auto;
                padding: 24px 18px 40px;
            }}

            .card {{
                background: #fffaf3;
                border-radius: 24px;
                padding: 24px;
                border: 3px solid #D4AF37;
                box-shadow: 0 12px 28px rgba(0,0,0,0.12);
            }}

            .title {{
                font-size: 2.2rem;
                font-weight: 900;
                text-align: center;
                color: #8B0000;
                margin-bottom: 10px;
            }}

            .subtitle {{
                text-align: center;
                color: #7a4d2b;
                font-size: 1.15rem;
                margin-bottom: 24px;
            }}

            .section-title {{
                font-size: 1.4rem;
                font-weight: 900;
                color: #8B0000;
                margin: 14px 0 12px;
            }}

            .image-wrap {{
                display: flex;
                justify-content: center;
                margin: 18px 0 28px;
            }}

            .image-wrap img {{
                max-width: 100%;
                border-radius: 16px;
                border: 10px solid #D4AF37;
                background: white;
                box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            }}

            .info {{
                background: #fff3e0;
                border-radius: 16px;
                padding: 18px 20px;
                line-height: 1.9;
                margin-bottom: 20px;
                border-left: 6px solid #8B0000;
            }}

            .info p {{
                margin: 0 0 10px;
            }}

            .label {{
                font-weight: 800;
                color: #7a4d2b;
            }}

            .actions {{
                display: flex;
                gap: 14px;
                flex-wrap: wrap;
                justify-content: center;
                margin-top: 22px;
            }}

            .btn {{
                text-decoration: none;
                padding: 14px 24px;
                border-radius: 14px;
                font-weight: 800;
                transition: 0.2s ease;
                display: inline-block;
                font-size: 1.1rem;
            }}

            .btn-primary {{
                background: #d07a33;
                color: white;
            }}

            .btn-primary:hover {{
                background: #b96625;
            }}

            .btn-secondary {{
                background: #eadbc8;
                color: #5b3d2b;
            }}

            .btn-secondary:hover {{
                background: #dfcdb6;
            }}

            .footer {{
                text-align: center;
                margin-top: 24px;
                color: #8a6a52;
                font-size: 1rem;
                line-height: 1.8;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                <div class="title">臺灣廟宇文化虛實互動平台</div>
                <div class="subtitle">VR 小遊戲繪畫創作成果展示</div>

                <div class="image-wrap">
                    <img src="{image_url}" alt="作品圖片">
                </div>

                <div class="info">
                    <p><span class="label">作品名稱：</span>神明描繪創作</p>
                    <p><span class="label">創作來源：</span>VR 沉浸式互動學習場景</p>
                    <p><span class="label">創作時間：</span>{now}</p>
                    <p><span class="label">作品說明：</span>本作品由使用者於 VR 沉浸式文化學習場景中完成，系統透過 QR Code 機制將虛擬創作成果延伸至行動裝置端，實現文化學習成果之保存、展示與分享。</p>
                </div>

                <div class="section-title">認識文昌帝君</div>
                <div class="info">
                    <p>
                        文昌帝君是臺灣民間信仰中與學業、智慧、文章與考試運勢密切相關的重要神祇，常被視為守護學生與考生的文運之神。透過文昌帝君為核心案例，引導學習者從神像造型與文化意涵中，認識臺灣廟宇文化與學習信仰之連結。
                    </p>
                </div>

                <div class="section-title">玩中學設計</div>
                <div class="info">
                    <p>
                        透過繪畫互動，引導學習者觀察文昌帝君特徵，
                        將文化知識轉化為主動學習體驗。
                    </p>
                </div>

                <div class="actions">
                    <a class="btn btn-primary" href="{image_url}" download>下載作品</a>
                    <a class="btn btn-secondary" href="/">返回首頁</a>
                </div>

                <div class="footer">
                    文化學習 × VR 互動 × 跨裝置分享
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)