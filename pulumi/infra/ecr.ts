import * as awsx from "@pulumi/awsx";

const repository = new awsx.ecr.Repository("text-to-speech-image", {});

export const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    path: "./handlers/docker-build",
    env: {
        "DOCKER_DEFAULT_PLATFORM": "linux/amd64"
    }
});

export const summarizeImage = new awsx.ecr.Image("summarizeImage", {
    repositoryUrl: repository.url,
    path: "./handlers/docker-summarize",
    env: {
        "DOCKER_DEFAULT_PLATFORM": "linux/amd64"
    }
});


export const url = repository.url;