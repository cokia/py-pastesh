from pastesh import upload_to_pastesh

def main():
    # 암호화된 paste를 생성하고 URL을 반환합니다.
    message = "Hello, this is a test message."
    subject = "Test Subject"
    
    try:
        paste_url = upload_to_pastesh(message, subject=subject)
        print(f"Paste created successfully! URL: {paste_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
