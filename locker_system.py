# locker_system.py
import csv
import random

# 파일에서 사물함 목록 로드

def load_lockers(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

# 기존에 들어가 있는 사물함 번호 확인

def get_used_lockers(file_path):
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return {row["사물함번호"] for row in reader}
    except FileNotFoundError:
        return set()

# 회원 등록: 이름만 입력 받아 무중복 사물함 번호와 비밀번호 자동 배정

def register_member(name, lockers, member_file):
    used_lockers = get_used_lockers(member_file)
    available_lockers = [l for l in lockers if l["사물함번호"] not in used_lockers]

    if not available_lockers:
        return f"{name}님께 배정할 수 있는 사물함이 없습니다."

    selected = random.choice(available_lockers)
    locker_number = selected["사물함번호"]
    password = selected["비밀번호"]

    with open(member_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["이름", "나이", "성별", "잔여일수", "사물함번호", "비밀번호"])
        age = random.randint(18, 60)
        gender = random.choice(["남", "여"])
        days_left = random.choice([0, 7, 15, 30, 60])
        writer.writerow([name, age, gender, days_left, locker_number, password])

    return f"{name}님, 사물함 번호는 {locker_number}번, 비밀번호는 {password}입니다."
