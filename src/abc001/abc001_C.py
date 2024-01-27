from decimal import ROUND_HALF_UP, Decimal

deg, dis = map(float, input().split())
wind_v = Decimal(f"{dis/60:.2f}")
wind_v = wind_v.quantize(Decimal(".1"), rounding=ROUND_HALF_UP)

wind_range = [-0.1, 0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]
wind_p = 12
for i in range(len(wind_range)-1):
    if Decimal(wind_range[i]+0.09) <= wind_v <= Decimal(wind_range[i+1]+0.01):
        wind_p = i
        break

Dir = "N"
dirs = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
dir_range = [11.25, 33.75, 56.25, 78.75, 101.25, 123.75, 146.25, 168.75, 191.25, 213.75, 236.25, 258.75, 281.25, 303.75, 326.25, 348.75]
for i in range(len(dir_range)-1):
    if dir_range[i] <= deg / 10 < dir_range[i+1]:
        Dir = dirs[i]
if wind_p == 0:
    Dir = "C"

print(Dir,wind_p)

# 風力の計算で境界部分の誤差により, 風速がどの範囲にも属さないケースがあったので範囲を緩和した
