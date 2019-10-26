from . import BasicTests


class UserTestCase(BasicTests):

    def test_user_create(self):
        user = {'username': 'user1', 'password': 'pass1'}

        res = self.post('/api/v1/user', user)
        self.assertEqual(res.status_code, 201)

    def test_user_create_duplicated(self):
        user1 = {'username': 'user1', 'password': 'pass1'}
        user2 = {'username': 'user1', 'password': 'pass1'}

        res = self.post('/api/v1/user', user1)
        self.assertEqual(res.status_code, 201)

        res = self.post('/api/v1/user', user2)
        self.assertEqual(res.status_code, 401)

    def test_user_get(self):
        user = {'username': 'user1', 'password': 'pass1'}

        # create user
        res = self.post('/api/v1/user', user)
        self.assertEqual(res.status_code, 201)

        # call without authorization
        user_id = res.json.get('id')
        res = self.get(f'/api/v1/user/{user_id}')
        self.assertEqual(res.status_code, 403)

        # login
        res = self.post('/api/v1/auth/login', user)
        self.assertEqual(res.status_code, 200)

        access_token = res.json.get('access_token')
        res = self.get(f'/api/v1/user/{user_id}', jwt=access_token)
        self.assertEqual(res.status_code, 200)
