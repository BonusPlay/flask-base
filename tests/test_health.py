from . import BasicTests


class HealthTestCase(BasicTests):

    def test_swagger(self):
        res = self.app.get('/api/v1/')
        self.assertEqual(res.status_code, 200)

    def test_ping(self):
        res = self.app.get('/api/v1/health/ping')
        self.assertEqual(res.status_code, 200)
