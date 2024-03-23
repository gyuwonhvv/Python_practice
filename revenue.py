# 월 평균 매출 구하기
with open('revenue_31days.txt', 'r') as d:
    total_revenue = 0
    total_days = 0
    for line in d:
        data = line.strip().split(": ")
        revenue = int(data[1])
        
        total_revenue += revenue
        total_days += 1
    
    print(int(total_revenue / total_days))
