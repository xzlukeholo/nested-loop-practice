# # 題目 1：印出 4 列、5 欄星星
for row in range(4):
    for column in range(5):
        print("*", end="")
    print()

# 題目 2：印出座位表

seats = [
    ["A1", "A2", "A3"],
    ["B1", "B2", "B3"],
    ["C1", "C2", "C3"]
]

for row in seats:
    for student in row:
        print(student)

# 題目 3：列出早餐所有組合

foods = ["蛋餅", "飯糰", "鍋貼"]
drinks = ["紅茶", "豆漿", "奶茶", "綠茶"]

for food in foods:
    for drink in drinks:
        print(f"{food} + {drink}")

"""
挑戰題一 : 進階圖形——靠右對齊的數字直角三角形
--------owo--------

你剛剛寫的題目 1 是固定長寬的矩形。
這次我們要讓內層迴圈的次數隨著外層改變，而且還要加上「空格」來控制對齊！
題目要求： 請用巢狀迴圈印出一個高度為 5 的直角三角形，但必須靠右對齊，且每一列印出的是該列的行號數字
(如下圖所示）。預期輸出效果：
    1
   22
  333
 4444
55555

提示： 1. 外層迴圈控制列數(1 到 5)。
2. 每一列在印出數字之前，必須先印出一定數量的「空格」。
3. 想想看：第一列有 4 個空格、1 個數字；第二列有 3 個空格、2 個數字...
這個規律跟現在是「第幾列」有什麼數學關係？

"""
# 一開始自己寫的:(老師給80分)

row_count = 0
blank_count = 5
for row in range(5):
    row_count += 1
    blank_count -= 1
    for blank_column in range(blank_count):
        print(" ", end="")
    for n_column in range(row_count):
        print(row_count, end="")
    print()


# 下面是老師完,給提示後的改進版本:(92分)

for row in range(1, 6):

    blank = 5 - row

    for b_column in range(blank):
        print(" ", end="")
    for n_column in range(row):
        print(row, end="")
    print()

"""
挑戰題二: 實務應用——電影院座位劃位與排他邏輯
--------owo--------

剛才的題目 2 是單純印出所有座位。
在真實世界的劃位系統中，有些位置可能已經被買走了（不能賣)
而且通常我們需要幫座位加上排數與號碼。

題目要求：有一間小電影院，一共有 3 排(A、B、C),每排有 5 個位置(1 到 5 號）。
但是,B 排的所有位置因為設備維修「不開放預約」
而且 A3、C5 這兩個特定的風水寶位「已經被點走（已售出）」了。
請用巢狀迴圈列出目前所有還能購買的空座位。

預期輸出效果：

可購買座位: A1
可購買座位: A2
可購買座位: A4
可購買座位: A5
可購買座位: C1
可購買座位: C2
可購買座位: C3
可購買座位: C4

提示： 1. 外層迴圈走訪排數 ["A", "B", "C"]，內層迴圈走訪號碼 range(1, 6)。
2. 你需要在內層迴圈裡面加入 if 條件判斷（甚至可以用到你剛學的 match-case 喔！）。
3. 如果遇到不能賣的座位，可以用 continue 跳過它，不印出來。

這兩題分別考驗了你對「迴圈變數的數學邏輯」以及「迴圈內加入條件控制(if / continue)」的能力。

"""
seats = [
    ["A1", "A2", "A3", "A4", "A5"],
    ["B1", "B2", "B3", "B4", "B5"],
    ["C1", "C2", "C3", "C4", "C5"]
]

sold_seats = ["A3", "C5"]

for row in seats:
    if "A1" in row:
        for seat in row:
            match seat:
                case "A3":
                    continue
                case _:
                    print(f"可購買座位: {seat}")
    if "B1" in row:
        for seat in row:
            print(f"不開放預約: {seat}")
    if "C1" in row:
        for seat in row:
            match seat:
                case "C5":
                    continue
                case _:
                    print(f"可購買座位: {seat}")

"""
第三題：nested-loop-practice 進階小題目
主題：門市每日營收檢查器
--------owo--------

你現在是一間飲料店的小小資料分析助理。

公司有 3 間門市，每間門市都有 3 天的營收資料。
請用「巢狀迴圈」依序取出每間門市、每一天，以及對應的營收資料，並照指定格式印出。

已知資料：

stores = ["高雄店", "台南店", "台中店"]

revenues = [
    [3200, 4100, 3900],  # 高雄店
    [2800, 3000, 3500],  # 台南店
    [4500, 4700, 4600]   # 台中店
]

days = ["星期一", "星期二", "星期三"]


題目要求：

請用巢狀迴圈印出所有門市每天的營收。

預期輸出效果：

高雄店 星期一 營收：3200 元
高雄店 星期二 營收：4100 元
高雄店 星期三 營收：3900 元
台南店 星期一 營收：2800 元
台南店 星期二 營收：3000 元
台南店 星期三 營收：3500 元
台中店 星期一 營收：4500 元
台中店 星期二 營收：4700 元
台中店 星期三 營收：4600 元


限制：

1. 請使用巢狀迴圈
2. 請練習使用 range(len(...))
3. 先不要使用 sum()
4. 先不要使用 enumerate()
5. 先不要使用 zip()


提示：

外層迴圈控制「第幾間門市」
內層迴圈控制「第幾天」

也就是：

stores[i]      代表第 i 間門市
days[j]        代表第 j 天
revenues[i][j] 代表第 i 間門市第 j 天的營收
"""
# stores = ["高雄店", "台南店", "台中店"]

