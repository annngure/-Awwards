from django.test import TestCase
from . models import *
# Create your tests here.

class LocationTestClass(TestCase):

    #Set up method the test for location 
  def setUp(self):
    self.test_location = Location(name = 'Kericho')
    self.test_location.save()

    #Testing instance

  def test_instance(self):
    self.assertTrue(isinstance(self.test_location, Location))

    #Testing Save method

  def test_save_method(self):
    locations = Location.objects.all()
    self.assertTrue(len(locations)>0)

    # Tear down method
  def tearDown(self):
    Location.objects.all().delete()

        # Testing delete method

  def test_delete_location(self):
    self.test_location.delete()
    self.assertEqual(len(Location.objects.all()), 0)



class Review(TestCase):
  def setUp(self):
    self.ann = User.objects.create(username="try")
    self.image = Image.objects.create(image='image1',user=self.ann)
    self.comment = Review.objects.create(comment = 'goodbackground')
    self.test_review = Review.objects.create(user=self.ann,image=self.image ,comment='goodbackground')
    self.test_review.save()

    #Testing instance

  def test_instance(self):
    self.assertTrue(isinstance(self.test_reviews, Review))

    #Testing Save method
  def test_save_method(self):
    reviews = Review.objects.all()
    self.assertTrue(len(reviews)>0)

  def test_save_review(self):
    self.assertEqual(len(Review.objects.all()), 1)

    # Tear down method
  def tearDown(self):
    Review.objects.all().delete()

     # Testing delete method
  def test_delete_review(self):
    self.test_review.delete()
    self.assertEqual(len(Review.objects.all()), 0)
        

class ProfileTest(TestCase):
  def setUp(self):
    self.user = User(username='mary',email="mary@gmail.com", password='password')
    self.user.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_user(self):
    self.user.save()

  def test_delete_user(self):
    self.user.delete()

class ProjectTest(TestCase):
  def test_instance(self):
    self.assertTrue(isinstance(self.user, User))

  def test_save_projectr(self):
    self.user.save()

  def test_delete_project(self):
    self.user.delete()
      