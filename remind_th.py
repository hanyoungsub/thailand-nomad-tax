"""
태국 노마드 세금 계산기 월간 점검 리마인더 (매월 5일)
계류 중인 '당해/익년 송금 면세' 개정안 통과 여부 확인용. 태국 국세청은 태국어+구조 불안정이라 크롤링 부적합.
통과 시: 계산기 로직 대폭 갱신 필요(대부분 케이스 면세화) → 즉시 클로드와 작업.
"""
import os
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram(msg):
    r = requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
        json={"chat_id": TELEGRAM_CHAT_ID, "text": msg},
        timeout=30,
    )
    print("텔레그램:", r.status_code)

if __name__ == "__main__":
    send_telegram(
        "[태국세제 월간점검] 계류 개정안(당해/익년 송금 면세) 통과 여부 확인 시기.\n"
        "절차: 'Thailand foreign income remittance exemption enacted' 구글 검색 → 통과 확인 시 즉시 클로드와 계산기 갱신(선점 기회).\n"
        "▶thailand-nomad-tax.pages.dev"
    )
