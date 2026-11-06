# Quy trình thực nghiệm PR Flow

Mục đích: tạo dữ liệu Pull Request → kiểm tra CI → merge → triển khai để phân tích Process Mining. Các workflow được kích hoạt bằng pull request hoặc push vào `main`.

- `PR Flow CI`: kiểm tra các tệp notebook là JSON định dạng notebook v4, build trang demo và chạy unit test. CI không chạy các cell notebook, không kiểm chứng độ chính xác của mô hình hay kết quả học máy.
- `PR Flow Deploy demo`: lặp lại kiểm tra, sau đó triển khai một trang tĩnh thử nghiệm trên GitHub Pages khi có push vào `main`. Chỉ thư mục `pr-flow-site` được xuất bản; mã notebook không được đưa lên trang. Trang công khai và chỉ phục vụ demo, không phải production của bài tập.
- Sự kiện deployment gắn với môi trường `github-pages`. Trong PR Flow, chọn workflow `PR Flow CI` và môi trường `github-pages`. Chỉ số bị thiếu phải được giữ là thiếu dữ liệu.

Lưu ý: các PR do cùng người tự tạo và merge không phải thử nghiệm có reviewer độc lập, không đủ bằng chứng để khẳng định hiệu quả cải tiến.
