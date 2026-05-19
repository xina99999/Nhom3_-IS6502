# Linear Regression

Linear Regression, hay hồi quy tuyến tính, là một thuật toán học có giám sát được sử dụng để dự đoán một giá trị số liên tục dựa trên một hoặc nhiều biến đầu vào. Thuật toán này giả định rằng giữa biến đầu vào và biến cần dự đoán tồn tại một mối quan hệ gần tuyến tính.

Ví dụ, nếu cần dự đoán giá nhà, biến đầu vào có thể là diện tích, số phòng hoặc tuổi của căn nhà. Giá nhà là biến cần dự đoán. Linear Regression sẽ cố gắng tìm ra một phương trình tuyến tính mô tả mối quan hệ giữa biến đầu vào và giá trị đầu ra.

## Ý tưởng chính

Ý tưởng chính của Linear Regression là tìm một đường thẳng, hoặc một mặt phẳng trong trường hợp có nhiều biến, sao cho đường hoặc mặt phẳng đó nằm gần các điểm dữ liệu thật nhất có thể.

Với Simple Linear Regression, mô hình chỉ có một biến độc lập. Công thức có dạng:

```text
y = b0 + b1*x
```

Trong đó:

- `y` là giá trị cần dự đoán.
- `x` là biến đầu vào.
- `b0` là hệ số chặn, tức giá trị dự đoán khi `x = 0`.
- `b1` là hệ số góc, cho biết khi `x` tăng thêm 1 đơn vị thì `y` thay đổi bao nhiêu.

Với Multiple Linear Regression, mô hình có nhiều biến độc lập. Công thức có dạng:

```text
y = b0 + b1*x1 + b2*x2 + ... + bp*xp
```

Trong đó `x1, x2, ..., xp` là các biến đầu vào, còn `b1, b2, ..., bp` là các hệ số tương ứng với từng biến.

## Cách Linear Regression học

Trong Linear Regression, "học" nghĩa là tìm ra các hệ số của mô hình từ dữ liệu ban đầu. Sau khi học xong, mô hình dùng các hệ số này để dự đoán giá trị mới.

Có thể hiểu quá trình này gồm hai phần:

- Giai đoạn học: dùng dữ liệu `X` và `Y` để tính các hệ số hồi quy.
- Giai đoạn dự đoán: dùng các hệ số đã học và dữ liệu đầu vào mới để tính giá trị `y` mới.

Phần dưới sẽ trình bày chi tiết cách tính trong Simple Linear Regression và Multiple Linear Regression.

## Simple Linear Regression

Trong Simple Linear Regression, vì chỉ có một biến đầu vào nên ta có thể tính trực tiếp hai hệ số `b0` và `b1`.

Trước tiên, thuật toán tính giá trị trung bình của `X` và `Y`. Sau đó, nó đo xem `X` và `Y` thay đổi cùng nhau như thế nào. Nếu `X` tăng và `Y` cũng thường tăng, hệ số `b1` sẽ có giá trị dương. Nếu `X` tăng nhưng `Y` thường giảm, hệ số `b1` sẽ có giá trị âm.

Sau khi tính được `b1`, thuật toán dùng giá trị trung bình của `X` và `Y` để tính `b0`. Khi đã có `b0` và `b1`, mô hình có thể dự đoán giá trị mới bằng công thức:

```text
predicted_y = b0 + b1*x_new
```

Về mặt tính toán, Simple Linear Regression thường tính hệ số theo các bước sau:

1. Tính số lượng quan sát `n`.
2. Tính tổng các giá trị của `X` và `Y`.
3. Tính giá trị trung bình của `X` và `Y`:

```text
mean_x = sum_x / n
mean_y = sum_y / n
```

4. Tính mức độ thay đổi chung giữa `X` và `Y`. Phần này được gọi là tử số. Với mỗi điểm, ta nhân độ lệch của `X` với độ lệch của `Y` so với trung bình: nếu cả hai cùng lớn hơn hoặc cùng nhỏ hơn trung bình, tích này dương, tức `X` và `Y` có xu hướng đồng biến:

