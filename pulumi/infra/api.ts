import * as awsx from "@pulumi/awsx/classic";
import { lambda as textToSpeechLambda } from './lambdas/textToSpeechLambda'
import { lambda as summarizeLambda } from './lambdas/summarizeLambda'

export const api = new awsx.apigateway.API(
    `text-to-speech-api-gateway`, {
        stageName: 'DEV',
        routes: [
            {
                path: "/textToSpeech",
                method: "POST",
                eventHandler: textToSpeechLambda
            },
            {
                path: "/summarize",
                method: "POST",
                eventHandler: summarizeLambda
            },

        ]
    }
)