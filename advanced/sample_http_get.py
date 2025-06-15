"""
HTTP GETリクエストのサンプルコード
標準ライブラリのurllib.requestを使用
"""

import urllib.request
import urllib.parse
import json
from typing import Dict, Any, Optional


def simple_get_request(url: str) -> str:
    """
    シンプルなGETリクエスト
    
    Args:
        url: リクエスト先のURL
        
    Returns:
        レスポンステキスト
    """
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')


def get_request_with_headers(url: str, headers: Dict[str, str]) -> Dict[str, Any]:
    """
    ヘッダー付きGETリクエスト
    
    Args:
        url: リクエスト先のURL
        headers: HTTPヘッダー
        
    Returns:
        レスポンス情報の辞書
    """
    request = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(request) as response:
        return {
            'status_code': response.getcode(),
            'headers': dict(response.headers),
            'content': response.read().decode('utf-8')
        }


def get_json_api(url: str, params: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    JSON APIへのGETリクエスト
    
    Args:
        url: APIのURL
        params: クエリパラメータ
        
    Returns:
        JSONレスポンス
    """
    if params:
        query_string = urllib.parse.urlencode(params)
        url = f"{url}?{query_string}"
    
    headers = {
        'User-Agent': 'Python urllib sample',
        'Accept': 'application/json'
    }
    
    request = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(request) as response:
            content = response.read().decode('utf-8')
            return json.loads(content)
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} {e.reason}")
        raise
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        raise
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        raise


def download_file(url: str, filename: str) -> None:
    """
    ファイルダウンロード
    
    Args:
        url: ダウンロード元URL
        filename: 保存先ファイル名
    """
    urllib.request.urlretrieve(url, filename)
    print(f"File downloaded: {filename}")


def main():
    """メイン実行関数"""
    
    print("=== HTTP GETリクエストサンプル ===")
    
    # 1. シンプルなGETリクエスト
    print("1. シンプルなGETリクエスト")
    try:
        response = simple_get_request('https://httpbin.org/get')
        print(f"Response length: {len(response)} characters")
        print(f"First 200 chars: {response[:200]}...")
    except Exception as e:
        print(f"Error: {e}")
    
    # 2. ヘッダー付きGETリクエスト
    print("2. ヘッダー付きGETリクエスト")
    try:
        headers = {
            'User-Agent': 'Python Sample Client 1.0',
            'Accept': 'application/json'
        }
        response = get_request_with_headers('https://httpbin.org/headers', headers)
        print(f"Status Code: {response['status_code']}")
        print(f"Content-Type: {response['headers'].get('Content-Type')}")
        print(f"Response: {response['content'][:200]}...")
    except Exception as e:
        print(f"Error: {e}")
    
    # 3. JSON APIリクエスト（パラメータ付き）
    print("3. JSON APIリクエスト（パラメータ付き）")
    try:
        params = {
            'param1': 'value1',
            'param2': 'value2'
        }
        response = get_json_api('https://httpbin.org/get', params)
        print(f"URL: {response['url']}")
        print(f"Args: {response['args']}")
        print(f"Headers User-Agent: {response['headers']['User-Agent']}")
    except Exception as e:
        print(f"Error: {e}")
    
    # 4. エラーハンドリングの例
    print("4. エラーハンドリングの例（存在しないURL）")
    try:
        response = simple_get_request('https://httpbin.org/status/404')
    except urllib.error.HTTPError as e:
        print(f"HTTP Error caught: {e.code} {e.reason}")
    except Exception as e:
        print(f"Other error: {e}")


if __name__ == '__main__':
    main()