# revenues = [
#     [3200, 4100, 3900],  # 高雄店
#     [2800, 3000, 3500],  # 台南店
#     [4500, 4700, 4600]   # 台中店
# ]

# days = ["星期一", "星期二", "星期三"]

# for store_n in range(len(stores)):
#     for day_n in range(len(days)):
#         print(
#             f"{stores[store_n]} {days[day_n]} 營收:{revenues[store_n][day_n]} 元")

# 這題寫得正確。
# 老師給我 95 / 100。
# 老師推薦我把變數名稱改得更直覺一點:
# 雖然 store_n、day_n 可以懂
# 但 store_index、day_index 更清楚地表示「這是索引」。
# 輸出格式跟題目預期差一點點。

# 這邊先註解,因為下一題要延伸這題,讓題目加入一點「資料分析邏輯」，但還是限制在妳目前學過的範圍：
# 巢狀迴圈、range(len(...))、if 判斷、變數累加、最大值/最小值判斷。
# 下面這題適合當 題目三的進階難度。

"""
第四題:nested-loop-practice 四星挑戰題
主題：門市營收分析小助手
--------owo--------

你現在是一間飲料店的小小資料分析助理。

公司有 3 間門市，每間門市都有 3 天的營收資料。
這次不只要印出每天營收，還要做基本分析。

已知資料：

stores = ["高雄店", "台南店", "台中店"]

revenues = [
    [3200, 4100, 3900],  # 高雄店
    [2800, 3000, 3500],  # 台南店
    [4500, 4700, 4600]   # 台中店
]

days = ["星期一", "星期二", "星期三"]


題目要求：

請用巢狀迴圈完成以下功能：

1. 印出每間門市每天的營收

預期格式：

高雄店 星期一 營收:3200 元
高雄店 星期二 營收:4100 元
高雄店 星期三 營收:3900 元

2. 每間門市印完 3 天營收後，印出該門市的「三天總營收」

預期格式：

高雄店 三天總營收:11200 元 (只是範例數字不一定正確)

3. 判斷每間門市的營收表現

規則如下：

三天總營收 >= 13000:表現優秀
三天總營收 >= 10000:表現正常
三天總營收 < 10000:需要加油

預期格式：

高雄店 表現：正常

4. 最後印出「全公司三天總營收」

預期格式：

全公司三天總營收:36300 元(只是範例數字不一定正確)


限制：

1. 請使用巢狀迴圈
2. 請使用 range(len(...))
3. 先不要使用 sum()
4. 先不要使用 enumerate()
5. 先不要使用 zip()
6. 先不要使用 max()
7. 先不要使用 min()


提示：

外層迴圈控制「第幾間門市」
內層迴圈控制「第幾天」

stores[i]       代表第 i 間門市
days[j]         代表第 j 天
revenues[i][j]  代表第 i 間門市第 j 天的營收

妳可能會需要兩個累加變數：

store_total    用來記錄單一門市三天總營收
company_total  用來記錄全公司三天總營收
"""

stores = ["高雄店", "台南店", "台中店"]

revenues = [
    [3200, 4100, 3900],  # 高雄店
    [2800, 3000, 3500],  # 台南店
    [4500, 4700, 4600]   # 台中店
]

days = ["星期一", "星期二", "星期三"]

company_total = 0  # 用來記錄全公司三天總營收

for store_index in range(len(stores)):

    store_total = 0  # 用來記錄單一門市三天總營收

    for day_index in range(len(days)):
        print(
            f"{stores[store_index]} {days[day_index]} 營收:{revenues[store_index][day_index]} 元")
        store_total += revenues[store_index][day_index]

    company_total += store_total

    print(f"{stores[store_index]} 三天總營收:{store_total} 元")

    if store_total >= 13000:
        print(f"{stores[store_index]} 表現: 優秀")
        print()
    elif store_total >= 10000:
        print(f"{stores[store_index]} 表現: 正常")
        print()
    elif store_total < 10000:
        print(f"{stores[store_index]} 需要加油")
        print()

print(f"全公司三天總營收:{company_total} 元")
