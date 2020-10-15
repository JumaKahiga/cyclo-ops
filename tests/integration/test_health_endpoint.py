from tests import EndpointTestCase


class TestHealthCheck(EndpointTestCase):
    def test_health_check(self):
        resp = self.app_client.get('/health')

        assert resp.status_code == 200
        assert resp.json() == {'service_status': 'healthy'}