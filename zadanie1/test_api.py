import subprocess
import json

def run_curl_command(url):
    result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
    return result.stdout

def test_endpoint(url, key_elements):
    response = run_curl_command(url)
    response_json = json.loads(response)
    for element in key_elements:
        if element not in response_json:
            print(f"Test for {url}: FAILED (missing {element})")
            return
    print(f"Test for {url}: PASSED")

def main():
    api_url = "https://jsonplaceholder.typicode.com"
    endpoints = [
        (f"{api_url}/posts/1", ['userId', 'id', 'title']),
        (f"{api_url}/comments/1", ['postId', 'id', 'email']),
        (f"{api_url}/todos/1", ['userId', 'id', 'title'])
    ]

    for url, elements in endpoints:
        test_endpoint(url, elements)

if __name__ == "__main__":
    main()
