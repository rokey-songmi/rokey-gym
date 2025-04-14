from locker_system import load_lockers, register_member

# 파일 경로 설정
locker_file_path = "locker_list.csv"
member_file_path = "members.csv"

# 사물함 목록 불러오기
lockers = load_lockers(locker_file_path)

# 새 회원 등록 실행
new_member_name = input("새로 등록할 회원의 이름을 입력하세요: ")
result = register_member(new_member_name, lockers, member_file_path)

print(result)
