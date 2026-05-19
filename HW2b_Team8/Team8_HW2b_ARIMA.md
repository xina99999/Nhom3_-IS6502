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

Sai phân bậc 1:

```text
110 - 100 = 10
125 - 110 = 15
```

Chuỗi mới:

```text
[10, 15]
```

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
3. Chọn các tham số `p`, `d`, `q`.
4. Huấn luyện mô hình ARIMA.
5. Đánh giá mô hình bằng AIC hoặc RMSE.
6. Dùng mô hình để dự báo dữ liệu tương lai.

## Tìm mô hình ARIMA tối ưu

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

## Ví dụ trực quan

Giả sử có doanh số theo ngày:

| Ngày | Doanh số |
| ----- | --------- |
| 1 | 100 |
| 2 | 105 |
| 3 | 108 |
| 4 | 115 |
| 5 | 120 |

Nếu dùng:

```text
ARIMA(1,1,1)
```

thì:

- `p = 1`: dùng 1 giá trị quá khứ.
- `d = 1`: sai phân 1 lần.
- `q = 1`: dùng 1 sai số quá khứ.

Sau khi học, mô hình có thể dự báo doanh số ngày thứ 6.

## Mã giả ARIMA

```text
FUNCTION FitARIMA(train, max_p, max_q):

    d = ChooseDifferencingOrder(train)

    best_order = NULL
    best_aic = +infinity
    best_model = NULL


    FOR p = 0 TO max_p:

        FOR q = 0 TO max_q:

            TRY:

                model = TrainARIMA(
                            data = train,
                            order = (p, d, q)
                        )

                current_aic = CalculateAIC(model)


                IF current_aic < best_aic:

                    best_order = (p, d, q)
                    best_aic = current_aic
                    best_model = model


            CATCH error:

                CONTINUE


    RETURN best_order, best_aic, best_model
```

## Mã giả dự báo bằng ARIMA

```text
FUNCTION ForecastARIMA(model, steps):

    forecasts = empty list

    FOR t = 1 TO steps:

        next_value = PredictNext(model)

        Append forecasts with next_value

    RETURN forecasts
```
