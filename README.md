
![](assets/img/hlpr-logo.png)


> **hlpr** - A submission to `Hack the Crisis - Sweden`.

## Pitch
* People who have symptoms and those around them should self-isolate and stay at home meaning basic daily tasks become a hurdle and businesses lose customers hurting their economy.
* **hlpr** is an easy-to-use app that enables those who want and can help to support those who need help with specific tasks within a certain time frame and in a trustworthy way.
* By gamifying the experience and providing helpers with 'hlpr-points' that can be converted into giftcards or redeemed at partner businesses during transactions this app also helps businesses stay afloat under the economic pressure.


## Backend 

This repository contains the code for the hlpr backend. A submission to `Hack the Crisis - Sweden`.

## Repo Structure 

```bash 
.
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── api_config.yaml
├── api_descriptor.pb
├── assets
│   └── img
│       └── hlpr-logo.png
├── docs
│   ├── proto-docs.html
│   └── proto-docs.md
├── hlpr
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── apis
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   └── grpc.py
│   ├── client
│   │   ├── __init__.py
│   │   └── client.py
│   ├── proto
│   │   ├── task.proto
│   │   └── user.proto
│   └── services
│       ├── __init__.py
│       ├── db
│       │   ├── __init__.py
│       │   ├── conn.py
│       │   ├── helpr.db
│       │   ├── mock.py
│       │   └── models.py
│       ├── servicers
│       │   ├── __init__.py
│       │   ├── task.py
│       │   └── user.py
│       └── stubs
│           ├── __init__.py
│           ├── task_pb2.py
│           ├── task_pb2_grpc.py
│           ├── user_pb2.py
│           └── user_pb2_grpc.py
└── requirements.txt
```

## Protobuf

The client and server code is generated from `task.proto` & `user.proto` files residing in `hlpr/proto`. 

The stubs and descriptor can be regenerated using: 

```bash
python -m grpc_tools.protoc -I hlpr/proto \
			--include_imports \
			--include_source_info \
			--python_out=hlpr/services/stubs \
			--descriptor_set_out=api_descriptor.pb \
			--grpc_python_out=hlpr/services/stubs hlpr/proto/user.proto hlpr/proto/task.proto 
```

The backend consits of a grpc server `hlpr/apis/grpc.py`.

The actual implementation will contain 3 servicers:

* `TaskServicer`
* `UserServicer` 
* `BountyServicer`

This is where the actual logic is implemented `hlpr/services/servicers`. 

### proto-docs

You can generate the docs using the following docker image `docker pull pseudomuto/protoc-gen-doc`: 

```bash
docker run --rm \
  -v $(pwd)/docs:/out \
  -v $(pwd)/hlpr/proto:/protos \
  pseudomuto/protoc-gen-doc
```

> Default is `html` but you can change this with `--doc_opt=markdown,docs.md`


## Deployment

Currently, the implementation can be deployed to `GKE` following this guide: https://cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine


## TODO 

- [ ] Add auth 
- [ ] Add bounty Service 
- [ ] Add BankId Integration 
- [ ] Add Swish Integration ?? 
- [x] Add K8s Manifests 


## Team description

We are a team of colleagues who work in the digital department at Volvo Cars. Amongst us we have different focus areas such as data science, software development and user research. We also have different nationalities and we 

**Team contact info** 

* Leonard Aukea: leonard.aukea@gmail.com 
* Carolina Jaramillo: jaramillo.carolina@gmail.com 
* Oriol Lopez Torres: lopez.torres.oriol@gmail.com
* Ashwin Rajamohan: ashwin.rajamohan@gmail.com 
* Geroge Markhulia: markhulia@gmail.om 

**Github Org**: https://github.com/hlpr-hackers