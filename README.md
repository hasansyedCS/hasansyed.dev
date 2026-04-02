# hasansyed.dev

[![Portfolio](https://img.shields.io/badge/Portfolio-hasansyed.dev-blue)](https://hasansyed.dev)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF)](https://github.com/hasansyedCS/hasansyed.dev/actions)
[![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4)](https://github.com/hasansyedCS/hasansyed.dev/tree/main/infrastructure)
[![AWS](https://img.shields.io/badge/AWS-SAA--C03-orange)](https://aws.amazon.com/certification/certified-solutions-architect-associate/)

Live Deployment: [https://hasansyed.dev](https://hasansyed.dev)

Serverless personal portfolio deployed with AWS S3 + Cloudfront, with an HTML frontend, and DynamoDB + Lambda backend.

## Architecture

```mermaid
graph TD
    User[User Browser] --> CF[CloudFront CDN]
    
    subgraph "Static Content"
        CF --> S3[S3 Bucket\nindex.html + CSS + JS]
    end
    
    subgraph "Visitor Counter API"
        CF --> API[API Gateway\nPOST /visitor]
        API --> Lambda[Lambda\nPython]
        Lambda --> DB[(DynamoDB\nVisitor Count)]
    end
    
    subgraph "Management"
        TF[Terraform] -->|Provisions| AWS[AWS Resources]
        GH[GitHub Actions] -->|Deploys on push| CF
        GH -->|Deploys on push| Lambda
    end
```

