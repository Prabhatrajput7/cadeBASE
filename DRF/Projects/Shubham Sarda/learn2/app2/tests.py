from inspect import stack
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse_lazy
# https://medium.com/@ksarthak4ever/test-driven-development-tdd-in-django-and-django-rest-framework-drf-a889a8068cb7
# Create your tests here.

"""Out db is not affected while running test case django will create a temporary db for testcase to check the fxality"""
# python manage.py test will run all tests.py under apps to run a perticular one do python manage.py test app2.tests
# class RegisterTC(APITestCase):
    
#     def test_reg_one(self):
#         data = {
#             "username":"trmit",
#             "email":"trmit@t.com",
#             "password":"qwertyOO7",
#             "password2":"qwertyOO7"
#         }
#         response = self.client.post(reverse('register'),data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class LoginLogoutTC(APITestCase):
#     """this class has nothing to do with registerclass"""
#     @classmethod
#     def setUpClass(cls):
#     # def setUp(self):
#         User.objects.create_user(username="termite",password="qwertyOO7")

#     def test_login_one(self):
#         data = {
#             "username":"termite",
#             "password":"qwertyOO7"
#         }
#         response = self.client.post(reverse('login'),data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_logout_one(self):
#         self.token = Token.objects.get(user__username='termite')
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#         response = self.client.post(reverse('logout'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     @classmethod
#     def tearDownClass(cls):
#     # def tearDownClass(self):
#         print('Done')

from app2.serializers import WatchListSerialz,StreamSerialz,ReviewSerializerz,ReviewSerializerzMVS
from app2.models import StreamPlatform,WatchList,Review

# class StreamTCS(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username="example", password="Password@123")
#         self.token = Token.objects.get(user__username=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#         """Adding the element for test case 2"""
#         self.stream = StreamPlatform.objects.create(name="Mxplayer", 
#                                 about="its a good one", website="https://www.mxplayer.com")


#     def test_streamplatform_create(self):
#         data = {
#             "name": "Mxplayer2",
#             "about": "its a good one2",
#             "website": "https://www.mxplayer2.com"
#         }
#         response = self.client.post(reverse('app2:streamplatform-list'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
#     def test_streamplatform_list(self):
#         response = self.client.get(reverse('app2:streamplatform-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_streamplatform_ind(self):
#         response = self.client.get(reverse('app2:streamplatform-detail', args=(self.stream.id,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class WatchListTestCase(APITestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username="example", password="Password@123")
#         self.token = Token.objects.get(user__username=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

#         self.stream = StreamPlatform.objects.create(name="Netflix", 
#                                 about="#1 Platform", website="https://www.netflix.com")
#         self.watchlist = WatchList.objects.create(platform=self.stream, title="Example Movie",
#                                 storyline="Example Movie", active=True)

#     def test_watchlist_create(self):
#         data = {
#             "platform": self.stream,
#             "title": "Example Movie",
#             "storyline": "Example Story",
#             "active": True
#         }
#         response = self.client.post(reverse('app2:watch'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         #  need to check this one
    
#     def test_watchlist_list(self):
#         response = self.client.get(reverse('app2:watch'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_watchlist_ind(self):
#         response = self.client.get(reverse('app2:watchlist-detail', args=(self.watchlist.id,)))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(WatchList.objects.count(), 1)
#         self.assertEqual(WatchList.objects.get().title, 'Example Movie')


class ResviewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = StreamPlatform.objects.create(name="Netflix", 
                                about="#1 Platform", website="https://www.netflix.com")
        self.watchlist = WatchList.objects.create(platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)
        self.watchlist2 = WatchList.objects.create(platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)
        self.review = Review.objects.create(review_user=self.user, rating=5, description="Great Movie", 
                                watchlist=self.watchlist2, active=True)

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }

        response = self.client.post(reverse('app2:review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 2)

        response = self.client.post(reverse('app2:review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            # "watchlist": self.watchlist2,
            "active": True
        }

        self.client.force_authenticate(user=None)
        # self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('app2:review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great Movie! - Updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(reverse('app2:review-detail', args=(self.watchlist.id,self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('app2:review-create', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_ind(self):
        response = self.client.get(reverse('app2:reviewind-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_ind_delete(self):
        """for view set we need to add -list or -detail"""
        response = self.client.delete(reverse('app2:ReviewViewSet-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get('/app2/reviewbyuser/?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_userbyusername(self):
        response = self.client.get(reverse('app2:review-filter', args=(self.user.username,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)