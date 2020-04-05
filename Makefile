GIT_COMMIT=$(shell git rev-parse --verify HEAD)
PROJECT_NAME=hlpr
PROTO_DIR=./$(PROJECT_NAME)/proto
STUB_DIR=./$(PROJECT_NAME)/services/stubs


DOCKER_CMD=docker run --rm \
			-v $(pwd)/docs:/out \
			-v $(pwd)/hlpr/proto:/protos \
			pseudomuto/protoc-gen-doc


.PHONY: protogen_py
protogen_py: 
	python -m grpc_tools.protoc -I $(PROTO_DIR) \
		--python_out=$(STUB_DIR) \
		--grpc_python_out=$(STUB_DIR) $(PROTO_DIR)/user.proto $(PROTO_DIR)/task.proto


.PHONY: run-grpc-api-server
run-grpc-api-server:
	python -m $(PROJECT_NAME).apis.grpc

# One for each service
.PHONY: build
build:
	docker build \
    --build-arg GIT_COMMIT=${GIT_COMMIT} \
    -t $(PROJECT_NAME):latest \
    -t $(PROJECT_NAME):${GIT_COMMIT} \
    .

.PHONY: generate_proto_docs 
generate_proto_docs:
	@rm -f docs/*
	@$(DOCKER_CMD) --doc_opt=html,proto-docs.html
	@$(DOCKER_CMD) --doc_opt=markdown,proto-docs.md
	# @$(DOCKER_CMD) --doc_opt=/templates/asciidoc.tmpl,proto-docs.txt

	