```text
numerator = sum((X[i] - mean_x) * (Y[i] - mean_y))
```

5. Tính mức độ biến thiên của riêng `X`. Phần này được gọi là mẫu số. Nó cho biết `X` trải rộng như thế nào so với trung bình, dùng để chuẩn hóa tử số thành hệ số góc thực sự:

```text
denominator = sum((X[i] - mean_x)^2)
```

6. Tính hệ số góc `b1`:

```text
b1 = numerator / denominator
```

7. Tính hệ số chặn `b0`:

```text
b0 = mean_y - b1 * mean_x
```

Sau khi có `b0` và `b1`, mô hình có thể dự đoán giá trị mới bằng cách thay `x_new` vào phương trình tuyến tính. Vì vậy, phần tính toán của Simple Linear Regression gồm hai giai đoạn: học hệ số từ dữ liệu ban đầu và dùng hệ số đó để dự đoán dữ liệu mới.

### Ví dụ tính tay

Giả sử có 5 căn nhà với diện tích (`X`, đơn vị m²) và giá (`Y`, đơn vị tỷ đồng) như sau:

| Căn nhà | Diện tích X | Giá Y |
| ------- | ----------- | ----- |
| 1       | 50          | 2.0   |
| 2       | 60          | 2.5   |
| 3       | 70          | 3.0   |
| 4       | 80          | 3.5   |
| 5       | 90          | 4.0   |

**Bước 1–3:** Tính trung bình.

```text
n = 5
sum_x = 50 + 60 + 70 + 80 + 90 = 350  →  mean_x = 350 / 5 = 70
sum_y = 2 + 2.5 + 3 + 3.5 + 4 = 15    →  mean_y = 15 / 5 = 3
```

**Bước 4:** Tính tử số — đo mức độ `X` và `Y` thay đổi cùng nhau.

```text
numerator = (50-70)(2-3) + (60-70)(2.5-3) + (70-70)(3-3) + (80-70)(3.5-3) + (90-70)(4-3)
          = (-20)(-1)   + (-10)(-0.5)     + (0)(0)       + (10)(0.5)      + (20)(1)
          = 20 + 5 + 0 + 5 + 20
          = 50
```

**Bước 5:** Tính mẫu số — đo mức độ phân tán của riêng `X`.

```text
denominator = (-20)^2 + (-10)^2 + 0^2 + 10^2 + 20^2
            = 400 + 100 + 0 + 100 + 400
            = 1000
```

**Bước 6–7:** Tính hệ số.

```text
b1 = 50 / 1000 = 0.05
b0 = 3 - 0.05 * 70 = 3 - 3.5 = -0.5
```

Phương trình thu được: `y = -0.5 + 0.05 * x`

Nghĩa là mỗi m² diện tích tăng thêm, giá nhà tăng thêm 0.05 tỷ đồng.

**Dự đoán:** Căn nhà mới có diện tích 75 m²:

```text
predicted_y = -0.5 + 0.05 * 75 = -0.5 + 3.75 = 3.25 tỷ đồng
```

### Mã giả Simple Linear Regression

