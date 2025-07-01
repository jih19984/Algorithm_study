# N: 전투 시간(second), M: B 스킬 시전시간
# N,M 입력
N, M = map(int,input().split())
Mod = 1000000007
# dp 리스트 생성
dp = [0] * (N+1)

# 규칙 찾기 
# 예시 N=4, M=2
# dp[0]=1
# dp[1]=1
# dp[2]=2
# dp[3]=3
# dp[4]=5
# dp[i+1]=dp[i-1]+dp[i]

for i in range(1,N+1):
    dp[0]=1
    dp[i]=dp[i-1]
    if N>=M:
        dp[i]=dp[i]+dp[i-M]

print(dp[N]%Mod)
