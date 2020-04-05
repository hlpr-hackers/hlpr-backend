GIT_COMMIT=$(shell git rev-parse --verify HEAD)
PROJECT_NAME=hlpr
PROTO_DIR=./$(PROJECT_NAME)/proto
STUB_DIR=./$(PROJECT_NAME)/services/stubs
GCR_PROJECT=hack-the-crisis-hlpr
IMAGE_NAME=python-grpc-hlpr-server
GCR_REGISTRY=gcr.io/$(GCR_PROJECT)/$(IMAGE_NAME)
  

DOCKER_CMD=docker run --rm \
			-v $(pwd)/docs:/out \
			-v $(pwd)/hlpr/proto:/protos \
			pseudomuto/protoc-gen-doc


.PHONY: protogen_py
protogen_py: 
	python -m grpc_tools.protoc -I $(PROTO_DIR) \
		--python_out=$(STUB_DIR) \
		--grpc_python_out=$(STUB_DIR) $(PROTO_DIR)/user.proto $(PROTO_DIR)/task.proto


.PHONY: protogen_descriptor
protogen_descriptor:
	python -m grpc_tools.protoc -I $(PROTO_DIR) \
			--include_imports \
			--include_source_info \
			--python_out=$(STUB_DIR) \
			--descriptor_set_out=api_descriptor.pb \
			--grpc_python_out=$(STUB_DIR) $(PROTO_DIR)/user.proto $(PROTO_DIR)/task.proto 
	
	
.PHONY: generate_proto_docs 
generate_proto_docs:
	@rm -f docs/*
	@$(DOCKER_CMD) --doc_opt=html,proto-docs.html
	@$(DOCKER_CMD) --doc_opt=markdown,proto-docs.md
	# @$(DOCKER_CMD) --doc_opt=/templates/asciidoc.tmpl,proto-docs.txt


.PHONY: run-grpc-api-server
run-grpc-api-server:
	python -m $(PROJECT_NAME).apis.grpc

.PHONY: run-client
run-client:
	python -m $(PROJECT_NAME).client.client	

# One for each service
.PHONY: build
build:
	docker build \
    --build-arg GIT_COMMIT=${GIT_COMMIT} \
    -t $(GCR_REGISTRY):latest \
    -t $(GCR_REGISTRY):${GIT_COMMIT} \
    .


.PHONY: gcloud-deploy 
gcloud-deploy: 
	gcloud endpoints services deploy $(pwd)/api_descriptor.pb $(pwd)/api_config.yaml


	