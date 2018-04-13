from app.models import Review,User
from app import db
def setUp(self):
        self.user_Rose = User(username = 'Vicklyne',password = '1234', email = 'vicklyneakinyi1@gmail.com')
        self.new_review = Review(movie_id=1234,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_Vicklyne )

def tearDown(self):
        Review.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,1234)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_Vicklyne)
