run-server:
	@echo "Running Load Testing for API "
	locust -f app/server/server.py --host=http://localhost:8881 -P 8081

run-client:
	@echo "Running Load Testing for Client Website "
	locust -f app/client/client.py --host=http://localhost:3000 -P 8082