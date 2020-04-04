compile_proto_py: 
	protoc --proto_path=protos --python_out=build/gen protos/task.proto protos/user.proto


compile_grpc_py: 
	python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/user.proto protos/task.proto