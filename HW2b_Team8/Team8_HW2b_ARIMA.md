# ARIMA

	ARIMA (AutoRegressive Integrated Moving Average) là một thuật toán dự báo chuỗi thời gian được sử dụng để dự đoán giá trị tương lai dựa trên các giá trị trong quá khứ. Thuật toán này đặc biệt phù hợp với dữ liệu có tính thời gian như doanh số bán hàng, nhiệt độ, giá cổ phiếu hoặc lưu lượng truy cập theo ngày.

	Khác với các mô hình hồi quy thông thường dự đoán dựa trên nhiều biến đầu vào khác nhau, ARIMA chủ yếu dự đoán dựa trên chính lịch sử của chuỗi dữ liệu đó.

	Ví dụ, nếu cần dự báo doanh số bán hàng tháng tiếp theo, mô hình sẽ học từ doanh số của các tháng trước để tìm ra xu hướng, mức độ biến động và các mẫu lặp lại theo thời gian.

	## Ý tưởng chính

	Ý tưởng chính của ARIMA là kết hợp ba thành phần:

	- **AR (AutoRegression)**: sử dụng các giá trị quá khứ để dự đoán giá trị hiện tại.
	- **I (Integrated)**: thực hiện sai phân để biến chuỗi dữ liệu thành stationary (ổn định).
	- **MA (Moving Average)**: sử dụng sai số dự đoán trong quá khứ để cải thiện dự báo.

	Mô hình được biểu diễn dưới dạng:

	```text
	ARIMA(p,d,q)
	```

	Trong đó:

	- `p` là số bậc tự hồi quy (AR).
	- `d` là số lần sai phân.
	- `q` là số bậc trung bình trượt (MA).

	## Thành phần AR (AutoRegression)

	Thành phần AR giả định rằng giá trị hiện tại có liên quan đến các giá trị trước đó.

	Ví dụ:

	```text
	Doanh số hôm nay có thể phụ thuộc vào doanh số của vài ngày trước.
	```

	Nếu `p = 2`, mô hình sử dụng 2 giá trị gần nhất để dự đoán giá trị tiếp theo.

	Công thức tổng quát:

	```text
	yt = c + a1*yt-1 + a2*yt-2 + ... + ap*yt-p + εt
	```

	Trong đó:

	- `yt` là giá trị hiện tại.
	- `yt-1`, `yt-2` là các giá trị quá khứ.
	- `a1, a2, ..., ap` là các hệ số cần học.
	- `εt` là sai số.

	## Thành phần I (Integrated)

	Nhiều chuỗi thời gian có xu hướng tăng hoặc giảm theo thời gian nên chưa ổn định. ARIMA cần chuỗi dữ liệu stationary trước khi huấn luyện.

	Một chuỗi được gọi là stationary khi:

	- trung bình không đổi theo thời gian
	- độ biến động tương đối ổn định
	- không có xu hướng tăng hoặc giảm mạnh

	Ví dụ stationary:

	| Thời gian | Giá trị |
	| ---------- | -------- |
	| 1 | 10 |
	| 2 | 12 |
	| 3 | 11 |
	| 4 | 13 |
	| 5 | 12 |

	Ví dụ không stationary:

	| Thời gian | Giá trị |
	| ---------- | -------- |
	| 1 | 100 |
	| 2 | 120 |
	| 3 | 140 |
	| 4 | 160 |
	| 5 | 180 |

	Chuỗi trên có xu hướng tăng liên tục nên chưa stationary.

	Để xử lý điều này, thuật toán thực hiện sai phân:

	```text
	y_diff[t] = y[t] - y[t-1]
	```

	Nếu cần sai phân 1 lần để ổn định dữ liệu thì:

	```text
	d = 1
	```

	Nếu cần sai phân 2 lần:

	```text
	d = 2
	```

	Ví dụ:

	| Thời gian | Giá trị |
	| ---------- | -------- |
	| 1 | 100 |
	| 2 | 110 |
	| 3 | 125 |
	| 4 | 140 |

	Sai phân bậc 1:

	```text
	110 - 100 = 10
	125 - 110 = 15
	140 - 125 = 15
	```

	Chuỗi mới:

	```text
	[10, 15, 15]
	```

	Sau khi dữ liệu trở nên ổn định hơn, mô hình mới tiếp tục học các mối quan hệ trong chuỗi thời gian.

	## Thành phần MA (Moving Average)

	Thành phần MA sử dụng các sai số trong quá khứ để điều chỉnh dự báo hiện tại.

	Ví dụ:

	```text
	Nếu mô hình dự đoán sai nhiều ở bước trước,
	nó sẽ dùng sai số đó để điều chỉnh dự báo tiếp theo.
	```

	Công thức tổng quát:

	```text
	yt = c + εt + b1*εt-1 + b2*εt-2 + ... + bq*εt-q
	```

	Trong đó:

	- `εt` là sai số hiện tại.
	- `εt-1`, `εt-2` là sai số quá khứ.
	- `b1, b2, ..., bq` là các hệ số MA.

	## Cách ARIMA học

	Quá trình học của ARIMA gồm các bước chính:

	1. Kiểm tra dữ liệu có stationary hay không.
	2. Nếu chưa stationary, thực hiện sai phân.
	3. Xác định các tham số `p`, `d`, `q`.
	4. Huấn luyện nhiều mô hình ARIMA khác nhau.
	5. Đánh giá mô hình bằng AIC hoặc RMSE.
	6. Chọn mô hình tốt nhất.
	7. Dùng mô hình để dự báo dữ liệu tương lai.

	## Tìm mô hình ARIMA tối ưu bằng Grid Search

	Trong thực tế, rất khó biết trước giá trị `p`, `d`, `q` tốt nhất. Vì vậy, thuật toán thường thử nhiều tổ hợp khác nhau và chọn mô hình tốt nhất dựa trên chỉ số AIC.

	Ví dụ:

	```text
	ARIMA(0,1,0)
	ARIMA(1,1,0)
	ARIMA(1,1,1)
	ARIMA(2,1,1)
	...
	```

	Mỗi mô hình sẽ được huấn luyện và tính giá trị AIC.

	Công thức AIC:

	```text
	AIC = 2k - 2ln(L)
	```

	Trong đó:

	- `k` là số tham số của mô hình.
	- `L` là likelihood của mô hình.

	AIC càng nhỏ thì mô hình càng tốt.

	## Mã giả tìm mô hình ARIMA tối ưu bằng Grid Search

	```text
	FUNCTION FitARIMA(train, max_p, max_q):

	    # Bước 1: Xác định số lần sai phân cần thiết

	    d = ChooseDifferencingOrder(train)


	    # Bước 2: Khởi tạo mô hình tốt nhất

	    best_order = NULL
	    best_aic = +infinity
	    best_model = NULL


	    # Bước 3: Thử nhiều tổ hợp (p,q)

	    FOR p = 0 TO max_p:

	        FOR q = 0 TO max_q:

	            TRY:

	                model = TrainARIMA(
	                            data = train,
	                            order = (p, d, q)
	                        )

	                current_aic = CalculateAIC(model)


	                # Bước 4: So sánh AIC

	                IF current_aic < best_aic:

	                    best_order = (p, d, q)
	                    best_aic = current_aic
	                    best_model = model


	            CATCH error:

	                CONTINUE


	    # Bước 5: Trả về mô hình tốt nhất

	    RETURN best_order, best_aic, best_model
	```
	## Mã giả ARIMA chi tiết

	```text
	FUNCTION ARIMA(train_data, p, d, q, forecast_steps):

	    # train_data      : dữ liệu chuỗi thời gian ban đầu
	    # p               : số bậc AR (dùng bao nhiêu giá trị quá khứ)
	    # d               : số lần sai phân
	    # q               : số bậc MA (dùng bao nhiêu lỗi quá khứ)
	    # forecast_steps  : số bước cần dự báo


	    # =========================================
	    # BƯỚC 1: KIỂM TRA VÀ SAI PHÂN DỮ LIỆU
	    # =========================================

	    diff_data = train_data

	    # Nếu d = 1 thì sai phân 1 lần
	    # Nếu d = 2 thì sai phân 2 lần

	    FOR i = 1 TO d:

	        temp = empty list

	        FOR t = 1 TO length(diff_data) - 1:

	            # lấy giá trị hiện tại trừ giá trị trước đó

	            diff_value = diff_data[t] - diff_data[t - 1]

	            Append temp with diff_value

	        # cập nhật chuỗi sau sai phân

	        diff_data = temp


	    # Sau bước này:
	    # dữ liệu đã ổn định hơn (stationary)
	    # để mô hình dễ học hơn


	    # =========================================
	    # BƯỚC 2: KHỞI TẠO
	    # =========================================

	    predictions = empty list

	    # lưu các giá trị dự báo trên chuỗi sai phân

	    errors = empty list

	    # lưu lỗi dự báo:
	    # error = giá trị thật - giá trị dự báo


	    # Ban đầu chưa có lỗi
	    # nên gán tất cả bằng 0

	    FOR i = 0 TO length(diff_data) - 1:

	        Append errors with 0


	    # =========================================
	    # BƯỚC 3: HỌC / DỰ BÁO TRÊN CHUỖI SAI PHÂN
	    # =========================================

	    FOR t = max(p, q) TO length(diff_data) - 1:


	        # -------------------------------------
	        # PHẦN AR (AutoRegression)
	        # dùng giá trị quá khứ
	        # -------------------------------------

	        ar_part = 0


	        FOR i = 1 TO p:

	            # AR coefficient:
	            # hệ số học được từ dữ liệu

	            # diff_data[t - i]:
	            # giá trị quá khứ

	            ar_part = ar_part + (
	                        AR_coefficient[i]
	                        * diff_data[t - i]
	                     )


	        # Ví dụ:
	        # nếu p = 2
	        # thì dùng:
	        # diff[t-1] và diff[t-2]


	        # -------------------------------------
	        # PHẦN MA (Moving Average)
	        # dùng lỗi quá khứ
	        # -------------------------------------

	        ma_part = 0


	        FOR j = 1 TO q:

	            # errors[t-j]:
	            # lỗi của các bước trước

	            ma_part = ma_part + (
	                        MA_coefficient[j]
	                        * errors[t - j]
	                     )


	        # Ví dụ:
	        # nếu q = 1
	        # thì dùng lỗi gần nhất


	        # -------------------------------------
	        # TÍNH GIÁ TRỊ SAI PHÂN DỰ BÁO
	        # -------------------------------------

	        predicted_diff = ar_part + ma_part


	        # predicted_diff:
	        # giá trị sai phân được dự báo


	        # -------------------------------------
	        # TÍNH LỖI
	        # -------------------------------------

	        current_error = (
	                            diff_data[t]
	                            - predicted_diff
	                        )


	        # lỗi = giá trị thật - giá trị dự báo


	        errors[t] = current_error


	        # lưu lỗi lại
	        # để MA sử dụng ở bước tiếp theo


	        # -------------------------------------
	        # LƯU KẾT QUẢ
	        # -------------------------------------

	        Append predictions with predicted_diff


	    # =========================================
	    # BƯỚC 4: DỰ BÁO TƯƠNG LAI
	    # =========================================

	    future_predictions = empty list


	    # lấy giá trị cuối cùng của dữ liệu gốc

	    last_original_value = train_data[last index]


	    # lấy sai phân dự báo cuối cùng

	    current_diff = predictions[last index]


	    FOR step = 1 TO forecast_steps:


	        # -------------------------------------
	        # PHẦN AR
	        # -------------------------------------

	        ar_future = 0


	        FOR i = 1 TO p:

	            ar_future = ar_future + (
	                            AR_coefficient[i]
	                            * current_diff
	                        )


	        # dùng sai phân trước đó
	        # để dự báo sai phân tiếp theo


	        # -------------------------------------
	        # PHẦN MA
	        # -------------------------------------

	        ma_future = 0


	        FOR j = 1 TO q:

	            ma_future = ma_future + (
	                            MA_coefficient[j]
	                            * errors[last index]
	                        )


	        # dùng lỗi gần nhất
	        # để hiệu chỉnh dự báo


	        # -------------------------------------
	        # DỰ BÁO SAI PHÂN
	        # -------------------------------------

	        future_diff = ar_future + ma_future


	        # future_diff:
	        # sai phân dự báo của bước tiếp theo


	        # -------------------------------------
	        # CHUYỂN NGƯỢC VỀ GIÁ TRỊ GỐC
	        # inverse differencing
	        # -------------------------------------

	        predicted_value = (
	                                last_original_value
	                                + future_diff
	                          )


	        # vì:
	        # diff = y[t] - y[t-1]

	        # nên:
	        # y[t] = y[t-1] + diff


	        Append future_predictions with predicted_value


	        # -------------------------------------
	        # CẬP NHẬT CHO VÒNG SAU
	        # -------------------------------------

	        last_original_value = predicted_value

	        current_diff = future_diff


	        # giá trị dự báo hiện tại
	        # sẽ trở thành dữ liệu đầu vào
	        # cho lần dự báo tiếp theo


	    # =========================================
	    # BƯỚC 5: TRẢ KẾT QUẢ
	    # =========================================

	    RETURN future_predictions
	```
