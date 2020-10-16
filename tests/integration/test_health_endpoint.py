from tests import EndpointTestCase


class TestHealthCheck(EndpointTestCase):
    def test_health_check(self):
        resp = self.app_client.get('/api/health')

        self.assertEqual(resp.status_code, 200)
        assert resp.json == {'service_status': 'healthy'}