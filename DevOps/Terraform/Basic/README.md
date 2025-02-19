## Terraform 기본요소

### 기본 구성요소

#### HCL(HashiCorp Configuration Language)
Terraform의 구성 파일은 HCl로 작성된다. HCL의 기본 문법과 구조를 이해해야한다.

#### Provider
Terraform은 다양한 클라우드 서비스 제공자(AWS, Azure, GCP등)를 지원한다.<br/>
각 프로바이더의 설정 방법과 리소스를 정의하는 방법을 알아야 한다.
````
provider "aws" {
  region = "us-west-2"
}
````

#### Resources
리소스는 실제 인프라의 구성 요소이다. 예를 들어, AWS의 EC2 인스턴스, S3 버킷 등이 리소스에 해당합니다.<br/> 
리소스를 정의하고 관리하는 방법을 배워야 한다.
````
variable "instance_type" {
  description = "EC2 인스턴스 타입"
  default     = "t2.micro"
}
````


#### Variables
변수는 코드의 재사용성을 높이고, 환경에 따라 다른 값을 설정할 수 있게 한다.<br/>
변수의 선언과 사용 방법을 알아야 한다.
````
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type

  tags = {
    Name = "ExampleInstance"
  }
}
````


#### Outputs
출력값은 Terraform 실행 후 생성된 리소스의 정보를 출력하는 데 사용된다.<br/>
출력값을 정의하고 사용하는 방법을 배워야 한다.
````
output "instance_id" {
  description = "생성된 인스턴스의 ID"
  value       = aws_instance.example.id
}
````


#### State Files
Terraform은 상태 파일을 사용하여 현재 인프라의 상태를 저장한다.<br/>
상태 파일의 역할과 관리 방법을 이해해야 한다.


#### Modules
모듈은 코드의 재사용성을 높이기 위해 사용된다. 
모듈을 작성하고 사용하는 방법을 배워야 한다.


#### Backends
백엔드는 상태 파일을 저장하는 위치를 정의한다.<br/>
로컬 파일 시스템, 원격 저장소(S3, Consul 등) 등을 사용할 수 있다.


#### Workspaces
워크스페이스는 동일한 구성 파일을 사용하여 여러 환경을 관리할 수 있게 합니다.<br/>
워크스페이스의 생성과 전환 방법을 알아야 합니다



### 접근 방식
#### 선언적 접근 방식
````
provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleInstance"
  }
}
````
* 최종 상태를 정의하고, Terraform이 필요한 단계를 자동으로 수행

#### 절차적 접근 방식
````python
import boto3

# AWS 세션 생성
session = boto3.Session(region_name='us-west-2')
ec2 = session.resource('ec2')

# EC2 인스턴스 생성
instance = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': 'ExampleInstance'}]
    }]
)

# 인스턴스 ID 출력
print(instance[0].id)
````
* 사용자가 모든 단계를 명시적으로 작성하여 수행


### 기본 명령어
| 명령어  |    실행 | 
| terraform init | 프로젝트 초기화 |
| terraform plan | 실행 계획을 생성 |
| terraform apply | 실행 계획을 적용 |
| terraform destroy | 인프라 리소스를 삭제 |
| terraform validate | 구성 파일의 문법을 검증 |
| terraform fmt | 구성 파일을 표준 형식으로 자동 정렬 |
| terraform show | 상태 파일이나 실행 계획의 내용을 표시 |
| terraform output | 출력값을 표시 |
| terraform refresh | 실제 인프라 상태를 최신 상태 파일로 업데이트 |
| terraform import | 기존 인프라를 Terraform 상태로 가쟈옴 |
| terraform taint | 특정 리소스를 강제로 재생성하도록 표시 |
| terraform untaint | taint된 리소스를 원래 상태로 되돌림 |
| terraform state | 상태 파일을 관리 |
| terraform workspace | 워크스페이스를 관리 |