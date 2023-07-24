from flask import Flask, request, jsonify

app = Flask(__name__)

def check_phishing_url(url):    
    if url == "https://google.com":
        return "yes"
    elif url == "https://dummy.com":
        return "no"
    else:
        return "unknown"

@app.route('/checkurl', methods=['POST'])
def checkurl():
    data = request.get_json()
    url = data.get('url', '')
    format_type = data.get('format', 'json')
    is_valid = check_phishing_url(url)
    
    response_data = {
        "url": url,
        "is_valid": is_valid
    }
    
    if format_type == 'json':
        return jsonify(response_data)
    elif format_type == 'xml':
        # Your implementation for XML response
        return "XML response not implemented"
    else:
        return "Invalid format type"

if __name__ == '__main__':
    app.run()
