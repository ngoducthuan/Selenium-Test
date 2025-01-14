from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Định nghĩa tên đăng nhập và mật khẩu cố định
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kiểm tra tên đăng nhập và mật khẩu
        if username == USERNAME and password == PASSWORD:
            print("Oke")
            return redirect(url_for('dashboard'))
        else:
            return "Tên đăng nhập hoặc mật khẩu không đúng!", 401

    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
