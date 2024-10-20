#Quiz 3 영화 별점 평균 계산기
class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_average_review(self):
        return sum(self.reviews) / len(self.reviews) if self.reviews else 0

    def display_movie_info(self):
        return f"영화 제목: {self.title}, 영화 감독: {self.director}, 개봉 년도: {self.release_year}, 평균 별점: {self.get_average_review():.2f}"

# 사용자 입력 받기
title = input("영화 제목을 입력하세요 : ")
director = input("영화 감독 이름을 입력하세요 : ")
release_year = int(input("개봉년도을 입력하세요 : "))

# Movie 객체 생성
movie = Movie(title, director, release_year)

# 별점 추가
while True:
    review_input = input("별점을 적어주세요. : (별점 작성을 종료하려면 '종료' 를 입력해주세요.): ")
    if review_input.lower() == '종료':
        break
    else:
        try:
            review = float(review_input)
            movie.add_review(review)
        except ValueError:
            print("숫자로 입력하세요.")

# 영화 정보 출력
print(movie.display_movie_info())
