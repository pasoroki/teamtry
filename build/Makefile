#
# HOW TO provide custom tag (version)?
#   run `make all TAG=my_custom_tag`
#

PROJECT_NAME?=teamtry
REPOSITORY?=outlookmobile.azurecr.io/$(PROJECT_NAME)
TAG?=latest

OK_COLOR=\033[32;01m
NO_COLOR=\033[0m

build:
	@echo "$(OK_COLOR)==>$(NO_COLOR) Building $(PROJECT_NAME):$(TAG)"
	@docker build --rm -t $(PROJECT_NAME):$(TAG) .

$(REPOSITORY)_$(TAG).tar: build
	@echo "$(OK_COLOR)==>$(NO_COLOR) Saving $(PROJECT_NAME):$(TAG) > $@"
	@docker save $(REPOSITORY):$(TAG) > $@

tag:
	@echo "$(OK_COLOR)==>$(NO_COLOR) Tagging $(PROJECT_NAME):$(TAG)"
	@docker tag $(PROJECT_NAME):$(TAG) $(REPOSITORY):$(TAG)

push: build tag
	@echo "$(OK_COLOR)==>$(NO_COLOR) Pushing $(PROJECT_NAME):$(TAG)"
	@docker push $(REPOSITORY):$(TAG)

clean:
	@echo "$(OK_COLOR)==>$(NO_COLOR) Cleaning local repo"
	@docker rmi $(PROJECT_NAME):$(TAG)
	@docker rmi $(REPOSITORY):$(TAG)


all: build tag push clean

.PHONY: all build push clean tag
