from . import BasicTests


class AuthTestCase(BasicTests):

    def test_login(self):
        user = {'username': 'user1', 'password': 'pass1'}

        # create user
        res = self.post('/api/v1/user', user)
        self.assertEqual(res.status_code, 201)

        # send no JSON message
        res = self.app.post('/api/v1/user')
        self.assertEqual(res.status_code, 400)

        # proper login
        res = self.post('/api/v1/auth/login', user)
        self.assertEqual(res.status_code, 200)

        # invalid credentials
        user['password'] = 'invalid'
        res = self.post('/api/v1/user', user)
        self.assertEqual(res.status_code, 401)

    def test_protected(self):
        user = {'username': 'user1', 'password': 'pass1'}

        # create user
        res = self.post('/api/v1/user', user)
        self.assertEqual(res.status_code, 201)

        # login
        res = self.post('/api/v1/auth/login', user)
        self.assertEqual(res.status_code, 200)

        # call protected endpoint
        access_token = res.json.get('access_token')
        res = self.get('/api/v1/auth/test', jwt=access_token)
        self.assertEqual(res.status_code, 200)
