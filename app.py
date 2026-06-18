"""
极简 Flask Web 应用 — CI/CD 实验演示
"""
from flask import Flask, render_template_string

app = Flask(__name__)

# 学生信息
STUDENT_ID = "2440666143"
STUDENT_NAME = "黄旭东"

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD 实验 — Flask App</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background: #0a0a0a;
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
            color: #ffffff;
        }
        .container {
            max-width: 480px; width: 90%; padding: 48px 24px;
        }
        .eyebrow {
            font-family: 'GeistMono', ui-monospace, SFMono-Regular, Menlo, Monaco, monospace;
            font-size: 14px; font-weight: 400; line-height: 20px;
            letter-spacing: 1.4px; text-transform: uppercase;
            color: #7d8187; margin-bottom: 16px;
        }
        h1 {
            font-size: 48px; font-weight: 400; line-height: 48px;
            letter-spacing: -1.2px; margin-bottom: 24px;
        }
        .version {
            font-size: 14px; color: #7d8187; margin-bottom: 32px;
        }
        .status {
            display: inline-block; background: transparent;
            color: #ffffff; padding: 8px 24px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            border-radius: 9999px; font-size: 14px; margin-bottom: 48px;
        }
        .card {
            background: #191919; border: 1px solid #212327;
            border-radius: 8px; padding: 24px; margin-bottom: 16px;
        }
        .card-title {
            font-family: 'GeistMono', ui-monospace, SFMono-Regular, Menlo, Monaco, monospace;
            font-size: 12px; font-weight: 400; line-height: 16px;
            letter-spacing: 1.2px; text-transform: uppercase;
            color: #7d8187; margin-bottom: 16px;
        }
        .info-row {
            display: flex; justify-content: space-between;
            padding: 12px 0; border-bottom: 1px solid #212327;
        }
        .info-row:last-child { border-bottom: none; }
        .info-label { color: #7d8187; font-size: 14px; }
        .info-value { color: #ffffff; font-size: 14px; }
        .student-card {
            background: #191919; border: 1px solid #212327;
            border-radius: 8px; padding: 24px; margin-top: 32px;
        }
        .student-row {
            display: flex; justify-content: space-between;
            padding: 12px 0; border-bottom: 1px solid #212327;
        }
        .student-row:last-child { border-bottom: none; }
        .student-label { color: #7d8187; font-size: 14px; }
        .student-value { color: #ffffff; font-size: 14px; }
        .footer {
            margin-top: 48px; text-align: center;
            color: #7d8187; font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="eyebrow">CI/CD DEPLOYMENT</div>
        <h1>部署成功</h1>
        <p class="version">Flask App v3.0 · Python {{ python_version }}</p>
        <div class="status">服务运行正常</div>

        <div class="card">
            <div class="card-title">系统信息</div>
            <div class="info-row">
                <span class="info-label">容器 ID</span>
                <span class="info-value">{{ hostname }}</span>
            </div>
            <div class="info-row">
                <span class="info-label">部署时间</span>
                <span class="info-value">{{ deploy_time }}</span>
            </div>
            <div class="info-row">
                <span class="info-label">环境</span>
                <span class="info-value">{{ environment }}</span>
            </div>
        </div>

        <div class="student-card">
            <div class="card-title">学生信息</div>
            <div class="student-row">
                <span class="student-label">学号</span>
                <span class="student-value">{{ student_id }}</span>
            </div>
            <div class="student-row">
                <span class="student-label">姓名</span>
                <span class="student-value">{{ student_name }}</span>
            </div>
        </div>

        <div class="footer">SOFTWARE ENGINEERING · CI/CD LAB</div>
    </div>
</body>
</html>"""


@app.route("/")
def index():
    import socket, platform, datetime
    return render_template_string(
        HTML,
        python_version=platform.python_version(),
        hostname=socket.gethostname(),
        deploy_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment="Production" if app.config.get("ENV") == "production" else "Development",
        student_id=STUDENT_ID,
        student_name=STUDENT_NAME,
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
