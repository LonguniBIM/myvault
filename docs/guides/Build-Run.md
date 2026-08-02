Dưới đây là các câu lệnh CMD / PowerShell để bạn tự build lại trang web:

1. Di chuyển vào thư mục giao diện web
Mở Terminal / CMD / PowerShell và chạy:

powershell
cd D:\wiki\web
2. Các lệnh Build
Chỉ build tạo bản tĩnh (Static output vào folder public):

powershell
npx quartz build
Build và Chạy Server xem trực tiếp trên trình duyệt (Khuyên dùng):

powershell
npx quartz build --serve
Sau khi chạy lệnh này, trình duyệt sẽ mở địa chỉ http://localhost:8080 (hoặc cổng hiển thị trên Terminal). Bạn chỉ cần mở Graph View lên kiểm tra.

💡 Lưu ý nhỏ
Nếu trình duyệt của bạn vẫn lưu bộ nhớ đệm (Cache) của tệp JS cũ, hãy nhấn Ctrl + F5 (hoặc Cmd + Shift + R trên Mac) khi đang ở trang web để tải lại hoàn toàn tài nguyên mới nhé!