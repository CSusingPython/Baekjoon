"""
평균은 넘겠지
link : https://www.acmicpc.net/problem/4344

# 문제
> 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
  당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
> 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
  둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
  이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
> 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

"""
import sys
read_input = sys.stdin.readline


def main():
    C = int(read_input())  # 테스트 케이스의 갯수 C개가 주어짐

    results = []
    for i in range(C):
        # Input string이 주어짐
        input_string = read_input()

        # Input String를 Int list로 parsing함
        int_list = parse_input_string(input_string)

        # 평균을 넘는 학생들의 비율을 계산
        num_over_average = calculate_ratio(int_list)

        # 비율을 반올림하여, 소수점 셋째 자리까지의 string으로 변환
        result = convert_float_to_string_format(num_over_average)

        # 결과를 list에 담음
        results.append(result)

    print("\n".join(results))


def parse_input_string(string):
    return [int(number) for number in string.split(' ')]


def calculate_ratio(int_list):
    count = int_list[0]
    average = sum(int_list[1:]) / count
    return len(list(filter(lambda x : x > average, int_list[1:]))) / count


def convert_float_to_string_format(float_value):
    return "{:2.3f}%".format(float_value*100)


if __name__ == "__main__":
    main()