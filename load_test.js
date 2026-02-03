import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10, // 10 virtual users
  duration: '30s', // Test for 30 seconds
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};

export default function () {
  const url = 'http://localhost:8000/health';
  const res = http.get(url);
  
  check(res, {
    'status is 200': (r) => r.status === 200,
    'protocol is HTTP/1.1': (r) => r.proto === 'HTTP/1.1',
  });
  
  sleep(1);
}
