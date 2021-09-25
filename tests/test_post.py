import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
  def setUp(self):
      self.user_Mark = User(first_name = "Mark",
                              last_name = "Muchiri",
                              username = "1offmark",
                              password = "easy",
                              email = "markmm@mail.com")
      self.new_post = Post(post_title = "Sample Title",
                           post_content = "kak dela, detka, kuda ty idesh'",
                           user_id = self.user_Mark.id)
      self.new_comment = Comment(comment = "Great job",
                                 post_id = self.new_post.id,
                                 user_id = self.user_Mark.id)

  def test_instance(self):
      self.assertTrue(isinstance(self.user_Mark, User))
      self.assertTrue(isinstance(self.new_post, Post))
      self.assertTrue(isinstance(self.new_comment, Comment))