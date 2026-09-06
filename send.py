#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import sys
import os
import json

def send_webhook_message(webhook_url, message, username=None, avatar_url=None):
    """
    Gửi tin nhắn tới webhook URL (hỗ trợ Discord, Slack, hoặc webhook tùy chỉnh).
    """
    headers = {'Content-Type': 'application/json'}
    payload = {
        'content': message
    }
    if username:
        payload['username'] = username
    if avatar_url:
        payload['avatar_url'] = avatar_url

    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        print(f"✅ Đã gửi tin nhắn thành công (status {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi khi gửi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Lấy webhook URL từ biến môi trường hoặc tham số dòng lệnh
    webhook_url = os.environ.get('WEBHOOK_URL')
    if not webhook_url and len(sys.argv) > 1:
        webhook_url = sys.argv[1]  # URL webhook có thể truyền làm tham số đầu tiên

    if not webhook_url:
        print("⚠️  Vui lòng cung cấp webhook URL qua biến môi trường WEBHOOK_URL hoặc tham số dòng lệnh.")
        sys.exit(1)

    # Tin nhắn có thể lấy từ tham số còn lại hoặc nhập từ stdin
    if len(sys.argv) > 2:
        message = ' '.join(sys.argv[2:])
    else:
        message = input("Nhập tin nhắn cần gửi: ")

    if not message:
        print("⚠️  Tin nhắn trống, không gửi.")
        sys.exit(1)

    send_webhook_message(webhook_url, message)