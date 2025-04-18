# Hướng dẫn Chạy Ứng dụng Web SVM Bank Data

## Các bước thực hiện

### 1. Di chuyển đến thư mục dự án

```bash
cd \web
```

### 2. Tạo và kích hoạt môi trường ảo

**Đối với Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Đối với macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Cài đặt thư viện cần thiết

```bash
pip install -r requirements.txt
```

### 4. Chạy ứng dụng

```bash
python app.py
```

hoặc nếu sử dụng Flask:

```bash
flask run
```

### 5. Truy cập ứng dụng trong trình duyệt

Mở trình duyệt web của bạn và truy cập: http://127.0.0.1:5000/
