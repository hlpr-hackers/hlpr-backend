GIT_COMMIT=$(shell git rev-parse --verify HEAD)
PROJECT_NAME=hlpr
PROTO_DIR=./$(PROJECT_NAME)/proto
STUB_DIR=./$(PROJECT_NAME)/services/stubs

.PHONY: protogen_py
protogen_py: 
	python -m grpc_tools.protoc -I $(PROTO_DIR) \
		--python_out=$(STUB_DIR) \
		--grpc_python_out=$(STUB_DIR) $(PROTO_DIR)/user.proto $(PROTO_DIR)/task.proto

.PHONY: run-grpc-api-task-server
run-grpc-api-task-server:
	python -m $(PROJECT_NAME).apis.task_server


.PHONY: run-grpc-api-user-server
run-grpc-api-user-server:
	python -m $(PROJECT_NAME).apis.user_server


# One for each service
.PHONY: build
build:
	docker build \
    --build-arg GIT_COMMIT=${GIT_COMMIT} \
    -t $(PROJECT_NAME):latest \
    -t $(PROJECT_NAME):${GIT_COMMIT} \
    .