```text
FUNCTION SimpleLinearRegression(X, Y):

    n = length(X)  # n = số mẫu dữ liệu, ví dụ 5 căn nhà thì n = 5

    sum_x = 0
    sum_y = 0

    FOR i = 0 TO n - 1:       # duyệt qua từng mẫu, cộng dồn X và Y
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / n         # tính trung bình X
    mean_y = sum_y / n         # tính trung bình Y


    numerator = 0    # tử số: đo mức độ X và Y thay đổi cùng nhau
    denominator = 0  # mẫu số: đo mức độ phân tán của X

    FOR i = 0 TO n - 1:
        x_diff = X[i] - mean_x          # độ lệch của X[i] so với trung bình
        y_diff = Y[i] - mean_y          # độ lệch của Y[i] so với trung bình

        numerator   = numerator   + x_diff * y_diff  # cộng dồn tích hai độ lệch
        denominator = denominator + x_diff * x_diff  # cộng dồn bình phương độ lệch X


    b1 = numerator / denominator    # hệ số góc: X tăng 1 đơn vị thì Y tăng bao nhiêu
    b0 = mean_y - b1 * mean_x      # hệ số chặn: giá trị Y khi X = 0

    RETURN b0, b1


FUNCTION PredictSimpleLinearRegression(b0, b1, x_new):

    y_predicted = b0 + b1 * x_new  # thay x_new vào phương trình để dự đoán

    RETURN y_predicted
```

## Multiple Linear Regression

Về bản chất, Multiple Linear Regression có cách tính tương tự Simple Linear Regression: mô hình vẫn cần tìm các hệ số sao cho giá trị dự đoán gần với giá trị thực tế nhất. Điểm khác là Simple Linear Regression chỉ có một biến đầu vào, còn Multiple Linear Regression có nhiều biến đầu vào.

Nếu chỉ có một biến `x`, mô hình chỉ cần tìm `b0` và `b1`:

```text
y = b0 + b1*x
```

Nhưng nếu có nhiều biến như diện tích, số phòng và tuổi căn nhà, phương trình sẽ dài hơn:

```text
y = b0 + b1*x1 + b2*x2 + b3*x3
```

Khi số lượng biến tăng lên, việc tính từng hệ số riêng lẻ bằng cách viết công thức thủ công sẽ rất dài và khó theo dõi. Vì vậy, Multiple Linear Regression thường dùng ma trận để gom toàn bộ dữ liệu và hệ số lại, sau đó giải trong một công thức chung.

Để hiểu bản chất, giả sử ta dự đoán giá nhà bằng 2 biến: diện tích và số phòng. Phương trình cần tìm là:

```text
giá = b0 + b1*diện_tích + b2*số_phòng
```

Giả sử có dữ liệu thật như sau:

```text
Nhà 1: diện tích = 50, số phòng = 2, giá = 1.7
Nhà 2: diện tích = 60, số phòng = 3, giá = 2.0
Nhà 3: diện tích = 80, số phòng = 4, giá = 2.5
```

Thay từng dòng dữ liệu vào phương trình, ta có hệ phương trình:

```text
b0 + 50*b1 + 2*b2 = 1.7
b0 + 60*b1 + 3*b2 = 2.0
b0 + 80*b1 + 4*b2 = 2.5
```

Việc học Multiple Linear Regression chính là tìm `b0`, `b1`, `b2` sao cho các phương trình trên đúng hoặc gần đúng nhất.

Để viết hệ phương trình này dưới dạng ma trận, ta viết rõ `b0` thành `1*b0`:

```text
1*b0 + 50*b1 + 2*b2 = 1.7
1*b0 + 60*b1 + 3*b2 = 2.0
1*b0 + 80*b1 + 4*b2 = 2.5
```

Khi đó, phần hệ số đứng trước `b0`, `b1`, `b2` được gom thành ma trận `X_new`:

```text
X_new = [
    [1, 50, 2],
    [1, 60, 3],
    [1, 80, 4]
]
```

Cột đầu tiên toàn số `1` xuất hiện để đưa `b0` vào phép nhân ma trận. Nếu không có cột `1`, phép tính chỉ có `b1*x1 + b2*x2` và sẽ bị thiếu hệ số chặn `b0`.

Vector hệ số cần tìm là:

```text
B = [b0, b1, b2]
```

Vector giá trị thực tế là:

```text
Y = [1.7, 2.0, 2.5]
```

Toàn bộ hệ phương trình có thể viết gọn thành:

```text
X_new * B = Y
```

