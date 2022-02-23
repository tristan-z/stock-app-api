import unittest
from routes.news import news, data as test_data, default_limit, default_index
from app import app
import json


# TODO: finish the rest of tests

class TestNewsRoute(unittest.TestCase):

# 	http://localhost:5000/news?limit=2&index=0

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client

# TODO: generalize logic to elimite if and elif

    def get_response(self, *args, **kwargs):
        limit = kwargs.get("limit", None)
        index = kwargs.get("index", None)
        res = None
        if (limit and index is None):
            res = self.client().get("/news?limit=" + str(limit))
        elif (limit is None and index):
            res = self.client().get("/news?index=" + str(index))
        elif (limit and index):
            res = self.client().get('/news' + "?limit=" + str(limit) + "&index=" + str(index))
        else: 
            res = self.client().get('/news')
        # return tuple of response and python dict of response data
        return res, json.loads(res.data.decode("utf-8"))

    def test_success_response_code(self):
        res, _ = self.get_response()
        self.assertEqual(res.status_code, 200)  
    
    def test_response(self):
        _, data = self.get_response()
        self.assertIs(type(data["total"]), int)
        self.assertIs(type(data["message"]), list)

    def test_limit(self):
        _, data = self.get_response()
        self.assertEqual(len(data["message"]), default_limit)
        # if a value is given, it should override the default
        limit = default_limit + 1
        _, data = self.get_response(limit=limit)
        self.assertEqual(len(data["message"]), limit)

    def test_limit_invalid_value(self):
        self.assertEqual(True, False)

    def test_index(self):
        # if no value is given, the default should run
        _, data = self.get_response()
        self.assertEqual(data["message"][0], test_data[default_index])
        # if a value is given, it should override the default
        index = default_index + 1
        _, data = self.get_response(index=index)
        self.assertEqual(data["message"][0], test_data[index])


    def test_handle_invalid_index(self):
        self.assertEqual(True, False)

    def test_message(self):
        index = 3
        limit = 5
        _, data = self.get_response(index=index, limit=limit)
        #ensure that message contains an list of objects (dict in python)
        msg = data["message"]
        self.assertIs(type(msg[0]), dict)
        #ensure that message contains the desired subset of the list
        self.assertEqual(msg, test_data[index:index+limit])

    def test_total(self):
         # test that total is expected value
        _, data = self.get_response()
        self.assertEqual(data["total"], 20)

if __name__ == "__main__":
    unittest.main()
