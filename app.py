from flask import Flask, render_template_string

app = Flask(__name__)

GALLERY_PHOTOS = [
    {
        "filename": "933681-gallery-7mfzYYu71g.jpg",
        "caption": "Momen Studio Penuh Makna",
    },
    {
        "filename": "933681-gallery-HakA3ItzCC.jpg",
        "caption": "Anggun & Berkah",
    },
    {
        "filename": "933681-gallery-hvPkCE1H63.jpg",
        "caption": "Cahaya Senja Bersama",
    },
    {
        "filename": "933681-gallery-shgbZWWMta.jpg",
        "caption": "Langkah Sejiwa",
    },
    {
        "filename": "933681-gallery-VVKCB3amIN.jpg",
        "caption": "Harmoni dalam Balutan Putih",
    },
    {
        "filename": "933681-gallery-YxxfQV87lL.jpg",
        "caption": "Menuju Hari Bahagia",
    },
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Happy Wedding — Andi Ridwanto & Vita Ayu Nilam Nur Aini</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    /* Sesuaikan variabel warna di bawah ini agar persis dengan tone warna pada link */
    :root {
      --bg-main: #FAF6F0;
      --bg-card: #FFFFFF;
      --bg-soft: #F2EAE0;
      --primary: #6E4F3A;
      --primary-dark: #4A3324;
      --accent: #B88A58;
      --text-main: #2E241E;
      --text-muted: #6E5F56;
      --border-soft: #E5D8C8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      line-height: 1.7;
    }

    .container {
      max-width: 980px;
      margin: 0 auto;
      padding: 24px 18px 64px;
    }

    .hero {
      background: linear-gradient(160deg, var(--bg-card) 0%, var(--bg-soft) 100%);
      border: 1px solid var(--border-soft);
      border-radius: 24px;
      padding: 44px 28px;
      text-align: center;
      box-shadow: 0 12px 32px rgba(74, 51, 36, 0.06);
      margin-bottom: 36px;
    }

    .guest-badge {
      display: inline-block;
      background-color: var(--bg-main);
      color: var(--primary);
      border: 1px solid var(--border-soft);
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 500;
      margin-bottom: 16px;
    }

    .eyebrow {
      text-transform: uppercase;
      letter-spacing: 3px;
      font-size: 0.78rem;
      color: var(--accent);
      font-weight: 600;
      margin-bottom: 10px;
    }

    h1.couple-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(2.1rem, 5vw, 3.4rem);
      font-weight: 700;
      color: var(--primary-dark);
      line-height: 1.2;
      margin-bottom: 14px;
    }

    .wedding-date {
      display: inline-block;
      font-size: 1rem;
      font-weight: 600;
      color: var(--primary);
      padding: 8px 20px;
      border-top: 1px solid var(--border-soft);
      border-bottom: 1px solid var(--border-soft);
      margin-bottom: 20px;
    }

    .greeting-text {
      max-width: 680px;
      margin: 0 auto;
      color: var(--text-muted);
      font-size: 1rem;
    }

    .section-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-soft);
      border-radius: 20px;
      padding: 32px 26px;
      margin-bottom: 36px;
      box-shadow: 0 8px 24px rgba(74, 51, 36, 0.04);
    }

    .section-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: 2rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-align: center;
      margin-bottom: 16px;
    }

    .divider {
      width: 64px;
      height: 2px;
      background-color: var(--accent);
      margin: 0 auto 24px;
    }

    .prayer-box {
      background-color: var(--bg-soft);
      border-left: 4px solid var(--accent);
      border-radius: 12px;
      padding: 22px 24px;
      font-style: italic;
      color: var(--text-main);
    }

    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 20px;
    }

    .photo-card {
      background-color: var(--bg-main);
      border: 1px solid var(--border-soft);
      border-radius: 16px;
      overflow: hidden;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }

    .photo-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 24px rgba(74, 51, 36, 0.1);
    }

    .photo-card img {
      width: 100%;
      height: 360px;
      object-fit: cover;
      object-position: top center;
      display: block;
    }

    .photo-caption {
      padding: 12px 14px;
      font-size: 0.9rem;
      color: var(--primary-dark);
      text-align: center;
      font-weight: 500;
    }

    footer {
      text-align: center;
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-top: 16px;
    }
  </style>
</head>
<body>
  <div class="container">
    <header class="hero">
      <div class="guest-badge">From Nur Wahid</div>
      <div class="eyebrow">Happy Wedding</div>
      <h1 class="couple-title">Andi Ridwanto &amp; Vita Ayu Nilam Nur Aini</h1>
      <div class="wedding-date">Minggu, 29 November 2026</div>
      <p class="greeting-text">
        Selamat menempuh hidup baru untuk <strong>Andi Ridwanto</strong> dan
        <strong>Vita Ayu Nilam Nur Aini</strong>. Semoga cinta, ketenangan, dan
        kebahagiaan senantiasa menyertai setiap langkah perjalanan rumah tangga kalian.
      </p>
    </header>

    <section class="section-card">
      <h2 class="section-title">Doa Terbaik</h2>
      <div class="divider"></div>
      <div class="prayer-box">
        <p>
          &ldquo;Barakallahu laka wa baraka &lsquo;alaika wa jama&rsquo;a bainakuma fii khair.
          Semoga Allah SWT melimpahkan keberkahan kepada Andi Ridwanto dan Vita Ayu Nilam Nur Aini,
          menjadikan keluarga yang sakinah, mawaddah, wa rahmah, dikaruniai rezeki yang halal dan
          berkah, serta senantiasa saling menguatkan dalam suka maupun duka hingga akhir hayat.&rdquo;
        </p>
      </div>
    </section>

    <section class="section-card">
      <h2 class="section-title">Galeri Foto</h2>
      <div class="divider"></div>
      <div class="gallery-grid">
        {% for photo in photos %}
        <article class="photo-card">
          <img src="{{ url_for('static', filename='images/' + photo.filename) }}" alt="{{ photo.caption }}" />
          <div class="photo-caption">{{ photo.caption }}</div>
        </article>
        {% endfor %}
      </div>
    </section>

    <footer>
      Ucapan Bahagia untuk Andi Ridwanto &amp; Vita Ayu Nilam Nur Aini &bull; 29 November 2026
    </footer>
  </div>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, photos=GALLERY_PHOTOS)


if __name__ == "__main__":
    app.run(debug=True)