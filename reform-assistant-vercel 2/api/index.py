import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import anthropic

app = Flask(__name__)
CORS(app)

# Claude APIクライアントの初期化
client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        messages = data.get('messages', [])
        
        # Claude APIに送信
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=messages
        )
        
        return jsonify({
            'response': response.content[0].text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/initial-message', methods=['POST'])
def initial_message():
    try:
        data = request.get_json()
        form_data = data.get('formData', {})
        
        # フォームデータを基にプロンプトを作成
        prompt = f"""
あなたはリフォーム熊本のAIアドバイザーです。以下のお客様情報を基に、4つの魅力的なリフォームプランを提案してください。

お客様情報:
- 家族構成: {form_data.get('familyMembers', [])}
- ペット: {form_data.get('pets', {})}
- 住所: {form_data.get('address', '')}
- ライフスタイル: {form_data.get('lifestyle', [])}
- 趣味: {form_data.get('hobbies', [])}
- インテリアスタイル: {form_data.get('interiorStyle', [])}
- リフォーム箇所: {form_data.get('reformAreas', [])}
- リフォーム理由: {form_data.get('reformReasons', [])}
- その他の要望: {form_data.get('otherRequests', '')}

4つのプランを番号付きで提案し、それぞれに絵文字とキャッチーなタイトルをつけてください。
各プランは2-3行で簡潔に説明してください。
最後に「どのプランが気になりますか？番号で教えてください！😊」と質問してください。
"""
        
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return jsonify({
            'response': response.content[0].text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel用のハンドラー
def handler(request):
    with app.app_context():
        return app.full_dispatch_request()

if __name__ == '__main__':
    app.run(debug=True)

