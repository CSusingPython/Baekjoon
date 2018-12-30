import sys
read_input = sys.stdin.readline
# input value
"""
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

"""

def main():
    C = int(read_input())  # 테스트 케이스의 갯수 C개가 주어짐
    print("\ntest case input : ",C)
    results = []
    for i in range(C):
        print("test_case{}".format(i))
        # Input string이 주어짐
        input_string = read_input()
        # print(input_string)
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


