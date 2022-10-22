# クラス作成

部門内および部門間の予算の入出金の記録が可能なクラス作成

## 1. 実行準備

リモートリポジトリから取得後に Python を対話モードで起動

```
$ git clone https://github.com/Makoto-Araki/boilerplate-budget-app.git
$ cd boilerplate-budget-app
$ python (対話モードで起動)
```

## 2. 食料部門

食料部門の生成後に部門内の入出金を記録

```
>>> import budget
>>> food = budget.Category("Food")  # インスタンス生成
>>> food.deposit(1000, "initial")   # 入金
>>> food.withdraw(10.15, "others")  # 出金
>>> food.withdraw(21.15, "others")  # 出金
```

## 3. 衣料部門

衣料部門の生成後に部門内の入出金を記録

```
>>> import budget
>>> clothing = budget.Category("Clothing")
>>> clothing.deposit(1000, "initial")
>>> clothing.withdraw(43.25, "others")
>>> clothing.withdraw(92.35, "others")
>>> clothing.withdraw(88.45, "others")
>>> clothing.withdraw(21.15, "others")
>>> clothing.withdraw(44.65, "others")
```

## 4. 予算振替

食料部門から衣料部門へ予算振替

```
>>> food.transfer(50, clothing)
>>> food.transfer(60, clothing)
```

## 5. 入出金記録

食料部門と衣料部門の入出金記録を表示

```
>>> print(food.get_balance())
>>> print(clothing.get_balance())

*************Food*************
initial                1000.00  # 入金
others                  -10.15  # 出金
others                  -21.15  # 出金
Transfer to Clothing    -50.00  # 予算振替(出金)
Transfer to Clothing    -60.00  # 予算振替(出金)
Total: 858.70                   # 残高
858.7                           # メソッドの戻り値

***********Clothing***********
initial                1000.00  # 入金
others                  -43.25  # 出金
others                  -92.35  # 出金
others                  -88.45  # 出金
others                  -21.15  # 出金
others                  -44.65  # 出金
Transfer from Food       50.00  # 予算振替(入金)
Transfer from Food       60.00  # 予算振替(入金)
Total: 820.15                   # 残高
820.15                          # メソッドの戻り値
```

## 6. 関数実行

各部門の支出が全体に対してどの程度の割合かを棒グラフで表示

```
>>> from budget import create_spend_chart
>>> print(create_spend_chart([food, clothing]))
Percentage spent by category
100|       
 90|       
 80|       
 70|       
 60|    o  
 50|    o  
 40|    o  
 30| o  o  
 20| o  o  
 10| o  o  
  0| o  o  
    -------
     F  C  
     o  l  
     o  o  
     d  t  
        h  
        i  
        n  
        g  
```