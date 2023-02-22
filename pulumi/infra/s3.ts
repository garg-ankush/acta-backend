import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";


const STACK = "dev"

export const bucket = new aws.s3.Bucket(`polly-audio-bucket`, {
    bucket: `polly-audio-bucket-${STACK}`
})

export const accessBucketPolicy = new aws.iam.Policy(`access-polly-bucket`, {
    description: "IAM policy for accessing S3",
    path: "/",
    policy: bucket.arn.apply(arn => `{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": [
				  "s3:GetObject"
              ],
              "Resource": [
                "${arn}",
                "${arn}/*"
              ],
              "Effect": "Allow"
            }
          ]
        }
        `)
});