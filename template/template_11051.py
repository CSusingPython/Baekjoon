"""
평균은 넘겠지
link : https://www.acmicpc.net/problem/11051

# 문제
> 자연수 과 정수 가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

# 입력
> 첫째 줄에 $N$과 $K$가 주어진다. (1 ≤ $N$ ≤ 10, 0 ≤ $K$ ≤ $N$)

# 출력
> ${n \choose k}$ 를 출력한다.

"""
import sys
read_input = sys.stdin.readline


def main():
    # 1. input 값을 받아오기
    input_string = read_input()
    N, K = input_string.split(" ")
    N, K = int(N), int(K)  # string을 integer로 변환

    # 2. 결과 값을 계산하기
    value = solve_binomial_coefficient(N, K)

    # 3. 결과 값을 출력하기
    print(value)


def solve_binomial_coefficient(N, K):
    """
    이항계수를 구하는 부분
    """
    # FIXME
    return 0


if __name__ == "__main__":
    main()
