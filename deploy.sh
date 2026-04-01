#!/bin/bash
aws s3 sync ./ ./ s3://hasansyed.dev --delete
aws cloudfront create-invalidation --distribution-id YOUR_DISTRIBUTION_ID --paths "/*"
echo "Deployment complete!"