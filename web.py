from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Dùng cho flash messages

# Dữ liệu người dùng tĩnh (giả lập database)
users = {
    "admin": "1",  # Tên đăng nhập: mật khẩu
    "user1": "password123",
}

@app.route("/")
def home():
    return render_template("login.html")  # Trả về trang login

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    # Kiểm tra trường hợp trống
    if not username:
        flash("Username is required.", "danger")
        return redirect(url_for("home"))
    if not password:
        flash("Password is required.", "danger")
        return redirect(url_for("home"))

    # Kiểm tra thông tin đăng nhập
    if username in users and users[username] == password:
        # Đăng nhập thành công
        return render_template("dashboard.html", username=username)

    # Sai tên đăng nhập hoặc mật khẩu
    flash("Invalid username or password.", "danger")
    return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")  # Trang chính sau khi đăng nhập

if __name__ == "__main__":
    app.run(debug=True)
