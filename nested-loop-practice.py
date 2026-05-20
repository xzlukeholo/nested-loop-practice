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
