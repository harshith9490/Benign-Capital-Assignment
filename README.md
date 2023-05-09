# Benign-Capital-Assignment

1. Study about super trend indicator, it’s a very popular indicator, which can be easily understood through Google search.
2. Get Raw Market Data from this api https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
3. Apply super trend indicator to generate on each 5 min candle. You can use super trend variable as follows
ATR PERIOD = 7
MULTIPLIER = 3


# Super Trend Indicator
1. It was created by olivier seban
2. It will show the trend following indicator based on ATR(Average True Range)\n
3. It combines thge Trend Detection and volatility\n
4. Used to detect the changes in Trend Detection\n
5. Basic Upper Band = (high+low)/2 + (multiplier * ATR)\n
6. Basic lower Band = (high+low)/2 - (multiplier * ATR)\n

7. final upper band = if(previous final upper band > previous close ) \n
8.                       Then min(Basic upper Band , Previous Final Upper Band)
9.                    else
10.                        Basic Upper Band
11.                        
12. 
13. final lower band = if(previous final lower band < previous close ) 
14.                       Then max(Basic lower Band , Previous Final lower Band)
15.                    else
16.                        Basic lower Band
17. Super Trend = if(Previous super trend == Previous Final Upper Band AND Current Close <= Current Final Upper Band) OR
18.                  (Previous Super Trend == Previous Final Lower Band AND Current Close >= Current Fina Lower Band)
19.                 Then
20.                    Previous Final Upper/Lower Band
21.               else
22.                     Current Super Trend
                    
