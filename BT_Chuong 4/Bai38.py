# Quản lý sinh viên bằng Python

# Danh sách sinh viên rỗng ban đầu
danh_sach_sv = []

def them_sinh_vien():
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    # thêm vào danh sách dưới dạng dictionary
    danh_sach_sv.append({"ma": ma, "ten": ten})
    print("✅ Đã thêm sinh viên thành công!")

def xoa_sinh_vien():
    ma = input("Nhập mã sinh viên cần xóa: ")
    for sv in danh_sach_sv:
        if sv["ma"] == ma:
            danh_sach_sv.remove(sv)
            print("✅ Đã xóa sinh viên thành công!")
            return
    print("❌ Không tìm thấy sinh viên có mã này.")

def sua_sinh_vien():
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in danh_sach_sv:
        if sv["ma"] == ma:
            ten_moi = input("Nhập tên mới cho sinh viên: ")
            sv["ten"] = ten_moi
            print("✅ Đã sửa thông tin sinh viên thành công!")
            return
    print("❌ Không tìm thấy sinh viên có mã này.")

def xem_danh_sach():
    if not danh_sach_sv:
        print("📭 Danh sách sinh viên hiện đang rỗng.")
    else:
        print("📋 Danh sách sinh viên:")
        for sv in danh_sach_sv:
            print(f"- Mã: {sv['ma']}, Tên: {sv['ten']}")

# --- Menu chính ---
while True:
    print("\n--- MENU QUẢN LÝ SINH VIÊN ---")
    print("1. Thêm sinh viên")
    print("2. Xóa sinh viên")
    print("3. Sửa sinh viên")
    print("4. Xem danh sách sinh viên")
    print("5. Thoát")

    chon = input("Nhập lựa chọn (1-5): ")

    if chon == "1":
        them_sinh_vien()
    elif chon == "2":
        xoa_sinh_vien()
    elif chon == "3":
        sua_sinh_vien()
    elif chon == "4":
        xem_danh_sach()
    elif chon == "5":
        print("👋 Thoát chương trình.")
        break
    else:
        print("❌ Lựa chọn không hợp lệ, vui lòng nhập lại.")