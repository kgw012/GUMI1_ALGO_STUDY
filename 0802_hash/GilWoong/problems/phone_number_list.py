# 프로그래머스 문제 '전화번호 목록'
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book: list):
    book_dict = {}

    for phone_num in phone_book:
        book_dict[phone_num] = 1
    
    for phone_num in phone_book:
        for i in range(1, len(phone_num)):
            compare_num = phone_num[:i]
            if book_dict.get(compare_num):
                return False
    
    return True


if __name__=='__main__':

    test_cases = [
        {
            'phone_book': ["119", "97674223", "1195524421"],
            'answer': False 
        },
        {
            'phone_book': ["123","456","789"],
            'answer': True
        },
        {
            'phone_book': ["12","123","1235","567","88"],
            'answer': False
        }
    ]
    
    for test_case in test_cases:
        phone_book = test_case['phone_book']
        answer = test_case['answer']
        my_answer = solution(phone_book)

        print(f'answer: {answer}, my_answer: {my_answer}')