from flask import Flask, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>DAMZIEARK WEB SOLUTION</title>
        <style>
            body{font-family:Arial; margin:0; background:#f0f2f5; color:#222}
            header{background:linear-gradient(135deg,#0d1117,#2a0845); color:white; padding:35px 20px; text-align:center}
            header h1{margin:0; font-size:27px}
            .tag{background:#ff6a00; padding:6px 14px; border-radius:20px; font-size:14px; display:inline-block; margin-top:8px}
            .container{padding:20px; padding-bottom:90px}
            .card{background:white; border-radius:16px; padding:20px; margin-bottom:18px; box-shadow:0 4px 12px rgba(0,0,0,0.1); animation: pop 0.5s}
            @keyframes pop{from{transform:scale(0.9); opacity:0} to{transform:scale(1); opacity:1}}
            .price{color:green; font-weight:bold; font-size:20px}
            .btn{display:block; background:#25D366; color:white; text-align:center; padding:14px; border-radius:10px; text-decoration:none; font-weight:bold; margin-top:12px; font-size:16px}
            .btn-blue{background:#0d1117}
            input, textarea, select{width:100%; padding:12px; margin:8px 0; border-radius:10px; border:1px solid #ccc; box-sizing:border-box; font-size:15px}
            img{width:100%; border-radius:14px; margin-top:10px}
            .grid{display:grid; grid-template-columns:1fr 1fr; gap:10px}
            .sticker{font-size:28px}
            .floating-wa{position:fixed; bottom:20px; right:20px; background:#25D366; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:35px; box-shadow:0 4px 15px rgba(0,0,0,0.3); text-decoration:none; animation: bounce 2s infinite; z-index:999}
            @keyframes bounce{0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)}}
        </style>
    </head>
    <body>
        <header>
            <div class="sticker">💻🔥🚀</div>
            <h1>DAMZIEARK WEB SOLUTION</h1>
            <p>📍 Lagos State, Nigeria - We Dey Everywhere!</p>
            <span class="tag">💰 Very Cheap and Affordable 💰</span>
        </header>

        <div class="container">
            <div class="card">
                <div class="sticker">✨💼✨</div>
                <h2>🔥 Wetin I Dey Do 🔥</h2>
                <p>✅ 🏢 Business Website (Jumia Style)</p>
                <p>✅ 👨‍💼 Portfolio Website</p>
                <p>✅ ⛪ Church / School Website</p>
                <p>✅ 🛒 E-commerce + Booking Website</p>
                <p>✅ ⚡ Flask Web Apps</p>
                <p class="price">💸 Starting from 15k - Very Cheap! 💸</p>
                <a class="btn" href="https://wa.me/2349036004102">💬 Chat Me on WhatsApp Now 💬</a>
            </div>

            <div class="card">
                <div class="sticker">🖼️🎨💻</div>
                <h2>📸 My Fine Work</h2>
                <div class="grid">
                    <img src="https://images.unsplash.com/photo-1547658719-da2b51169166?w=500">
                    <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500">
                    <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=500">
                    <img src="https://images.unsplash.com/photo-1522542550225-18e00f34a8f0?w=500">
                </div>
                <p>😍 Clean, Fast, Mobile-Friendly 💯</p>
            </div>

            <div class="card">
                <div class="sticker">📅📌🔔</div>
                <h2>👇 Book Me Now 👇</h2>
                <p>👉 Fill form, e go enter my WhatsApp direct! 🚀</p>
                <form action="/book" method="post">
                    <input type="text" name="name" placeholder="👤 Your Name" required>
                    <input type="tel" name="phone" placeholder="📱 Your WhatsApp Number" required>
                    <select name="service" required>
                        <option value="">👉 Select Service 👈</option>
                        <option>🏢 Business Website</option>
                        <option>👨‍💼 Portfolio Website</option>
                        <option>🛒 E-commerce Website</option>
                        <option>📅 Booking Website</option>
                    </select>
                    <textarea name="message" placeholder="✍️ Describe wetin you want..." required></textarea>
                    <button type="submit" class="btn btn-blue">🚀 Book Now - Go to WhatsApp 💬</button>
                </form>
            </div>

            <div class="card" style="text-align:center; background:linear-gradient(135deg,#fff,#ffe9d6)">
                <div class="sticker">📍🌍📞</div>
                <h3>📍 Lagos State | Available Anywhere 🌍</h3>
                <p style="font-size:20px; font-weight:bold">📞 09036004102 📞</p>
                <a class="btn" href="https://wa.me/2349036004102">💚 Tap to Chat on WhatsApp 💚</a>
                <p>⭐⭐⭐⭐ Trusted by Customers</p>
            </div>
        </div>

        <a class="floating-wa" href="https://wa.me/2349036004102">💬</a>
    </body>
    </html>
    """

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    phone = request.form.get('phone')
    service = request.form.get('service')
    message = request.form.get('message')
    text = f"Hello Damzieark! New Booking: Name:{name} Phone:{phone} Service:{service} Message:{message}"
    return redirect(f"https://wa.me/2349036004102?text={text}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
