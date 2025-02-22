import requests
import json

# 샘플 API URL (공공 데이터 제공)
URL = "https://jsonplaceholder.typicode.com/posts"

# API 요청 보내기
response = requests.get(URL)

# 응답 확인
if response.status_code == 200:
    print("✅ API 호출 성공!")
    
      # JSON 데이터 받아오기
    data = response.json()  # 여기서 data 변수를 정의!
    
       # 특정 조건: userId가 1인 게시물만 출력
    filtered_posts = [post for post in data if post["userId"] == 1]

    print(f"🔍 userId=1인 게시물 개수: {len(filtered_posts)}개")
    
    # 첫 번째 게시물만 출력
    print(f"📝 첫 번째 게시물 제목: {filtered_posts[0]['title']}")

    # JSON 데이터 파일로 저장
    with open("filtered_posts.json", "w", encoding="utf-8") as file:
        json.dump(filtered_posts, file, indent=4, ensure_ascii=False)

    print("✅ 필터링된 데이터가 'filtered_posts.json' 파일로 저장됨!")

else:
    print(f"❌ API 호출 실패: {response.status_code}")
