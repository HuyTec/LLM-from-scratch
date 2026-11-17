# 001 · GPT cấp ký tự

**Giả thuyết:** GPT hai tầng có thể học quy luật ký tự trong Tiny Shakespeare
và giảm validation loss khi huấn luyện trên CPU.

**Cách kiểm tra:** Overfit một batch để kiểm tra dữ liệu và training loop.
Sau đó huấn luyện trên train, đo cross-entropy trung bình trên val và sinh
mẫu từ checkpoint có validation loss thấp nhất.

**Kết quả:** Chưa chạy. Cấu hình hiện tại là giả định ban đầu.
