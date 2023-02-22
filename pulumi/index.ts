import { lambda as textToSpeechLambda } from './infra/lambdas/textToSpeechLambda'
import { lambda as summarizeLambda } from './infra/lambdas/summarizeLambda'

import { api as textToSpeechAPI} from './infra/api'
import { bucket } from './infra/s3'

Object.keys(textToSpeechLambda)
Object.keys(summarizeLambda)
Object.keys(textToSpeechAPI)

export const API_URL = textToSpeechAPI.url
export const bucketName = bucket.id;