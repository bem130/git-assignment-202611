import hashlib

student_id = input("学籍番号: ").strip()
name = input("氏名: ").strip()
source = student_id + name
digest = hashlib.sha256(source.encode("utf-8")).hexdigest()

print(f"照合用の元データ: {source}")
print(f"SHA-256: {digest}")