Nói cách khác, ma trận chỉ là cách viết gọn của nhiều phương trình cùng lúc:

```text
[1, 50, 2] * [b0, b1, b2] = 1.7
[1, 60, 3] * [b0, b1, b2] = 2.0
[1, 80, 4] * [b0, b1, b2] = 2.5
```

Vấn đề là ta cần tìm `B`. Nếu đây là phương trình số thường:

```text
3 * b = 6
```

thì ta có thể chia hai vế cho `3` để tìm `b`:

```text
b = 6 / 3 = 2
```

Nhưng với ma trận:

```text
X_new * B = Y
```

ta không thể chia trực tiếp cho `X_new` như số thường. Nếu `X_new` là ma trận vuông, ta có thể dùng nghịch đảo của nó. Tuy nhiên trong thực tế, `X_new` thường không vuông vì số mẫu dữ liệu thường khác số hệ số cần tìm.

Ví dụ nếu có 100 căn nhà và 2 biến đầu vào, sau khi thêm cột `1`, `X_new` sẽ có kích thước:

```text
100 dòng × 3 cột
```

Ma trận này không vuông, nên không thể tính nghịch đảo trực tiếp.

Để giải quyết, ta nhân cả hai vế với ma trận chuyển vị của `X_new`, gọi là `XT`:

```text
X_new * B = Y

XT * X_new * B = XT * Y
```

Sau đó đặt:

```text
XTX = XT * X_new
XTY = XT * Y
```

Khi đó phương trình trở thành:

```text
XTX * B = XTY
```

Điểm quan trọng là `XTX` là ma trận vuông. Ví dụ:

```text
X_new có kích thước 100×3
XT có kích thước 3×100

XT * X_new có kích thước 3×3
```

Lúc này `XTX` đã vuông, nên ta có thể dùng nghịch đảo để tìm `B`:

```text
B = inverse(XTX) * XTY
```

Viết đầy đủ:

```text
B = inverse(transpose(X_new) * X_new) * transpose(X_new) * Y
```

Công thức này được gọi là Normal Equation. Nó giúp tính toàn bộ hệ số `b0, b1, b2, ..., bp` cùng lúc.

Tóm lại, các bước sau bước thêm cột `1` có thể hiểu như sau:

1. Chuẩn bị ma trận `X` chứa các biến đầu vào.
2. Chuẩn bị vector `Y` chứa giá trị thực tế.
3. Thêm cột `1` vào đầu `X` để tạo `X_new`.
4. Viết bài toán thành `X_new * B = Y`.
5. Vì `X_new` thường không vuông, không thể lấy nghịch đảo trực tiếp.
6. Nhân cả hai vế với `XT` để tạo ra `XTX * B = XTY`.
7. Vì `XTX` là ma trận vuông, dùng `inverse(XTX)` để giải ra `B`.

Sau khi có `B`, mô hình có thể dự đoán dữ liệu mới bằng cách nhân từng hệ số với biến tương ứng:

```text
predicted_y = b0 + b1*x1 + b2*x2 + ... + bp*xp
```

### Mã giả Multiple Linear Regression

```text
FUNCTION MultipleLinearRegression(X, Y):

    n = số hàng của X      # số mẫu dữ liệu
    p = số cột của X       # số biến đầu vào

    X_new = ma trận mới có n hàng và p + 1 cột

    FOR i = 0 TO n - 1:
        X_new[i][0] = 1

        FOR j = 0 TO p - 1:
            X_new[i][j + 1] = X[i][j]

    XT = transpose(X_new)

    XTX = XT * X_new
    XTY = XT * Y

    B = inverse(XTX) * XTY

    RETURN B

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


FUNCTION PredictMultipleLinearRegression(B, x_new):

    y_predicted = B[0]

    FOR j = 1 TO length(B) - 1:
        y_predicted = y_predicted + B[j] * x_new[j - 1]

    RETURN y_predicted
```
