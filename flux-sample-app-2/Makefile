check-env:
ifndef BUCKET_NAME
	$(error BUCKET_NAME is undefined, example: make pack_deploy BUCKET_NAME=lambda-bucket STACK_NAME=ecr-flux-sample-app-2)
	exit 1
else
	@echo $(BUCKET_NAME)
endif

ifndef STACK_NAME
	$(error STACK_NAME is undefined, example: make pack_deploy BUCKET_NAME=lambda-bucket STACK_NAME=ecr-flux-sample-app-2)
	exit 1
else
	@echo $(STACK_NAME)
endif

ifndef GITHUB_TOKEN
	$(error GITHUB_TOKEN is undefined, example: make pack_deploy BUCKET_NAME=lambda-bucket STACK_NAME=ecr-flux-sample-app-2 GITHUB_TOKEN=tokennnn)
	exit 1
else
	@echo $(GITHUB_TOKEN)
endif

python_build_depen: 
	pip3 install -t cd_flux/ -r cd_flux/requirements.txt

simpl_deploy:
	sam build -u \
	&& sam deploy --guided --profile ${PROFILE}

pack_deploy: check-env python_build_depen
	sam build -u \
	&& sam package --template-file template.yaml --s3-bucket ${BUCKET_NAME} --output-template-file packaged.yaml \
	&& sam deploy -t packaged.yaml --stack-name ${STACK_NAME} --s3-bucket ${BUCKET_NAME} --capabilities CAPABILITY_IAM --parameter-overrides githubToken=${GITHUB_TOKEN}

build:
	sam build -u --debug

